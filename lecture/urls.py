from django.urls import path
from . import views

app_name = 'lecture'

urlpatterns = [
    path('', views.lecture_home, name='index'),
    path('lecture/create', views.lecture_create, name='lecture_create'),
    path('lecture/timetable', views.lecture_timetable, name='lecture_timetable'),
    path('lecture/list', views.lecture_list, name='lecture_list'),
    path('lecture/modify/<int:lectureinfo_id>/', views.lecture_modify, name='lecture_modify'),
    # path('giten/ncreate/', views.giten_ncreate, name='giten_ncreate'),
    # path('giten/ycreate/', views.giten_ycreate, name='giten_ycreate'),
    # path('giten/directions/', views.giten_directions, name='giten_directions'),

]