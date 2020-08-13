from django.urls import path
from . import views

urlpatterns = [
    # users path
    path('', views.Login.as_view, name='login'),
    path('google/', views.google, name='google'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.logout, name='logout'),
    path('join/', views.join, name='join'),
    path('join/article/', views.article, name='article'),
    path('join/student/', views.student, name='student'),
    path('join/lecturer', views.lecturer, name='lecturer'),
]
