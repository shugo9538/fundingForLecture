from django.shortcuts import render

# Create your views here.
def all(request):
    return render(request, 'lecturelist/entirelist.html')

def opening(request):
    return render(request, 'lecturelist/openlist.html')

def funding(request):
    return render(request, 'lecturelist/fundinglist.html')
