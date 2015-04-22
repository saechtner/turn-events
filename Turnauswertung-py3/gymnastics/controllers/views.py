from django.shortcuts import render

# renders index / home page
def index(request):
    return render(request, 'gymnastics/index.html', None)

# renders todo page
def process(request):
    return render(request, 'gymnastics/process.html', None)
