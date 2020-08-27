from django.urls import path
from . import views

urlpatterns = [
    # users path
    path('edit', views.edit, name='edit'),
    path('withdrawal', views.withdrawal, name='withdrawal'),
    path('lecturefunding', views.lecturefunding, name='lecturefunding'),
    path('student', views.student, name='student'),
    path('teacher', views.teacher, name='teacher'),
]
