from django.contrib import admin
from .models import *
from uss.models import *
from video_lessons.models import *
# Register your models here.
admin.site.register(QuestionVPR)
admin.site.register(AnswerVPR)
admin.site.register(TestVPR)
admin.site.register(StudentsWorks)
admin.site.register(AnsEx)
admin.site.register(TestVPR_Student)
admin.site.register(KR)
admin.site.register(ExKR)
admin.site.register(AnsExKR)
admin.site.register(Profile)
admin.site.register(Group)
admin.site.register(KrSt)
admin.site.register(StatsKr)
admin.site.register(News)
admin.site.register(Photo)
admin.site.register(VideoLesson)