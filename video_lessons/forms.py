from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class VideoLessonForm(ModelForm):
    class Meta:
        model = VideoLesson
        fields = ('name', 'link', 'annotation_file')
