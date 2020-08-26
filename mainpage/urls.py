from django.urls import path
from . import views

urlpatterns = [
    # users path
    path('', views.index, name='index'),
    path('/google9133cf5bbea3d62c.html', views.googlecheck, name='google')
]
