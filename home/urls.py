from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # 메인 화면
]