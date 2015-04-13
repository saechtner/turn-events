import re

from django.shortcuts import redirect, render
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic

from django.db.models import Sum

from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from subprocess import Popen, PIPE
import tempfile



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
    stream_athletes_disciplines = { stream.id: {'athletes': [], 'disciplines': stream.discipline_set.all()} for stream in streams_distinct }
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
    stream_athletes_disciplines = { stream.id: {'athletes': [], 'disciplines': stream.discipline_set.all()} for stream in streams_distinct }
    discipline_list = []

    for athlete in athletes:
        stream_athletes_disciplines[athlete.stream.id]['athletes'].append(athlete)

    ### Tabindex ###
    for stream in streams_distinct:
        discipline_list.extend(stream_athletes_disciplines[stream.id]['disciplines'])

    x = 1
    discipline_tabindex_dict = {}
    for discipline in set(discipline_list):
        discipline_tabindex_dict[discipline] = x
        x += 1

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
        'discipline_tabindex_dict': discipline_tabindex_dict
    }

    return render(request, 'gymnastics/squads/enter_performances.html', context)

def handle_entered_performances(request):
    performanceDict = request.POST

    athletes = Athlete.objects.all()
    disciplines = Discipline.objects.all()
    performances = Performance.objects.all()

    for key, value in performanceDict.items():
        if '-' in key and value:
            athleteID, performanceID = re.split(r'-+', key.rstrip())

            athlete = athletes.get(id=athleteID)
            discipline = disciplines.get(id=performanceID)

            try:
                performance = performances.get(athlete=athlete,discipline=discipline)
                performance.value = value
            except:
                performance = Performance( \
                    value=value,
                    athlete=athlete,
                    discipline=discipline
                )

            performance.save()

    return redirect(reverse('squads.index'))

def judge_pdf(request):
    squads = Squad.objects.all().prefetch_related('athlete_set')
    squad_disciplines = {}
    for squad in squads:
        squad_disciplines[squad.id] = []
        athletes = squad.athlete_set.all().select_related('stream')
        for athlete in athletes:
            squad_disciplines[squad.id].extend([ discipline for discipline in athlete.stream.discipline_set.all() ])
        squad_disciplines[squad.id] = set(squad_disciplines[squad.id])

    context = Context({
            'squads': squads,
            'squad_disciplines': squad_disciplines,
        })

    template = get_template('gymnastics/squads/squads_judges.tex')
    rendered_tpl = template.render(context).encode('utf-8')

    import os
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
    # r['Content-Disposition'] = 'attachment; filename={0}_{1}_{2}.pdf'.format(_('Squads'), _('Judge'), _('Lists'))
    r['Content-Disposition'] = 'filename={0}_{1}_{2}.pdf'.format(_('Squads'), _('Judge'), _('Lists'))
    r.write(pdf)
    return r

def overview_pdf(request):
    squads = Squad.objects.all().prefetch_related('athlete_set').select_related('athlete_set__club')

    context = Context({
            'squads': squads,
        })

    template = get_template('gymnastics/squads/squads_athletes.tex')
    rendered_tpl = template.render(context).encode('utf-8')

    import os
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
    # r['Content-Disposition'] = 'attachment; filename={0}_{1}.pdf'.format(_('Squads'), _('Overview'))
    r['Content-Disposition'] = 'filename={0}_{1}.pdf'.format(_('Squads'), _('Overview'))
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
        some_kwargs = self.kwargs
        return reverse('squads.detail', kwargs = { 'pk' : self.kwargs['pk'] })


class SquadDeleteView(generic.DeleteView):

    model = Squad
    template_name = 'gymnastics/squads/delete.html'
    success_url = reverse_lazy('squads.index')