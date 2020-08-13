from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from social_core.exceptions import AuthAlreadyAssociated
from .models import UserInfo #Mongo로 바꿀 예정
from django.views.generic import View
import requests


# Create your views here.her
def google(request):
    return render(request, 'users/google.html')


def auth_allowed(backend, uid, user=None, *args, **kwargs):
    print("backend >>", backend)
    print("uid >>", uid)
    print("user >>", user)
    print("args >>", args)
    print("kwargs >>", kwargs)

    return HttpResponse("로그인 성공")


# def users(request):
#     return render(request, 'users/users.html')


class Login(View):
  def get(self, request):
      return render(request, 'users/users.html')

  def post(self, request):
      id=request.POST.get('id')
      pw=request.POST.get('password')
      msg=False

      if id=="one" and pw==123:
          msg=True
      msg = "one"

      context={
          'msg': msg,
      }

      return render(requests, 'users/article.html', context)

# def login(request):
#     return HttpResponse("Login Test")


def logout(request):
    return HttpResponse("Logout Test")


def join(request):
    return HttpResponse("Join Test")


def article(request):
    return HttpResponse("Article Test")


def student(request):
    return HttpResponse("student Test")


def lecturer(request):
    return HttpResponse("Lecturer Test")