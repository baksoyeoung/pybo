from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Season, Lectureinfo, Teacher, campus, subjects, science
from .form import LectureCreateForm, MylectureListForm, Lecture_modify_set
from django.db.models import Q, Count
from django.template import RequestContext
from django.core import serializers
import json


# Create your views here.

season_list = Season.objects.order_by('-create_date')
teacher_list = Teacher.objects.order_by('name')
campus_list = campus.objects.order_by('num')
subjects_list = subjects.objects.order_by('num')
science_list = science.objects.order_by('num')

def lecture_home(request):
    return render(request, 'lecture/lecture_home.html')


def lecture_create(request):
    # season_list = Season.objects.order_by('-create_date')
    # teacher_list = Teacher.objects.order_by('name')
    # campus_list = campus.objects.order_by('num')
    # subjects_list = subjects.objects.order_by('num')
    # science_list = science.objects.order_by('num')

    if request.method == 'POST':
        # print("======> POST DATA:", request.POST)
        lect_grade_check = request.POST.getlist('lect_grade')
        lect_yoil_check = request.POST.getlist('lect_yoil')
        lect_time_check = request.POST.getlist('lect_time')
        lect_time2_check = request.POST.getlist('lect_time2')

        form = LectureCreateForm(request.POST)
        # print(form)
        if form.is_valid():
            lectureinfo = form.save(commit=False)
            lectureinfo.lect_grade = lect_grade_check
            lectureinfo.lect_yoil = lect_yoil_check
            lectureinfo.lect_time = lect_time_check
            lectureinfo.lect_time2 = lect_time2_check
            lectureinfo.create_date = timezone.now()
            lectureinfo.save()

            set_data = {'season_nm': lectureinfo.season_nm,
                        'camp_nm': lectureinfo.camp_nm,
                        'subject': lectureinfo.subject,
                        'lect_grade': lectureinfo.lect_grade,
                        'name': lectureinfo.name,
                        'lect_nm': lectureinfo.lect_nm,
                        'lect_explan': lectureinfo.lect_explan,
                        'timeselect': lectureinfo.timeselect,
                        'lect_yoil': lectureinfo.lect_yoil,
                        'lect_time': lectureinfo.lect_time,
                        'lect_time2': lectureinfo.lect_time2,
                        'week_cnt': lectureinfo.week_cnt,
                        'in_cnt': lectureinfo.in_cnt,
                        'lect_fee': lectureinfo.lect_fee,
                        'lect_fee_explan': lectureinfo.lect_fee_explan,
                        'science': lectureinfo.science}

            f = LectureCreateForm(set_data)
            print(f)
            form = f

    else:
        form = LectureCreateForm()

        # print(form)

    context = {'form': form, 'season_list': season_list, 'teacher_list': teacher_list, 'campus_list': campus_list,
               'subjects_list': subjects_list, 'science_list': science_list}

    return render(request, 'lecture/lecture_create.html', context)

def lecture_list(request):
    # season_list = Season.objects.order_by('-create_date')
    # teacher_list = Teacher.objects.order_by('name')
    # campus_list = campus.objects.order_by('num')

    # print("======> GET DATA", request.GET)

    if request.method == "POST":
        # print("======> POST DATA:", request.POST)
        season_nm = request.POST.get('season_nm')
        camp_nm = request.POST.get('camp_nm')
        name = request.POST.get('name')
        set_data = {'season_nm': season_nm,
                    'camp_nm': camp_nm,
                    'name': name,}

        f = MylectureListForm(set_data)
        form = f

        mylecture_list = Lectureinfo.objects.order_by('camp_nm', '-lect_grade')

        mylecture_list = mylecture_list.filter(
            Q(season_nm__icontains=season_nm), # 학기검색
            Q(camp_nm__icontains=camp_nm),  # 캠퍼스검색
            Q(name__icontains=name)   # 강사명검색

        ).distinct()

        print(mylecture_list)

    else:
        form = MylectureListForm()
        mylecture_list = Lectureinfo.objects.order_by('camp_nm', '-lect_grade')

    context = {'form': form, 'season_list': season_list, 'teacher_list': teacher_list, 'campus_list': campus_list,
               'mylecture_list': mylecture_list}

    return render(request, 'lecture/lecture_list.html', context)

def lecture_modify(request, lectureinfo_id):
    """
    강의수정
    """
    lectureinfo = get_object_or_404(Lectureinfo, pk=lectureinfo_id)

    # print(lectureinfo)

    if request.method == "POST":
        lect_grade_check = request.POST.getlist('lect_grade')
        lect_yoil_check = request.POST.getlist('lect_yoil')
        lect_time_check = request.POST.getlist('lect_time')
        lect_time2_check = request.POST.getlist('lect_time2')

        print('moditfy:', lect_grade_check)
        print('moditfy:', lect_yoil_check)
        print('moditfy:', lect_time_check)
        print('moditfy:', lect_time2_check)

        form = LectureCreateForm(request.POST, instance=lectureinfo)
        print('modify:', form.is_valid())
        if form.is_valid():
            lectureinfo = form.save(commit=False)
            lectureinfo.lect_grade = lect_grade_check
            lectureinfo.lect_yoil = lect_yoil_check
            lectureinfo.lect_time = lect_time_check
            lectureinfo.lect_time2 = lect_time2_check
            lectureinfo.modify_date = timezone.now()
            lectureinfo.save()
            return redirect('lecture:lecture_list')
    else:

        form = LectureCreateForm(instance=lectureinfo)

        lecture_modify_state = 'view'
        # print(form.is_valid())
        # print(form)

    context = {'form': form, 'season_list': season_list, 'teacher_list': teacher_list, 'campus_list': campus_list,
               'subjects_list': subjects_list, 'science_list': science_list,
               'lecture_modify_state': lecture_modify_state}

    return render(request,'lecture/lecture_create.html', context)


def lecture_delete(request, lectureinfo_id):
    """
    강의삭제
    """
    lectureinfo = get_object_or_404(Lectureinfo, pk=lectureinfo_id)
    # if request.user != question.author:
    #     messages.error(request, '삭제권한이 없습니다.')
    #     return redirect('pybo:detail', question_id=question.id)
    lectureinfo.delete()
    return redirect('lecture:lecture_list')

def lecture_timetable(request):
    return render(request, 'lecture/lecture_timetable.html')
