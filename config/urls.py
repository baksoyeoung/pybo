"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from pybo import views
from pybo.views import base_views
from giten import views
from lecture import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')),
    path('common/', include('common.urls')),
    path('giten/', include('giten.urls')),
    path('lecture/', include('lecture.urls')),
    # path('', base_views.index, name='index'), # '/' 에 해당하는 path -> settings.py 에 LOGIN_REDIRECT_URL
    #path('', views.index, name='index'), # giten 인덱스
    path('', views.lecture_list, name='index'), #lecture 인덱스
]
