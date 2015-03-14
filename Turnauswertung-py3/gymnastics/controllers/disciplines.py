from django.shortcuts import render

from gymnastics.models.discipline import Discipline

def index(request):
    context = { 'disciplines': Discipline.objects.all() }
    return render(request, 'gymnastics/disciplines/index.html', context)
