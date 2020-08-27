from django.shortcuts import render

# Create your views here.
def system(request):
    return render(request, 'notice/systemnotice.html')

def lecture(request):
    return render(request, 'notice/lecturenotice.html')