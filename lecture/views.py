from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Season, Lectureinfo

# Create your views here.

def lecture_home(request):
    return render(request, 'lecture/lecture_home.html')
