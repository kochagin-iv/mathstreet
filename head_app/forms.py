from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import QuestionVPR


class NameForm(forms.Form):
    surname = forms.CharField(label='Ваша фамилия', max_length=100)
    name = forms.CharField(label='Ваше имя', max_length=100)


class QuestVprForm(ModelForm):
    class Meta:
        model = QuestionVPR
        fields = ['num_ex', 'description', 'corr_ans']


class TestVprFrom(forms.Form):
    name = forms.CharField(label='Название теста ВПР')
    description = forms.CharField(widget=forms.Textarea, label='Описание теста ВПР')
    time = forms.IntegerField(label='Время на выполнение теста ВПР в минутах', initial=1)


class FormAnswer(forms.Form):
    #форма ответа на вопрос работы
    ans = forms.CharField(label='Ваш ответ', max_length=100, required=False)
    #file = forms.FileField(label='Файл - ответ на задание(при необходимости)', required=False)


class StudentsWorksForm(ModelForm):
    file = forms.FileField(label='', widget=forms.FileInput, required=False)

    class Meta:
        model = StudentsWorks
        fields = ('name', 'description', 'file')


class testform(forms.Form):
    ans = forms.CharField(label='Ваш ответ', max_length=100, required=False)


class ExAnsForm(ModelForm):
    file = forms.FileField(label='', widget=forms.FileInput, required=False)

    class Meta:
        model = AnsEx
        fields = ('description', 'file', 'ex_id')


class KrForm(ModelForm):
    class Meta:
        model = KR
        fields = ('name', 'description', 'time', 'visible')


class KrQForm(ModelForm):
    class Meta:
        model = ExKR
        fields = ('description', 'corr_ans', 'file', 'points')


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ('title', 'short_text', 'text', 'file', 'visible_for_all')


class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ('text_info1', 'text_info2', 'file')


