from django.urls import path
from . import views

app_name = 'lecture'

urlpatterns = [
    path('', views.lecture_home, name='index'),
    # path('giten/ncreate/', views.giten_ncreate, name='giten_ncreate'),
    # path('giten/ycreate/', views.giten_ycreate, name='giten_ycreate'),
    # path('giten/directions/', views.giten_directions, name='giten_directions'),

]