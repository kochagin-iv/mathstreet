from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from uss.models import *
from .forms import *
from .models import *
from django.db.models import Q
from random import randint
from django.contrib import messages
from math import ceil
from django.views.generic import ListView, View


# Create your views here.


def check_super(request):
    if request.user.is_authenticated and request.user.is_superuser:
        pass
    return redirect('/')


def handler404(request, exception):
    return render(request, '404.html')


def handler500(request):
    return render(request, '404.html')


def home(request):
    context = {}
    context['q'] = QuestionVPR.objects.all()
    context['last_news'] = News.objects.all().order_by('-id')
    context['last_photos'] = Photo.objects.all().order_by('-id')[:5]
    context['last_works'] = StudentsWorks.objects.all().order_by('-id')[:5]
    if len(context['last_news']) > 5:
        context['last_news'] = context['last_news'][:5]
    if len(context['last_photos']) > 5:
        context['last_photos'] = context['last_photos'][:5]
    if len(context['last_works']) > 5:
        context['last_works'] = context['last_works'][:5]
    # print(len(QuestionVPR.objects.all()))
    context['works'] = []
    context['test_vprs'] = []
    if request.user.is_authenticated:
        us = request.user
        context['my_user'] = us
        mas_groups = us.profile.group_ids.split(';')
        for i in mas_groups:
            if i != '':
                num = int(i)
                for j in KR.objects.all():
                    if (';' + str(num) + ';') in j.groups and not (';' + (str(request.user.id) + ';') in j.done) and j.visible:
                        dic = {}
                        dic['work'] = j
                        if j.time % 10 >= 5 or j.time % 10 == 0:
                            dic['word_minut'] = 'минут'
                        if j.time % 10 == 2 or j.time % 10 == 3 or j.time == 4:
                            dic['word_minut'] = 'минуты'
                        if j.time % 10 == 1:
                            dic['word_minut'] = 'минута'
                        context['works'].append(dic)

                for j in TestVPR.objects.all():
                    if (';' + str(num) + ';') in j.groups and not (';' + (str(request.user.id) + ';') in j.done):
                        dic = {}
                        dic['work'] = j
                        if j.time % 10 >= 5 or j.time % 10 == 0:
                            dic['word_minut'] = 'минут'
                        if j.time % 10 == 2 or j.time % 10 == 3 or j.time == 4:
                            dic['word_minut'] = 'минуты'
                        if j.time % 10 == 1:
                            dic['word_minut'] = 'минута'
                        context['test_vprs'].append(dic)
    return render(request, 'home.html', context)


def about(request):
    context = {}
    return render(request, 'about.html', context)


@login_required(login_url='/login')
def add_vpr(request):
    check_super(request)
    context = {}
    if request.method == 'POST':
        # print(111111)
        form = QuestVprForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вопрос успешно добавлен!')
            return redirect('/')
        messages.error(request, 'Что-то пошло не так...')
    else:
        form = QuestVprForm()
        context['form'] = form
    return render(request, 'add_vpr.html', context)


@login_required(login_url='/login')
def edit_vpr(request, pk):
    check_super(request)
    context = {}
    item = get_object_or_404(QuestionVPR, id=pk)
    form = QuestVprForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        messages.success(request, 'Вопрос успешно изменен!')
        return redirect('/')
    context['form'] = form
    return render(request, 'edit_vpr.html', context)


@login_required(login_url='/login')
def add_test_vpr(request):
    check_super(request)
    context = {}
    context['groups'] = []
    for i in Group.objects.all():
        dic = {}
        dic['name'] = i.name
        dic['idd'] = 'Group' + str(i.id)
        context['groups'].append(dic)
    if request.method == 'POST':
        # print(111111)
        form = TestVprFrom(request.POST)
        if form.is_valid():

            # i вида Group***
            e = TestVPR(name=form.cleaned_data['name'],
                        description=form.cleaned_data['description'],
                        time=form.cleaned_data['time'])

            for i in request.POST:
                if 'Group' in i:
                    num = int(i.replace('Group', ''))
                    e.groups += str(num)
                    e.groups += ';'
            e.save()
            messages.success(request, 'Тест успешно добавлен!')
            return redirect('/')
    else:
        form = TestVprFrom()
        context['form'] = form
    return render(request, 'add_vpr_test.html', context)


@login_required(login_url='/login')
def all_tests(request):
    check_super(request)
    context = {}
    context['s_user'] = (request.user.is_superuser)
    if request.method == 'POST':
        if request.user.is_superuser:
            pk = int(dict(request.POST)['pk'][0])
            AnswerVPR.objects.filter(test_id=pk).delete()
            TestVPR.objects.filter(id=pk).delete()
            messages.success(request, 'Тест успешно удален!')
        else:
            return redirect('/')
    context['tests'] = []
    for i in TestVPR.objects.all():
        kol = i.done.count(';')
        context['tests'].append({'test': i, 'test_id': i.id,
                                 'kol_already': kol})
    context['tests'].reverse()
    return render(request, 'all_testsVPR.html', context)


@login_required(login_url='/login')
def test_fio(request, pk):
    context = {}
    test = TestVPR.objects.get(id=pk)
    context['test'] = test
    context['word_minut'] = ''
    if test.time % 10 >= 5 or test.time % 10 == 0:
        context['word_minut'] = 'минут'
    if test.time % 10 == 2 or test.time % 10 == 3 or test.time == 4:
        context['word_minut'] = 'минуты'
    if test.time % 10 == 1:
        context['word_minut'] = 'минута'
    if request.method == 'POST':
        if (str(request.user.id) + ';') in test.done:
            messages.warning(request, 'Выполнить тест можно только 1 раз!')
            return redirect('/')
        nums_ex = []
        for item in QuestionVPR.objects.all():
            if item.num_ex not in nums_ex:
                nums_ex.append(item.num_ex)
        for i in nums_ex:
            f = QuestionVPR.objects.filter(num_ex=i)
            e = f[randint(0, len(f) - 1)]
            ans = AnswerVPR()
            ans.us_id = request.user.id
            ans.test_id = pk
            ans.q_id = e.id
            ans.save()
        st_t_vpr = TestVPR_Student()
        st_t_vpr.us_id = request.user.id
        st_t_vpr.test_id = pk
        st_t_vpr.save()
        st = '/' + 'test/' + str(st_t_vpr.id)
        messages.success(request, 'Теперь вы можете приступить к работе!')
        return redirect(st)
    return render(request, 'test_fio.html', context)


@login_required(login_url='/login')
def do_test(request, pk):
    context = {}
    tt = TestVPR_Student.objects.get(id=pk)
    us_id = tt.us_id
    t_id = tt.test_id
    answ = AnswerVPR.objects.filter(us_id=us_id, test_id=t_id)
    tst = TestVPR.objects.get(id=t_id)
    if request.method != 'POST' and (str(request.user.id) + ';') in tst.done:
        messages.warning(request, 'Выполнить тест можно только 1 раз!')
        return redirect('/')

    quests = []
    kol = 1
    context['time'] = str(TestVPR.objects.get(id=t_id).time)
    for i in answ:
        quests.append({'qst': QuestionVPR.objects.get(id=i.q_id),
                       'kol': kol,
                       'form': FormAnswer})
        kol += 1
    context['quests'] = quests
    # print(quests[0][1])
    if request.method == 'POST':
        form = dict(request.POST)
        form = form['ans']
        for i in range(len(form)):
            answ[i].ans = form[i]
            if str(answ[i].ans) == str(QuestionVPR.objects.get(id=answ[i].q_id).corr_ans):
                answ[i].is_corr = 1
            answ[i].save()
        st = '/results_testvpr/' + str(pk)
        messages.info(request, 'Тест завершен, посмотрите результаты.')
        return redirect(st)
    tst.done += (str(request.user.id) + ';')
    tst.save()
    return render(request, 'do_test.html', context)


def res_t_vpr_st(request, pk):
    context = {}
    tt = TestVPR_Student.objects.get(id=pk)
    us_id = tt.us_id
    t_id = tt.test_id
    answ = AnswerVPR.objects.filter(us_id=us_id, test_id=t_id)
    kol_corr = 0
    for i in answ:
        if i.is_corr:
            kol_corr += 1
    context['kol_corr'] = kol_corr
    context['kol_q'] = len(answ)
    quests = []
    kol = 0
    for i in answ:
        quests.append({'qst': QuestionVPR.objects.get(id=i.q_id),
                       'kol': kol + 1,
                       'my_ans': i.ans,
                       'corr_ans': QuestionVPR.objects.get(id=i.q_id).corr_ans})
        kol += 1
    context['quests'] = quests
    return render(request, 'res_vpr_test.html', context)


@login_required(login_url='/login')
def all_q_vpr(request):
    check_super(request)
    context = {}
    context['num_v'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    return render(request, 'all_q_vpr.html', context)


@login_required(login_url='/login')
def view_vpr_num(request, pk):
    check_super(request)
    context = {}
    context['q'] = QuestionVPR.objects.filter(num_ex=pk)
    # print(len(QuestionVPR.objects.all()))
    context['num'] = pk
    return render(request, 'view_num_vpr.html', context)


def cmp(input):
    return input['res']


@login_required(login_url='/login')
def view_all_test_res_vpr(request, pk):
    check_super(request)
    context = {}
    test = TestVPR.objects.get(id=pk)
    context['test'] = test
    context['kol_already'] = test.done.count(';')
    context['all_res'] = []
    s = test.done.split(';')
    for i in s:
        if i != '':
            us = User.objects.filter(id=int(i))
            nm = request.user.first_name
            sr = request.user.last_name
            context['all_res'].append({'nm': nm,
                                       'res': len(AnswerVPR.objects.filter(us_id=request.user.id,
                                                                           test_id=pk,
                                                                           is_corr=1)),
                                       'kol': len(AnswerVPR.objects.filter(us_id=request.user.id,
                                                                           test_id=pk)),
                                       'sr': sr,
                                       't_id': TestVPR_Student.objects.get(us_id=request.user.id,
                                                                           test_id=pk).id})
    context['all_res'].sort(key=cmp)
    print(context['all_res'])
    return render(request, 'view_all_st_test_res_vpr.html', context)


@login_required(login_url='/login')
def test_view_res_tch(request, pk):
    check_super(request)
    tt = TestVPR_Student.objects.get(id=pk)
    us_id = request.user.id
    nm = request.user.first_name
    sr = request.user.last_name
    t_id = tt.test_id
    context = {}
    answ = AnswerVPR.objects.filter(us_id=us_id, test_id=t_id)
    kol_corr = 0
    for i in answ:
        if i.is_corr:
            kol_corr += 1
    context['kol_corr'] = kol_corr
    context['kol_q'] = len(answ)
    quests = []
    kol = 0
    for i in answ:
        quests.append({'qst': QuestionVPR.objects.get(id=i.q_id),
                       'kol': kol + 1,
                       'my_ans': i.ans,
                       'corr_ans': QuestionVPR.objects.get(id=i.q_id).corr_ans,
                       'ans': AnswerVPR.objects.get(q_id=i.q_id,
                                                    us_id=us_id,
                                                    test_id=t_id)})
        kol += 1
    context['quests'] = quests
    context['nm'] = nm
    context['sr'] = sr
    if request.method == 'POST':
        a = dict(request.POST)
        for i in a:
            if 'csrf' not in i:
                ansvp = AnswerVPR.objects.get(id=int(i))
                print(ansvp.ans)
                ansvp.is_corr = (1 + ansvp.is_corr) % 2
                ansvp.save()
                st = '/test_view_res/' + str(pk)
                messages.success(request, 'Результат ответа успешно изменен!')
                return redirect(st)
    return render(request, 'view_st_res_test_vpr.html', context)


@login_required(login_url='/login')
def add_st_work(request):
    check_super(request)
    if request.method == 'POST':
        form = StudentsWorksForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Работа успешно добавлена!')
            return redirect('/')
    context = {}
    context['form'] = StudentsWorksForm()
    return render(request, 'add_st_work.html', context)


@login_required(login_url='/login')
def edit_st_work(request, pk):
    check_super(request)
    context = {}
    item = StudentsWorks.objects.get(id=pk)
    if request.method == 'POST':
        form = StudentsWorksForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Работа успешно изменена!')
            return redirect('/')
    context['item'] = item
    context['form'] = StudentsWorksForm(instance=item)
    return render(request, 'edit_st_work.html', context)


@login_required(login_url='/')
def all_works(request):
    context = {}
    if request.method == 'POST':
        pk = int(dict(request.POST)['pk'][0])
        StudentsWorks.objects.filter(id=pk).delete()
        messages.success(request, 'Работа успешно удалена!')
    context['all_ex'] = []
    context['all_works'] = StudentsWorks.objects.all().order_by('-id')

    return render(request, 'all_st_works.html', context)


@login_required(login_url='/login')
def view_st_work(request, pk):
    context = {}
    item = StudentsWorks.objects.get(id=pk)
    context['work'] = item
    return render(request, 'view_st_work.html', context)


@login_required(login_url='/login')
def add_kr(request):
    check_super(request)

    context = {}
    if request.method == 'POST':
        print(request.POST)
        form = KrForm(request.POST)
        if form.is_valid():
            e = KR(name=form.cleaned_data['name'],
                   description=form.cleaned_data['description'],
                   time=form.cleaned_data['time'],
                   done=';',
                   groups=';')
            e.save()
            nm = 'Работа ' + e.name + ' успешно добавлена!'
            messages.success(request, nm)
            return redirect('/all_kr/')
    context['create_form'] = KrForm()
    return render(request, 'add_kr.html', context)


def all_kr(request):
    context = {}
    check_super(request)

    context['all_kr'] = KR.objects.all()
    if request.method == 'POST':
        KR.objects.filter(id=request.POST['pk']).delete()
        ExKR.objects.filter(kr_id=request.POST['pk']).delete()
        AnsExKR.objects.filter(kr_id=request.POST['pk']).delete()
        KrSt.objects.filter(kr_id=request.POST['pk']).delete()
        StatsKr.objects.filter(kr_id=request.POST['pk']).delete()
        messages.success(request, 'Работа успешно удалена!')
        return redirect('/all_kr')
    return render(request, 'all_kr.html', context)


@login_required(login_url='/login')
def edit_kr(request, pk):
    check_super(request)

    context = {}
    context['groups'] = []
    for i in Group.objects.all():
        dic = {}
        dic['name'] = i.name
        dic['idd'] = 'Group' + str(i.id)
        dic['status'] = 0

        if (str(i.id) + ';') in KR.objects.get(id=pk).groups:
            dic['status'] = 1
        context['groups'].append(dic)
    item = KR.objects.get(id=pk)
    context['kr'] = item
    context['ex'] = ExKR.objects.filter(kr_id=pk)
    context['len_ex'] = len(ExKR.objects.filter(kr_id=pk))
    # Копирование работы и связанных с ней заданий
    if request.method == 'POST' and 'copy' in request.POST:
        # print(request.POST)
        item = KR.objects.get(id=pk)
        last_id = item.id
        print(item.id)
        item.pk = None
        item.name = item.name + '_копия_' + str(len(KR.objects.filter(name__contains=item.name)))
        item.save()
        new_id = item.id
        for i in ExKR.objects.filter(kr_id=last_id):
            new_ex = ExKR()
            new_ex.kr_id = new_id
            new_ex.description = i.description
            new_ex.corr_ans = i.corr_ans
            new_ex.ans_file = i.ans_file
            new_ex.save()
        messages.success(request, 'Работа успешно скопирована!')
        return redirect('/all_kr')
    # Удаление задания из работы
    if request.method == 'POST' and 'pk' in request.POST:
        ExKR.objects.filter(id=request.POST['pk']).delete()
        AnsExKR.objects.filter(ex_id=request.POST['pk']).delete()

        messages.success(request, 'Задание успешно удалено!')
        return redirect('/edit_kr/' + str(pk))

    if request.method == 'POST':
        print(request.POST)

        form = KrForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            e = KR.objects.get(id=pk)
            e.groups = ''
            # i вида Group***
            for i in request.POST:
                if 'Group' in i:
                    num = int(i.replace('Group', ''))
                    e.groups += str(num)
                    e.groups += ';'
            e.save()
            messages.success(request, 'Работа успешно изменена!')
            return redirect('/all_kr')
    context['item'] = item
    context['form'] = KrForm(instance=item)
    return render(request, 'edit_kr.html', context)


@login_required(login_url='/')
def add_kr_ex(request, pk):
    check_super(request)
    context = {}
    if request.method == 'POST':
        # print(111111)
        # print(request.POST)
        form = KrQForm(request.POST, request.FILES)
        if form.is_valid():
            v = ExKR(description=form.cleaned_data['description'],
                     corr_ans=form.cleaned_data['corr_ans'],
                     kr_id=pk,
                     file=form.cleaned_data['file'],
                     points=form.cleaned_data['points'])
            if 'ans_file' in request.POST:
                v.ans_file = True
            if 'ans_text' in request.POST:
                v.ans_text = True
            v.save()
            messages.success(request, 'Задание успешно добавлено!')
            return redirect('/edit_kr/' + str(pk))
        messages.error(request, 'Что-то пошло не так...')
    else:
        form = KrQForm()
        context['form'] = form
    context['kr'] = KR.objects.get(id=pk)
    return render(request, 'add_q_kr.html', context)


@login_required(login_url='/login')
def edit_q_kr(request, pk, idd):
    check_super(request)

    context = {}
    kr = KR.objects.get(id=pk)
    item = ExKR.objects.get(id=idd)
    if request.method == 'POST':
        if 'ans_file' in request.POST:
            item.ans_file = True
            item.save()
        if 'ans_text' in request.POST:
            item.ans_text = True
            item.save()

        form = KrQForm(request.POST, request.FILES, instance=item)
        print(request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Задание успешно изменено!')
            return redirect('/edit_kr/' + str(pk))
    context['item'] = item
    context['form'] = KrQForm(instance=item)
    return render(request, 'edit_q_kr.html', context)


@login_required(login_url='/login')
def kr_fio(request, pk):
    context = {}
    kr = KR.objects.get(id=pk)
    context['kr'] = kr
    context['word_minut'] = ''
    if kr.time % 10 >= 5 or kr.time % 10 == 0:
        context['word_minut'] = 'минут'
    if kr.time % 10 == 2 or kr.time % 10 == 3 or kr.time == 4:
        context['word_minut'] = 'минуты'
    if kr.time % 10 == 1:
        context['word_minut'] = 'минута'
    if request.method == 'POST':
        if (';' + str(request.user.id) + ';') in kr.done:
            messages.warning(request, 'Выполнить работу можно только 1 раз!')
            return redirect('/')
        ex = []
        for item in ExKR.objects.filter(kr_id=pk):
            ex.append(item)
        for i in ex:
            ans = AnsExKR()
            ans.us_id = request.user.id
            ans.ex_id = i.id
            ans.kr_id = pk
            ans.number_ans = len(AnsExKR.objects.filter(us_id=request.user.id,
                                                        ex_id=i.id,
                                                        kr_id=pk)) + 1
            ans.save()

        kr_st = KrSt()
        kr_st.us_id = request.user.id
        kr_st.kr_id = pk
        kr_st.save()
        st = '/do_kr/' + str(kr_st.id)
        messages.success(request, 'Теперь вы можете приступить к работе!')
        return redirect(st)

    return render(request, 'kr_fio.html', context)


def get_max_num_ans_with_ex(user_id, kr_id, ex_id):
    ma = -1
    for i in AnsExKR.objects.filter(us_id=user_id, kr_id=kr_id, ex_id=ex_id):
        if i.number_ans > ma: ma = i.number_ans
    return ma


def get_max_num_ans_without_ex(user_id, kr_id):
    ma = -1
    for i in AnsExKR.objects.filter(us_id=user_id, kr_id=kr_id):
        if i.number_ans > ma: ma = i.number_ans
    return ma


@login_required(login_url='/login')
def do_kr(request, pk):
    context = {}
    kr_st = KrSt.objects.get(id=pk)
    kr = KR.objects.get(id=kr_st.kr_id)
    if request.method != 'POST' and (';' + str(request.user.id) + ';') in kr.done:
        messages.warning(request, 'Выполнить работу можно только 1 раз!')
        return redirect('/')

    quests = []
    kol = 1
    context['time'] = str(kr.time)
    answ = AnsExKR.objects.filter(us_id=request.user.id, kr_id=kr.id)
    for i in ExKR.objects.filter(kr_id=kr.id):
        # print('aaaa', i.file)
        quests.append({'qst': i,
                       'kol': kol,
                       'form': FormAnswer})
        kol += 1
    context['quests'] = quests
    if request.method == 'POST':
        print('req_POST', request.POST)
        # print(request.FILES)
        form = dict(request.POST)
        form = form['ans']
        print('form', form)
        num_ans = len(StatsKr.objects.filter(us_id=request.user.id,
                                             kr_id=kr.id)) + 1
        str_anss = ''
        pts = 0
        for j in range(len(form)):
            if len(AnsExKR.objects.filter(us_id=request.user.id,
                                          kr_id=kr.id,
                                          ex_id=answ[j].ex_id,
                                          number_ans=num_ans)) == 0:
                new_ans = AnsExKR(us_id=request.user.id,
                                  kr_id=kr.id,
                                  ex_id=answ[j].ex_id,
                                  number_ans=num_ans)
                new_ans.save()
            anss = AnsExKR.objects.get(us_id=request.user.id,
                                       kr_id=kr.id,
                                       ex_id=answ[j].ex_id,
                                       number_ans=num_ans)
            anss.ans = str(form[j])
            if str(form[j]) != '' and str(form[j]) == str(ExKR.objects.get(id=anss.ex_id).corr_ans):
                anss.is_corr = 1
                str_anss += '1'
                anss.points = ExKR.objects.get(id=anss.ex_id).points
                pts += ExKR.objects.get(id=anss.ex_id).points
            else:
                str_anss += '0'
                anss.points = 0
            str_anss += ';'
            anss.save()
        dic_req_files = dict(request.FILES)
        for i in dic_req_files:
            print(i, dic_req_files[i])  # i example view - f5ex54
            flag = 0
            ex_id = ''
            for symb in i:
                if symb == 'e':
                    flag = 1
                if flag:
                    ex_id += symb
            ex_id = int(ex_id[2:])
            print(ex_id)
            print('len', len(AnsExKR.objects.filter(us_id=request.user.id,
                                          kr_id=kr.id,
                                          ex_id=ex_id,
                                          number_ans=num_ans)))
            if len(AnsExKR.objects.filter(us_id=request.user.id,
                                          kr_id=kr.id,
                                          ex_id=ex_id,
                                          number_ans=num_ans)) == 0:
                new_ans = AnsExKR(us_id=request.user.id,
                                  kr_id=kr.id,
                                  ex_id=ex_id,
                                  number_ans=num_ans)
                new_ans.save()
            anss = AnsExKR.objects.get(us_id=request.user.id,
                                       kr_id=kr.id,
                                       ex_id=ex_id,
                                       number_ans=num_ans)
            print(anss.ans)
            print(dic_req_files[i])
            anss.file = dic_req_files[i][0]
            anss.save()
        stat_kr = StatsKr(us_id=request.user.id,
                          kr_id=kr.id,
                          us_num=num_ans,
                          kol_num=len(ExKR.objects.filter(kr_id=kr.id)),
                          kol_corr=len(AnsExKR.objects.filter(kr_id=kr.id,
                                                              us_id=request.user.id,
                                                              number_ans=num_ans,
                                                              is_corr=True)),
                          anss=str_anss,
                          time=0,
                          points=pts)
        stat_kr.save()
        st = '/res_kr_st/' + str(pk)
        messages.info(request, 'Работа завершена, посмотрите результаты.')
        return redirect(st)
    if not (';' + (str(request.user.id) + ';') in kr.done):
        kr.done += (str(request.user.id) + ';')
        kr.save()
    return render(request, 'do_kr.html', context)


@login_required(login_url='/login')
def res_kr_st(request, pk):
    context = {}
    kr_st = KrSt.objects.get(id=pk)
    kr = KR.objects.get(id=kr_st.kr_id)
    kol = 0
    kol_corr = 0
    for i in AnsExKR.objects.filter(kr_id=kr.id,
                                    us_id=request.user.id,
                                    number_ans=len(StatsKr.objects.filter(us_id=request.user.id,
                                                                          kr_id=kr.id))):
        if not ExKR.objects.get(id=i.ex_id).ans_file:
            kol += 1
            if i.is_corr == 1:
                kol_corr += 1
    context['kol_corr'] = kol_corr
    context['kol'] = len(ExKR.objects.filter(kr_id=kr.id))
    context['kol_file'] = len(ExKR.objects.filter(kr_id=kr.id, ans_file=True))
    context['kol_err'] = context['kol'] - context['kol_corr'] - context['kol_file']
    return render(request, 'res_kr_st.html', context)


@login_required(login_url='/login')
def all_res_kr(request, pk):
    check_super(request)

    context = {}
    context['res'] = []
    context['nums'] = []
    kr = KR.objects.get(id=pk)
    for i in range(len(ExKR.objects.filter(kr_id=pk))):
        context['nums'].append(i + 1)
    stat_kr = []
    if len(StatsKr.objects.filter(kr_id=pk)) != 0:
        stat_kr = StatsKr.objects.filter(kr_id=pk)
    kol_points_max_summ = 0
    for exercise in ExKR.objects.filter(kr_id=pk):
        kol_points_max_summ += exercise.points
    context['kol_points_max_summ'] = kol_points_max_summ
    for i in stat_kr:
        mas_info = {}
        nm = User.objects.get(id=i.us_id).first_name
        sr = User.objects.get(id=i.us_id).last_name
        mas_info['nm'] = nm
        mas_info['sr'] = sr
        mas_info['id'] = i.id
        mas_info['points'] = i.points
        mas_info['percent_correct'] = mas_info['points'] / kol_points_max_summ * 100
        mas_corr = []
        mas_info['kol'] = 0
        mas_info['kol_corr'] = 0
        for j in i.anss.split(';'):
            if j == '': continue
            mas_info['kol'] += 1
            if int(j) == 1:
                mas_info['kol_corr'] += 1
                mas_corr.append(1)
            else:
                mas_corr.append(0)
        mas_info['mas_ans'] = mas_corr
        if mas_info['kol'] == 0:
            mas_info['per'] = 0
        else:
            mas_info['per'] = round(mas_info['kol_corr'] / mas_info['kol'], 4) * 100
        context['res'].append(mas_info)
    return render(request, 'all_res_kr_tch.html', context)


@login_required(login_url='/login')
def view_st_res_kr(request, pk):
    context = {}
    check_super(request)

    stats_kr = StatsKr.objects.get(id=pk)
    check_super(request)
    nm = User.objects.get(id=stats_kr.us_id).first_name
    sr = User.objects.get(id=stats_kr.us_id).last_name
    kr_id = stats_kr.kr_id
    context = {}
    answ = AnsExKR.objects.filter(us_id=stats_kr.us_id,
                                  kr_id=stats_kr.kr_id,
                                  number_ans=stats_kr.us_num)
    kol_corr = 0
    context['kol_corr'] = stats_kr.kol_corr
    context['kol_q'] = len(answ)
    context['kol_pts'] = stats_kr.points
    quests = []
    kol = 0
    for i in answ:
        print(i.file.name)
        quests.append({'qst': ExKR.objects.get(id=i.ex_id),
                       'kol': kol + 1,
                       'my_ans': i.ans,
                       'my_file': i.file,
                       'ans': AnsExKR.objects.get(ex_id=i.ex_id,
                                                  us_id=stats_kr.us_id,
                                                  kr_id=stats_kr.kr_id,
                                                  number_ans=stats_kr.us_num)})
        kol += 1
    context['quests'] = quests
    context['nm'] = nm
    context['sr'] = sr
    if request.method == 'POST':
        a = dict(request.POST)
        print(a)
        for i in a:
            if 'csrf' in i: continue
            if 'f' in i:
                num_id = int(i.replace('f', ''))
                ansvp = AnsExKR.objects.get(id=num_id)
                ansvp.points = int(a[i][0])
                if ansvp.points == ExKR.objects.get(id=ansvp.ex_id).points:
                    ansvp.is_corr = 1
                else:
                    ansvp.is_corr = 0
                ansvp.save()

            else:
                ansvp = AnsExKR.objects.get(id=int(i))
                print(ansvp.ans)
                ansvp.is_corr = (1 + ansvp.is_corr) % 2
                if ansvp.is_corr:
                    ansvp.points = ExKR.objects.get(id=ansvp.ex_id).points
                else:
                    ansvp.points = 0
                ansvp.save()
            stats_kr.anss = ''
            kol_cr = 0
            pts = 0
            for i in AnsExKR.objects.filter(kr_id=stats_kr.kr_id,
                                            us_id=stats_kr.us_id,
                                            number_ans=stats_kr.us_num):
                if i.is_corr:
                    stats_kr.anss += '1;'
                    kol_cr += 1
                else:
                    stats_kr.anss += '0;'
                pts += i.points
            stats_kr.points = pts
            stats_kr.kol_corr = kol_cr
            stats_kr.save()
            st = '/view_st_res_kr/' + str(pk)
            messages.success(request, 'Результат ответа успешно изменен!')
            return redirect(st)
    return render(request, 'view_st_res_kr.html', context)


@csrf_exempt
def ajja(request):
    if request.method == 'POST':
        a = dict(request.POST)
        print(a)
    return HttpResponse()


@login_required(login_url='/login')
def list_of_done(request, pk):
    kr = KR.objects.get(id=pk)
    dn = kr.done.split(';')
    check_super(request)

    context = {}
    context['kr'] = kr
    context['all_ppl'] = []
    for i in dn:
        if i != '':
            dic = {}
            dic['idd'] = 'People' + str(i)
            dic['us'] = User.objects.get(id=int(i))
            context['all_ppl'].append(dic)
    if request.method == 'POST':
        # i вида People***

        for i in context['all_ppl']:
            if i['idd'] not in request.POST:
                num = int(i['idd'].replace('People', ''))
                kr.done = kr.done.replace(';' + str(num) + ';', ';')
                kr.save()
        messages.success(request, 'Успешно сохранено!')
        return redirect('/edit_kr/' + str(pk))
    # print(context['all_ppl'])
    return render(request, 'list_of_done_kr.html', context)


@login_required(login_url='/login')
def news(request):
    context = {}
    context['news'] = []
    if request.user.is_superuser:
        context['news'] = News.objects.all()
    else:
        us = request.user
        mas_groups = us.profile.group_ids.split(';')
        for i in mas_groups:
            if i != '':
                num = int(i)
                for new in News.objects.filter(groups__contains=';' + str(num) + ';'):
                    context['news'].append(new)
    context['news'] = context['news'][::-1]
    print(context['news'])
    return render(request, 'news.html', context)


@login_required(login_url='/login')
def add_news(request):
    check_super(request)
    context = {}
    context['form'] = NewsForm()
    context['groups'] = []
    for i in Group.objects.all():
        dic = {}
        dic['name'] = i.name
        dic['idd'] = 'Group' + str(i.id)
        context['groups'].append(dic)
    if request.method == 'POST':
        print(request.POST)

        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            e = News(title=form.cleaned_data['title'],
                     short_text=form.cleaned_data['short_text'],
                     text=form.cleaned_data['text'],
                     file=form.cleaned_data['file'],
                     visible_for_all=form.cleaned_data['visible_for_all'])
            for i in request.POST:
                if 'Group' in i:
                    num = int(i.replace('Group', ''))
                    e.groups += str(num)
                    e.groups += ';'
            e.save()
            messages.success(request, 'Новость успешно добавлена!')
            return redirect('/')
        messages.warning(request, 'Допущены ошибки при заполнении формы!')

    return render(request, 'add_news.html', context)


@login_required(login_url='/login')
def view_new(request, pk):
    context = {}
    new = News.objects.get(id=pk)
    if new.visible_for_all == 0:
        mas_groups = new.groups.split(';')
        fl = 0
        if request.user.is_superuser:
            fl = 1
        for i in mas_groups:
            if i != '':
                num = int(i)
                if (';' + str(num) + ';') in request.user.profile.group_ids:
                    fl = 1
        if fl == 0:
            return redirect('/')
    context['new'] = new
    return render(request, 'view_new.html', context)


@login_required(login_url='/login')
def edit_new(request, pk):
    check_super(request)
    context = {}
    context['groups'] = []
    for i in Group.objects.all():
        dic = {}
        dic['name'] = i.name
        dic['idd'] = 'Group' + str(i.id)
        dic['status'] = 0

        if (';' + str(i.id) + ';') in News.objects.get(id=pk).groups:
            dic['status'] = 1
        context['groups'].append(dic)

    new = News.objects.get(id=pk)
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=new)
        if form.is_valid():
            form.save()
        e = News.objects.get(id=pk)
        e.groups = ''
        # i вида Group***
        for i in request.POST:
            if 'Group' in i:
                num = int(i.replace('Group', ''))
                e.groups += str(num)
                e.groups += ';'
        e.save()
        messages.success(request, 'Новость успешно редактирована!')
        return redirect('/news')
    context['form'] = NewsForm(instance=new)
    return render(request, 'edit_new.html', context)


@login_required(login_url='/login')
def delete_new(request, pk):
    check_super(request)
    News.objects.filter(id=pk).delete()

    messages.success(request, 'Новость успешно удалена!')
    return redirect('/news')


def photos(request):
    context = {}
    context['photos'] = Photo.objects.all().order_by('-id')
    return render(request, 'photos.html', context)


@login_required(login_url='/login')
def add_photo(request):
    check_super(request)
    context = {}
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            Ph = Photo(text_info1=form.cleaned_data['text_info1'],
                       text_info2=form.cleaned_data['text_info2'],
                       file=form.cleaned_data['file'])
            Ph.save()
            messages.success(request, 'Фото успешно добавлено!')
            return redirect('/photos/')
    context['form'] = PhotoForm()
    return render(request, 'add_photo.html', context)
