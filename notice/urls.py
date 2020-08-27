from django.urls import path
from . import views

urlpatterns = [
    path('system/', views.system, name='system_notice'),
    path('lecture/', views.lecture, name='lecture_notice'),
]
