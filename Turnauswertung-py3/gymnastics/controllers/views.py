from django.shortcuts import render

# renders index / home page
def index(request):
    return render(request, 'gymnastics/index.html', None)

