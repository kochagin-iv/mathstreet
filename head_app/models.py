from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from ckeditor.fields import RichTextField
from django.utils.timezone import now
from uss.models import *
# Create your models here.


class QuestionVPR(models.Model):
    num_ex = models.IntegerField(verbose_name='Номер задания ВПР', blank=True, null=True)
    description = RichTextUploadingField(verbose_name='Задание', blank=True, null=True)
    corr_ans = models.CharField(verbose_name='Верный ответ', blank=True, max_length=100)

    def save(self):
        super(QuestionVPR, self).save()


class AnswerVPR(models.Model):
    us_id = models.IntegerField(verbose_name='ID ученика', blank=True, default=-1)
    q_id = models.IntegerField(blank=True, null=True)
    ans = models.CharField(max_length=100, blank=True, null=True)
    test_id = models.IntegerField(blank=True, null=True)
    is_corr = models.BooleanField(verbose_name='Верный ли ответ', blank=True, default=0)

    def __str__(self):
        return 'Answer ' + str(self.us_id) + ' test_num ' + str(self.test_id)


class TestVPR(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название теста')
    description = models.TextField(verbose_name='Краткое описание теста', blank=True)
    done = models.TextField(verbose_name='Список уже выполнивших тест', blank=True)
    time = models.IntegerField(verbose_name='Время на выполнение задание в минутах', blank=True, default=0)
    groups = models.TextField(verbose_name='Задано следующим группам', default=';', blank=True, null=True)
    is_visible = models.BooleanField(default=0)

    def __str__(self):
        return 'Test ' + str(self.name)


class StudentsWorks(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    description = RichTextUploadingField(verbose_name='Работа ученика', blank=True, null=True)
    file = models.FileField(verbose_name='Добавить файл', upload_to='students_works_upload/', blank=True, null=True)


class AnsEx(models.Model):
    us_id = models.IntegerField(verbose_name='ID ученика', blank=True, default=-1)
    description = RichTextUploadingField(verbose_name='Ответ', blank=True, null=True)
    file = models.FileField(verbose_name='Добавить файл', upload_to='documents_upload/', blank=True, null=True)
    ex_id = models.IntegerField(blank=True, null=True)
    is_check = models.BooleanField(default=False)


class TestVPR_Student(models.Model):
    us_id = models.IntegerField(verbose_name='ID ученика', blank=True, default=-1)
    test_id = models.IntegerField(verbose_name='id теста')


class KR(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название', null=True, blank=True)
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    time = models.IntegerField(verbose_name='Время в минутах', default=10)
    done = models.TextField(verbose_name='Уже делали')
    groups = models.TextField(verbose_name='Задано следующим группам', default=';', blank=True, null=True)
    #view_st_res
    visible = models.BooleanField(verbose_name='Работа видна', default=0, blank=True)


class ExKR(models.Model):
    description = RichTextUploadingField(verbose_name='Задание', blank=True, null=True)
    corr_ans = models.CharField(verbose_name='Верный ответ', blank=True, max_length=100)
    kr_id = models.IntegerField(verbose_name='Ключ связи с кр')
    file = models.FileField(verbose_name='Файл, прикрепленный к заданию',
                            upload_to='documents_upload/', blank=True)
    ans_file = models.BooleanField(verbose_name='Ответ - файл', blank=True, default=False)
    ans_text = models.BooleanField(verbose_name='Ответ - текст', blank=True, default=False)

    points = models.IntegerField(verbose_name='Количество баллов за задание', default=1)


class AnsExKR(models.Model):
    us_id = models.IntegerField(verbose_name='ID ученика', blank=True, default=-1)
    ans = models.CharField(verbose_name='Ответ', max_length=100, blank=True, null=True, default='')
    ex_id = models.IntegerField(blank=True, null=True)
    number_ans = models.IntegerField(blank=True, default=1, verbose_name='Какой по счету ответ на задание от ученика')
    is_corr = models.BooleanField(default=False)
    kr_id = models.IntegerField()
    file = models.FileField(verbose_name='Файл, ответ на задание(при необходимости)',
                            upload_to='documents_upload/', blank=True)
    points = models.IntegerField(verbose_name='Полученные баллы за задание', default=1)

    def __str__(self):
        return str(User.objects.get(id=self.us_id).first_name) + ' ' + str(User.objects.get(id=self.us_id).last_name) + ' ' + KR.objects.get(id=self.kr_id).name


class KrSt(models.Model):
    us_id = models.IntegerField(verbose_name='ID ученика', blank=True, default=-1)
    kr_id = models.IntegerField(verbose_name='ключ связи с кр')


class StatsKr(models.Model):
    us_id = models.IntegerField(verbose_name='ID ученика', blank=True, default=-1)
    us_num = models.IntegerField(verbose_name='Номер попытки', blank=True, default=1)
    kr_id = models.IntegerField(verbose_name='ID работы')
    kol_num = models.IntegerField(verbose_name='Число заданий в работе', blank=True)
    kol_corr = models.IntegerField(verbose_name='Количество правильных ответов', blank=True)
    anss = models.TextField(verbose_name='Правильно/нет ответил ученик', blank=True)
    time = models.IntegerField(verbose_name='Потраченное время на работу', blank=True)
    points = models.IntegerField(verbose_name='Набранные за работу баллы', default=0)

    def __str__(self):
        return str(User.objects.get(id=self.us_id).first_name) + ' ' + str(User.objects.get(id=self.us_id).last_name) + ' ' + KR.objects.get(id=self.kr_id).name


class News(models.Model):
    title = models.CharField(verbose_name='Название', max_length=200)
    short_text = models.TextField(verbose_name='Короткий заголовок(при необходимости)', blank=True)
    text = RichTextUploadingField(verbose_name='Текст', blank=True, null=True)
    date = models.DateField(verbose_name='Время добавления', default=now, editable=False)
    groups = models.TextField(verbose_name='Задано следующим группам', default=';', blank=True, null=True)
    visible_for_all = models.BooleanField(verbose_name='Новость видна всем', default=False)
    file = models.FileField(verbose_name='Файл, прикрепленный к новости',
                            upload_to='news_upload/', blank=True)


class Photo(models.Model):
    text_info1 = models.CharField(verbose_name='Название', max_length=200, blank=True)
    text_info2 = models.CharField(verbose_name='Текст/место/дата...', max_length=200, blank=True)
    file = models.ImageField(verbose_name='Фото',
                             upload_to='photos_upload/', blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.file.path)

        if img.height > 500 or img.weight > 500:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.file.path)
