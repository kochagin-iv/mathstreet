from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.clickjacking import xframe_options_exempt, xframe_options_sameorigin
from django.views.decorators.csrf import csrf_exempt
from uss.models import *
from head_app.forms import *
from head_app.models import *
from head_app.views import check_super
from django.db.models import Q
from random import randint
from django.contrib import messages
from math import ceil
from django.views.generic import ListView, View

from video_lessons.forms import VideoLessonForm
from video_lessons.models import *


@xframe_options_sameorigin
def all_video_lessons(request):
    context = {'videos': VideoLesson.objects.all().order_by('-id')}
    return render(request, 'all_video_lessons.html', context)


@login_required(login_url='/login')
def add_video_lesson(request):
    check_super(request)
    context = {}
    if request.method == 'POST':
        form = VideoLessonForm(request.POST, request.FILES)
        arr_classes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
        if form.is_valid():
            lesson = VideoLesson(name=form.cleaned_data['name'],
                                 link=form.cleaned_data['link'],
                                 annotation_file=form.cleaned_data['annotation_file'])
            for num in arr_classes:
                if num in request.POST:
                    lesson.num_class += num + ';'
            if 'alg' in request.POST:
                lesson.tag_subj = 'alg'
                lesson.subj = 'Алгебра'
            if 'geo' in request.POST:
                lesson.tag_subj = 'geo'
                lesson.subj = 'Геометрия'
            lesson.save()
            messages.success(request, 'Видеоурок успешно добавлен!')
            return redirect('/video_lessons/')
    context['form'] = VideoLessonForm()
    return render(request, 'add_video_lesson.html', context)


@login_required(login_url='/login')
def edit_video_lesson(request, pk):
    check_super(request)
    context = {}
    video = VideoLesson.objects.get(id=pk)
    if request.method == 'POST':
        form = VideoLessonForm(request.POST, request.FILES, instance=video)
        if form.is_valid():
            form.save()
            messages.success(request, 'Видео ' + video.name + ' успешно изменено!')
            return redirect('/video_lessons/')
    context['video'] = video
    context['form'] = VideoLessonForm(instance=video)
    return render(request, 'edit_video_lesson.html', context)


@login_required(login_url='/login')
def view_lesson(request, key):
    check_super(request)
    lesson = VideoLesson.objects.get(id=key)
    context = {'lesson': lesson}
    context['subj'] = lesson.subj
    context['class'] = lesson.num_class
    context['class'] = context['class'].replace(';', '')
    return render(request, 'view_video_lesson.html', context)
    # return render(request, '../video_lessons/templates/edit_video_lesson.html', context)


def video_programm_class(request, num_class, subj):
    context = {}
    context['videos'] = []
    context['class'] = num_class
    context['subj'] = 'Алгебра' if subj == 'alg' else 'Геометрия'
    arr_videos = VideoLesson.objects.filter(tag_subj=subj)
    for video in arr_videos:
        if str(num_class) + ';' in video.num_class:
            context['videos'].append(video)
    return render(request, 'video_programm_class.html', context)
