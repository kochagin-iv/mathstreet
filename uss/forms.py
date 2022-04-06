from django import forms
from django.forms import ModelForm
from .models import *
from .views import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


'''class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']'''


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    last_name = forms.CharField(label='Фамилия', required=False)
    first_name = forms.CharField(label='Имя', required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'last_name', 'first_name',)


class NewGroupForm(forms.Form):
    name = forms.CharField(label='Название новой группы')


class ChangeGroupName(forms.Form):
    name = forms.CharField(label='Название группы',
                           required=False,
                           widget=forms.TextInput(attrs={'placeholder': 'Если хотите изменить название группы, '
                                                                        'введите в это поле новое название и нажмите Сохранить'}))