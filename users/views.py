from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from social_core.exceptions import AuthAlreadyAssociated
# from .models import UserInfo #Mongo로 바꿀 예정
from django.views.generic import View
from django.template import loader
from .models import MongoConnection
import json


# Create your views here.her

# 유저 로그인 창
def users(request):
    return render(request, 'users/users.html')

# 회원가입 버튼 동작
def join(request):
        return render(request, 'users/article.html')

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
class Login(View):
    def post(self, request):
        # 로그인 버튼 클릭시 폼(아이디, 패스워드)에서 데이터를 읽어옴
        user_id = request.POST['id']
        user_pw = request.POST['password']

        # 사용자 정보를 MongoDB 데이터와 비교
        userInfo = MongoConnection()
        userInfo.set(user_id)
        responseInfo = userInfo.user_check()
        del responseInfo['_id']
        print(responseInfo)

        msg=False

        # 읽어온 사용자 정보와 일치하는지 확인
        if user_id==responseInfo['id'] and user_pw==responseInfo['pw']:
            msg = True
            name = responseInfo['Email']

        # mainpage.html에 전달할 인자값들
        context = {
            'msg': msg,
            'name': name # Email을 전달해 페이지에서 나타나게함
        }

        return render(request, 'users/mainpage.html', context)

# 로그인 후 로그아웃 버튼 클릭시
def logout(request):
    return HttpResponse("Logout Test")



