"""dist_learn URL Configuration

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
from django.contrib import admin
from django.urls import path
from head_app import views as hviews
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.conf.urls import handler404, handler500
from .settings import MIDDLEWARE, INSTALLED_APPS
from django.contrib.staticfiles.views import serve
from django.views.decorators.cache import cache_control
from django.views.decorators.cache import never_cache

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', hviews.home, name='home'),
    path('add_vpr/', hviews.add_vpr, name='add_vpr'),
    path('edit_vpr/<int:pk>/', hviews.edit_vpr, name='edit_vpr'),
    path('add_test_vpr/', hviews.add_test_vpr, name='add_test_vpr'),
    path('all_tests/', hviews.all_tests, name='all_test_vpr'),
    path('test_fio/<int:pk>/', hviews.test_fio, name='test_fio'),
    path('test/<int:pk>/', hviews.do_test, name='do_test'),
    path('results_testvpr/<int:pk>/', hviews.res_t_vpr_st, name='res_t_vpr'),
    path('all_quest_vpr/', hviews.all_q_vpr, name='all_q_vpr'),
    path('view_vpr/<int:pk>/', hviews.view_vpr_num, name='view_vpr_num'),
    path('view_all_res_vpr/<int:pk>', hviews.view_all_test_res_vpr, name='view_all_vpr'),
    path('test_view_res/<int:pk>', hviews.test_view_res_tch, name='test_tch_vpr'),
    path('add_st_work/', hviews.add_st_work, name='add_ex'),
    path('edit_st_work/<int:pk>/', hviews.edit_st_work, name='add_ex'),
    path('all_works/', hviews.all_works, name='all_ex'),
    path('view_st_work/<int:pk>/', hviews.view_st_work, name='do_ex'),
    path('add_kr/', hviews.add_kr, name='add_kr'),
    path('all_kr/', hviews.all_kr, name='all_kr'),
    path('edit_kr/<int:pk>/', hviews.edit_kr, name='edit_kr'),
    path('add_kr_ex/<int:pk>', hviews.add_kr_ex, name='add_kr_ex'),
    path('edit_kr/<int:pk>/<int:idd>/', hviews.edit_q_kr, name='edit_q_kr'),
    path('kr_fio/<int:pk>/', hviews.kr_fio, name='kr_fio'),
    path('do_kr/<int:pk>/', hviews.do_kr, name='do_kr'),
    path('res_kr_st/<int:pk>/', hviews.res_kr_st, name='res_kr_st'),
    path('all_res_kr/<int:pk>', hviews.all_res_kr, name='all_res_kr'),
    path('view_st_res_kr/<int:pk>', hviews.view_st_res_kr, name='view_st_res_kr'),
    path('list_of_done/<int:pk>', hviews.list_of_done, name='list_of_done_kr'),
    path('ajjja/', hviews.ajja, name='aja'),
    path('news/', hviews.news, name='news'),
    path('add_news', hviews.add_news, name='add_news'),
    path('view_new/<int:pk>', hviews.view_new, name='view_new'),
    path('edit_new/<int:pk>', hviews.edit_new, name='edit_new'),
    path('delete_new/<int:pk>', hviews.delete_new, name='delete_new'),
    path('photos/', hviews.photos, name='photos'),
    path('add_photo/', hviews.add_photo, name='add_photo'),
    path('about/', hviews.about, name='about'),


    url('', include('uss.urls')),
    url('', include('video_lessons.urls')),
]

handler404 = 'head_app.views.handler404'
handler500 = 'head_app.views.handler500'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT,)