from django.shortcuts import render

# Create your views here.
def edit(request):
    return render(request, 'mypage/correction.html')

def withdrawal(request):
    return render(request, 'mypage/withdrawal.html')

def lecturefunding(request):
    return render(request, 'mypage/lecturefunding.html')

def student(request):
    return render(request, 'mypage/student.html')

def teacher(request):
    return render(request, 'mypage/teacher.html')