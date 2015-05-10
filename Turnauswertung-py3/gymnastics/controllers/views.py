from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render

# renders index / home page
def index(request):
    return redirect(reverse('tournaments.main'))

# renders todo page
def process(request):
    return render(request, 'gymnastics/process.html', None)
