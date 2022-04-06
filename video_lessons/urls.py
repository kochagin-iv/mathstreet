"""uss URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
import video_lessons.views as videoviews
from django.contrib.auth import views as auth_views
from .forms import *
from django.conf.urls import include, url


urlpatterns = [
    path('video_lessons/', videoviews.all_video_lessons, name='all_video_lessons'),
    path('add_video_lesson/', videoviews.add_video_lesson, name='add_video_lesson'),
    path('edit_video_lesson/<int:pk>/', videoviews.edit_video_lesson, name='edit_video_lesson'),
    path('video_lessons/<int:key>', videoviews.view_lesson, name='view_lesson'),
    path('video_lessons/<int:num_class>/<str:subj>', videoviews.video_programm_class, name='video_programm_class'),
]