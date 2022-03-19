from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import GeneratePdf

app_name = 'lecture'

urlpatterns = [
    path('', views.lecture_home, name='index'),
    path('lecture/create', views.lecture_create, name='lecture_create'),
    path('lecture/timetable', views.lecture_timetable, name='lecture_timetable'),
    path('lecture/form', views.lecture_form, name='lecture_form'),
    path('lecture/list', views.lecture_list, name='lecture_list'),
    path('lecture/modify/<int:lectureinfo_id>/', views.lecture_modify, name='lecture_modify'),
    path('lecture/delete/<int:lectureinfo_id>/', views.lecture_delete, name='lecture_delete'),
    path('lecture/login', auth_views.LoginView.as_view(template_name='lecture/lecture_login.html'), name='login'),
    path('lecture/logout', auth_views.LogoutView.as_view(), name='logout'),
    path('lecture_form_pdf', GeneratePdf.as_view(), name='lecture_form_pdf'),
    # path('giten/ncreate/', views.giten_ncreate, name='giten_ncreate'),
    # path('giten/ycreate/', views.giten_ycreate, name='giten_ycreate'),
    # path('giten/directions/', views.giten_directions, name='giten_directions'),

]