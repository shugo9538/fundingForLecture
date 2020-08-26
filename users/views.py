from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from social_core.exceptions import AuthAlreadyAssociated
# from .models import UserInfo #Mongo로 바꿀 예정
from django.views.generic import View, RedirectView
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import reverse

from .models import MongoConnection

from mainpage import urls

# Create your views here.her

# 유저 로그인 창
def users(request):
    return render(request, 'users/users.html')

# 회원가입 버튼 동작 클래스로 바꿔야겠네
def join(request):
    return render(request, 'users/join.html')

def article(request):
    return render(request, 'users/article.html')

def enrollment(request):
    return render(request, 'users/enrollment.html')

# 구글 계정 연동 추가 중
def google(request):
    return render(request, 'users/google.html')

def auth_allowed(backend, uid, user=None, *args, **kwargs):
    print("backend >>", backend)
    print("uid >>", uid)
    print("user >>", user)
    print("args >>", args)
    print("kwargs >>", kwargs)

    return HttpResponse("로그인 성공")

# 로그인 버튼 누르는 경우 동작
class Login(LoginView):
    def get(self, request):
        return render(request, 'users/login.html')

    def post(self, request):
        # 로그인 버튼 클릭시 폼(아이디, 패스워드)에서 데이터를 읽어옴
        user_id = request.POST['id']
        user_pw = request.POST['password']

        # 사용자 정보를 MongoDB 데이터와 비교
        userInfo = MongoConnection()
        userInfo.set(user_id)

        errorMsg = '로그인에 실패했습니다. 아이디와 비밀번호를 확인해주세요'
        # responseInfo = None

        # if userInfo.user_check() is errorMsg:
        #     request.session['failed'] = '로그인에 실패했습니다. 아이디와 비밀번호를 확인해주세요'
        # else:
        #     responseInfo = userInfo.user_check()
        #     del responseInfo['_id']

        responseInfo = userInfo.user_check()
        request.session['failed'] = None

        # 읽어온 사용자 정보와 일치하는지 확인
        if user_id == responseInfo['id'] and user_pw == responseInfo['pw']:
            request.session['name'] = responseInfo['id']
            request.session['failed'] = 'not failed'
        else:
            request.session['failed'] = errorMsg

        return redirect(reverse('index'))

# 로그인 후 로그아웃 버튼 클릭시
class Logout(LogoutView):
    def get(self, requests):
        response = render(requests)
        response.delete_cookie('name')
        return redirect(reverse('index'))



