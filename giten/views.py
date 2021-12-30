from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Gitenstudent
from .form import GitenCreateForm


# Create your views here.

def index(request):
    return render(request, 'giten/giten_home.html')


def giten_ncreate(request):  # 노형캠 모의고사 신청하기
    if request.method == 'POST':
        # print("======> POST DATA:", request.POST)
        # print("======> POST DATA:", request.POST.getlist('thirdweek[]'))
        thirdweekChk = request.POST.getlist('thirdweek[]')
        print("======> POST DATA:", thirdweekChk)
        form = GitenCreateForm(request.POST)
        if form.is_valid():
            Gitenstudent = form.save(commit=False)
            Gitenstudent.thirdweekone = thirdweekChk[0]
            Gitenstudent.thirdweektwo = thirdweekChk[1]
            Gitenstudent.create_date = timezone.now()
            Gitenstudent.save()
            return redirect('giten:index')
    else:
        form = GitenCreateForm()
    context = {'form': form}
    return render(request, 'giten/giten_ncreate.html', context)


def giten_ycreate(request):  # 노형캠 모의고사 신청하기
    if request.method == 'POST':
        # print("======> POST DATA:", request.POST)
        # print("======> POST DATA:", request.POST.getlist('thirdweek[]'))
        thirdweekChk = request.POST.getlist('thirdweek[]')
        print("======> POST DATA:", thirdweekChk)
        form = GitenCreateForm(request.POST)
        if form.is_valid():
            Gitenstudent = form.save(commit=False)
            Gitenstudent.thirdweekone = thirdweekChk[0]
            Gitenstudent.thirdweektwo = thirdweekChk[1]
            Gitenstudent.create_date = timezone.now()
            Gitenstudent.save()
            return redirect('giten:index')
    else:
        form = GitenCreateForm()
    context = {'form': form}
    return render(request, 'giten/giten_ycreate.html', context)
