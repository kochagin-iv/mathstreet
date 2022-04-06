from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from ckeditor.fields import RichTextField
from django.utils.timezone import now
from django.core.validators import FileExtensionValidator
from uss.models import *


class VideoLesson(models.Model):
    link = models.CharField(verbose_name='Ссылка на видео', max_length=200)
    name = models.CharField(verbose_name='Название видео', max_length=200, blank=True)
    annotation_file = models.FileField(verbose_name='Конспект',
                                       upload_to='annotation_upload/',
                                       validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
                                       blank=True, null=True)
    num_class = models.CharField(verbose_name='Класс', max_length=200, blank=True)
    tag_subj = models.TextField(verbose_name='Тэг предмета', blank=True)
    subj = models.TextField(verbose_name='Предмет', blank=True)
