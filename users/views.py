from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from social_core.exceptions import AuthAlreadyAssociated
# from .models import UserInfo #Mongo로 바꿀 예정
from django.views.generic import View, RedirectView, CreateView
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import reverse


from .models import MongoConnection

from mainpage import urls

# Create your views here.her
userInfo = MongoConnection()

# 회원가입 버튼 동작 클래스로 바꿔야겠네
def join(request):
    return render(request, 'users/join.html')

def article(request):
    return render(request, 'users/article.html')

def enrollment(request):
    return render(request, 'users/enrollment.html')

def create(request):
    print(request.POST['chkbox'])
    if request.POST['chkbox'] == True:
        userType = 'student'
        pm = None
        career = None
    else:
        userType = 'teacher'
        pm = request.POST.get('textarea1')
        career = request.POST.get('textarea2')

    createInfo = {
        'id': request.POST['id'],
        'nickname': request.POST['mbname'],
        'pw': request.POST['mbpw1'],
        'Email': request.POST['email'],
        'type': userType,
        'pm': pm,
        'career': career,
    }
    userInfo.createUser(createInfo)

    return redirect(reverse('index'))

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

        errorMsg = '로그인에 실패했습니다. 아이디와 비밀번호를 확인해주세요'

        userInfo.set(user_id)
        responseInfo = userInfo.userCheck()

        request.session['failed'] = None

        # 읽어온 사용자 정보와 일치하는지 확인
        if responseInfo is not None:
            if user_id == responseInfo['id'] and user_pw == responseInfo['pw']:
                request.session['name'] = responseInfo['nickname']
            else:
                request.session['failed'] = errorMsg
                return redirect(reverse('login'))
        else:
            request.session['failed'] = errorMsg
            return redirect(reverse('login'))

        return redirect(reverse('index'))

# 로그인 후 로그아웃 버튼 클릭시
class Logout(LogoutView):
    def get(self, requests):
        response = render(requests)
        response.delete_cookie('name')
        return redirect(reverse('index'))



