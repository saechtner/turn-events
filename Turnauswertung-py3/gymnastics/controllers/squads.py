import re
from subprocess import Popen, PIPE
import tempfile

from django.db.models import Sum
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import Context
from django.template.loader import get_template
from django.utils.translation import ugettext_lazy
from django.views import generic

from gymnastics.models.athlete import Athlete
from gymnastics.models.discipline import Discipline
from gymnastics.models.performance import Performance
from gymnastics.models.squad import Squad
from gymnastics.models.stream import Stream


def index(request):
    context = { 'squads': Squad.objects.all() }
    return render(request, 'gymnastics/squads/index.html', context)

def detail(request, id):
    squad = Squad.objects.get(id=id)

    #### Athletes ###
    athletes = squad.athlete_set.all() \
        .select_related('club').select_related('stream').select_related('team__stream').select_related('squad') \
        .prefetch_related('performance_set')

    ### Streams ###
    streams_distinct = set([athlete.stream for athlete in athletes])
    stream_athletes_disciplines = { stream.id: {'athletes': [], 'disciplines': stream.ordered_disciplines.all()} for stream in streams_distinct }
    for athlete in athletes:
        stream_athletes_disciplines[athlete.stream.id]['athletes'].append(athlete)

    # Results Athletes: disciplines results
    athletes_discipline_results = squad.athlete_set.all() \
        .values('id', 'performance__discipline_id') \
        .annotate(performance_result=Sum('performance__value'))
    athletes_disciplines_result_dict = { athlete.id: {} for athlete in athletes }
    for result in athletes_discipline_results:
        athletes_disciplines_result_dict[result['id']][result['performance__discipline_id']] = result['performance_result']
    context = { 
        'squad': squad,
        'athletes': athletes,
        'athletes_count': len(athletes),
        'athletes_disciplines_result_dict': athletes_disciplines_result_dict,
        'streams': streams_distinct,
        'stream_athletes_disciplines': stream_athletes_disciplines
    }
    return render(request, 'gymnastics/squads/detail.html', context)

def enter_performances(request, id):        
    squad = Squad.objects.get(id=id)

    #### Athletes ###
    athletes = squad.athlete_set.all() \
        .select_related('club').select_related('stream').select_related('team__stream').select_related('squad') \
        .prefetch_related('performance_set')

    ### Streams ###
    streams_distinct = set([athlete.stream for athlete in athletes])
    stream_athletes_disciplines = { stream.id: {'athletes': [], 'disciplines': stream.ordered_disciplines.all()} for stream in streams_distinct }

    for athlete in athletes:
        stream_athletes_disciplines[athlete.stream.id]['athletes'].append(athlete)

    stream_discipline_tabindex_dict = { stream.id: { discipline.id: int('{0}{1}'.format(stream_index+1, discipline_index)) for discipline_index, discipline in enumerate(stream.ordered_disciplines.all()) } for stream_index, stream in enumerate(streams_distinct) }

    # Results Athletes: disciplines results
    athletes_discipline_results = squad.athlete_set.all() \
        .values('id', 'performance__discipline_id') \
        .annotate(performance_result=Sum('performance__value'))
    athletes_disciplines_result_dict = { athlete.id: {} for athlete in athletes }

    for result in athletes_discipline_results:
        athletes_disciplines_result_dict[result['id']][result['performance__discipline_id']] = result['performance_result']

    context = { 
        'squad': squad,
        'athletes': athletes,
        'athletes_count': len(athletes),
        'athletes_disciplines_result_dict': athletes_disciplines_result_dict,
        'streams': streams_distinct,
        'stream_athletes_disciplines': stream_athletes_disciplines,
        'stream_discipline_tabindex_dict': stream_discipline_tabindex_dict
    }

    return render(request, 'gymnastics/squads/enter_performances.html', context)

def handle_entered_performances(request):
    performance_dict = request.POST

    athletes = Athlete.objects.all()
    disciplines = Discipline.objects.all()
    performances = Performance.objects.all()

    for key, value in performance_dict.items():
        if '-' in key and value:
            athlete_id, performance_id = re.split(r'-+', key.rstrip())

            athlete = athletes.get(id=athlete_id)
            discipline = disciplines.get(id=performance_id)

            try:
                performance = performances.get(athlete=athlete, discipline=discipline)
                performance.value = value
            except:
                performance = Performance( \
                    value=value,
                    athlete=athlete,
                    discipline=discipline)

            performance.save()

    return redirect(reverse('squads.index'))

def judge_pdf(request):
    squads = Squad.objects.all().prefetch_related('athlete_set')
    squad_disciplines = {}
    for squad in squads:
        squad_disciplines[squad.id] = []
        athletes = squad.athlete_set.all().select_related('stream')
        for athlete in athletes:
            squad_disciplines[squad.id].extend([ discipline for discipline in athlete.stream.ordered_disciplines.all() ])
        squad_disciplines[squad.id] = set(squad_disciplines[squad.id])

    context = Context({
            'squads': squads,
            'squad_disciplines': squad_disciplines,
        })

    template = get_template('gymnastics/squads/squads_judges.tex')
    rendered_tpl = template.render(context).encode('utf-8')

    with tempfile.TemporaryDirectory() as tempdir:
        # Create subprocess, supress output with PIPE and 
        # run latex twice to generate the TOC properly. 
        # Finally read the generated pdf.
        for i in range(2):
            process = Popen(
                ['pdflatex', '-output-directory', tempdir],
                stdin=PIPE,
                stdout=PIPE,
            )
            process.communicate(rendered_tpl)
        with open(os.path.join(tempdir, 'texput.pdf'), 'rb') as f:
            pdf = f.read()

    r = HttpResponse(content_type='application/pdf')
    # r['Content-Disposition'] = 'attachment; filename={0}_{1}_{2}.pdf'.format(ugettext_lazy('Squads'), ugettext_lazy('Judge'), ugettext_lazy('Lists'))
    r['Content-Disposition'] = 'filename={0}_{1}_{2}.pdf'.format(ugettext_lazy('Squads'), ugettext_lazy('Judge'), ugettext_lazy('Lists'))
    r.write(pdf)
    return r

def overview_pdf(request):
    squads = Squad.objects.all().prefetch_related('athlete_set').select_related('athlete_set__club')

    context = Context({
            'squads': squads,
        })

    template = get_template('gymnastics/squads/squads_athletes.tex')
    rendered_tpl = template.render(context).encode('utf-8')

    with tempfile.TemporaryDirectory() as tempdir:
        # Create subprocess, supress output with PIPE and 
        # run latex twice to generate the TOC properly. 
        # Finally read the generated pdf.
        for i in range(2):
            process = Popen(
                ['pdflatex', '-output-directory', tempdir],
                stdin=PIPE,
                stdout=PIPE,
            )
            process.communicate(rendered_tpl)
        with open(os.path.join(tempdir, 'texput.pdf'), 'rb') as f:
            pdf = f.read()

    r = HttpResponse(content_type='application/pdf')
    # r['Content-Disposition'] = 'attachment; filename={0}_{1}.pdf'.format(ugettext_lazy('Squads'), ugettext_lazy('Overview'))
    r['Content-Disposition'] = 'filename={0}_{1}.pdf'.format(ugettext_lazy('Squads'), ugettext_lazy('Overview'))
    r.write(pdf)
    return r


class SquadCreateView(generic.CreateView):

    model = Squad
    fields = ['name']
    template_name = 'gymnastics/squads/new.html'
    success_url = reverse_lazy('squads.index')


class SquadUpdateView(generic.UpdateView):

    model = Squad
    fields = ['name']
    template_name = 'gymnastics/squads/edit.html'

    def get_success_url(self):
        return reverse('squads.detail', kwargs = { 'id' : self.kwargs['pk'] })


class SquadDeleteView(generic.DeleteView):

    model = Squad
    template_name = 'gymnastics/squads/delete.html'
    success_url = reverse_lazy('squads.index')
