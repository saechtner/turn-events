from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseNotAllowed
from django.views import generic

from gymnastics.models.athlete import Athlete


def index(request):
    context = { 'athletes': Athlete.objects.all() }
    return render(request, 'gymnastics/athletes/index.html', context)

def results(request):
    context = { 'athletes': Athlete.objects.all() }
    return render(request, 'gymnastics/athletes/results.html', context)

def edit2(request, pk):
    if request.method == 'GET':
        try:
            context = {'athlete': Athlete.objects.get(id=pk)}
        except:
            # TODO
            print('!!!!!!!!!!!!!!!!!!!!!!')
            pass

        # print(context)
        # print(context['athlete'])
        # print(dir(context['athlete']))
        # print(Athlete)
        # print(dir(Athlete))

        return render(request, 'gymnastics/athletes/edit2.html', context)
    elif request.method == 'POST':
        # print(request.POST)
        # print(type(request.POST))

        # verify all request.POST fields in athlete and set them if they changed
        # OR 
        # set all athlete fields to the corresponding request.POST values
        # then try saving it
        # use verifier on the athlete model to raise proper exceptions if values are shit
        # catch these exceptions here (maybe use custom clasa)
        # put error messages together and render them

        athlete = Athlete.objects.get(id=pk)

        # assign all request.POST values to the corresponding athlete field
        for key, value in request.POST.items():
            if hasattr(athlete, key):
                setattr(athlete, key, value)

        # validate athlete - calls clean_fields, clean and validate_unique
        # athlete.full_clean()

        #simple test
        # athlete.first_name = request.POST['first_name']

        try:
            athlete.save()
            # render success
        except Exception as e:
            # set error messages (eine error message mit allen exceptions or vice versa)
            # add errors to context
            return render(request, 'gymnastics/athletes/edit2.html', context)

        # render success
        context = {'object': athlete}
        return render(request, 'gymnastics/athletes/detail.html', context)
      
    #http 405! 404?
    return  HttpResponseNotAllowed(['GET', 'POST'])
    # ToDO: add 405.http basic template
    # return  HttpResponseNotAllowed(['PUT'])




class AthleteCreateView(generic.CreateView):

    model = Athlete
    fields = ['first_name', 'last_name', 'sex', 'year_of_birth', 'club', 'squad', 'stream', 'team']
    template_name = 'gymnastics/athletes/new.html'
    success_url = reverse_lazy('athletes.index')


class AthleteDetailView(generic.DetailView):

    model = Athlete
    template_name = 'gymnastics/athletes/detail.html'


class AthleteUpdateView(generic.UpdateView):

    model = Athlete
    fields = ['first_name', 'last_name', 'sex', 'year_of_birth', 'club', 'squad', 'stream', 'team']
    template_name = 'gymnastics/athletes/edit.html'

    def get_success_url(self):
        some_kwargs = self.kwargs
        return reverse('athletes.detail', kwargs = { 'pk' : self.kwargs['pk'] })


class AthleteDeleteView(generic.DeleteView):

    model = Athlete
    template_name = 'gymnastics/athletes/delete.html'
    success_url = reverse_lazy('athletes.index')
