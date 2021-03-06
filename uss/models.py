from django.contrib.auth.models import User
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.postgres.fields import ArrayField

from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #image = models.ImageField(default='profile_pics/default.png', upload_to='profile_pics')
    group_ids = models.TextField(default=';', blank=True)
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        '''img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)'''


class Group(models.Model):
    name = models.TextField(verbose_name='Название группы')
    description = models.TextField(blank=True, verbose_name='Описание группы')
    color = models.IntegerField(default=0, verbose_name='Цвет группы')