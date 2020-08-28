from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    # users path
    # 회원가입
    path('join/', views.join, name='join'),
    path('join/article/', views.article, name='article'),
    path('join/enrollment/', views.enrollment, name='enrollment'),
    path('join/enrollment/create', views.create, name='create'),

    # 로그인 창
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),

    # path('join/article/google', views.Login.as_view(), name='how'),
    # path('join/article/inner', views.Login.as_view(), name='how'),

    # using postman api checking
    # path('login/', csrf_exempt(views.Login.as_view()), name='login'),
]
