from django.shortcuts import render

# Create your views here.
def index(request):
    template = 'mainpage/index.html'
    return render(request, template)

def googlecheck(request):
    return render(request, 'mainpage/googlecheck.html')