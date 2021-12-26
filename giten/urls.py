from django.urls import path
from . import views

app_name = 'giten'

urlpatterns = [
    #base_views.py
    # path('', base_views.index, name='index'),
    # path('<int:question_id>/', base_views.detail, name='detail'),

    #question_views.py
    # path('question/create/',question_views.question_create, name='question_create'),
    # path('question/modify/<int:question_id>/', question_views.question_modify, name='question_modify'),
    # path('question/delete/<int:question_id>/', question_views.question_delete, name='question_delete'),

    path('', views.index, name='index'),
]