from django.urls import path
from . import views

urlpatterns = [
    # users path
    path('', views.users, name='users'),
    path('google/', views.google, name='google'),
    path('login/', views.Login.as_view(), name='login'),
    # path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('join/', views.Login.as_view(), name='join'),
    path('join/article/', views.join, name='article'),
    path('join/student/', views.Login.as_view(), name='student'),
    path('join/lecturer/', views.Login.as_view(), name='lecturer'),
]
