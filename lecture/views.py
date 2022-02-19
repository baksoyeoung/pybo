from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages import get_messages
from django.utils import timezone
from .models import Season, Lectureinfo, Teacher, campus, subjects, science, grade, yoil, time
from .form import LectureCreateForm, MylectureListForm, Lecture_modify_set
from django.db.models import Q, Count
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.core import serializers
import json
import re
from .lecturefunc import lecture_time


# Create your views here.

season_list = Season.objects.order_by('-create_date')
teacher_list = Teacher.objects.order_by('name')
campus_list = campus.objects.order_by('num')
subjects_list = subjects.objects.order_by('num')
science_list = science.objects.order_by('num')
grade_list = grade.objects.order_by('num')
yoil_list = yoil.objects.order_by('num')
time_list = time.objects.order_by('num')

def lecture_home(request):

    # return render(request, 'lecture/lecture_home.html', context)

    if request.user.is_authenticated:
        form = MylectureListForm()
        mylecture_list = Lectureinfo.objects.order_by('camp_nm', 'lect_grade')

        if request.user.is_staff:
            mylecture_list = mylecture_list
            staff = True
        else:
            name = request.user.username
            staff = False
            mylecture_list = mylecture_list.filter(
                Q(name__icontains=name),  # 강사명검색
            ).distinct()

        context = {'form': form, 'season_list': season_list, 'teacher_list': teacher_list, 'campus_list': campus_list,
                   'mylecture_list': mylecture_list, 'grade_list': grade_list, 'yoil_list': yoil_list,
                   'username': request.user.username, 'staff': staff}

        print(request.user.username)
        return render(request, 'lecture/lecture_list.html', context)
    else:
        appis = 'lecture'
        url = '/lecture/lecture/list' #로그인후 이동할 url
        context = {'appis': appis, 'next': url}
        print('user no')
        print(context)
        return render(request, 'lecture/lecture_login.html', context)

@login_required(login_url='lecture:login')
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
    if request.user.is_staff:
        staff = True
    else:
        staff = False

    context = {'form': form, 'season_list': season_list, 'teacher_list': teacher_list, 'campus_list': campus_list,
               'subjects_list': subjects_list, 'science_list': science_list, 'username': request.user.username, 'staff': staff}

    return render(request, 'lecture/lecture_create.html', context)


@login_required(login_url='lecture:login')
def lecture_list(request, *args, **kwargs):
    # season_list = Season.objects.order_by('-create_date')
    # teacher_list = Teacher.objects.order_by('name')
    # campus_list = campus.objects.order_by('num')

    # print("======> GET DATA", request.GET)

    storage = get_messages(request)
    message_list = []
    for message in storage:
        message_list.append(message)

    if message_list:
        season_nm = str(message_list[0])
        camp_nm = str(message_list[1])
        name = str(message_list[2])

    if request.method == "POST":
        # print("======> POST DATA:", request.POST)
        season_nm = request.POST.get('season_nm')
        camp_nm = request.POST.get('camp_nm')
        if request.user.is_staff:
            name = request.POST.get('name')
        else:
            name = request.user.username

        grade_nm = request.POST.get('grade_nm')
        yoil_nm = request.POST.get('yoil_nm')
        set_data = {'season_nm': season_nm,
                    'camp_nm': camp_nm,
                    'name': name,
                    'grade': grade_nm,
                    'yoil_nm': yoil_nm,}

        f = MylectureListForm(set_data)
        form = f

        mylecture_list = Lectureinfo.objects.order_by('camp_nm', 'lect_grade', 'name')

        if grade_nm == '중등전체' or grade_nm == '고등전체':
            if grade_nm == '중등전체':
                grade_nm = '중'
            if grade_nm == '고등전체':
                grade_nm = '고'

            mylecture_list = mylecture_list.filter(
                Q(season_nm__icontains=season_nm), # 학기검색
                Q(camp_nm__icontains=camp_nm),  # 캠퍼스검색
                Q(name__icontains=name),  # 강사명검색
                Q(lect_yoil__contains=yoil_nm), # 요일검색
                Q(lect_grade__contains=grade_nm) # 학년

            ).distinct()
        else:
            mylecture_list = mylecture_list.filter(
                Q(season_nm__icontains=season_nm),  # 학기검색
                Q(camp_nm__icontains=camp_nm),  # 캠퍼스검색
                Q(name__icontains=name),  # 강사명검색
                Q(lect_yoil__contains=yoil_nm),  # 요일검색
                Q(lect_grade__icontains=grade_nm)  # 학년

            ).distinct()

        if request.user.is_staff:
            mylecture_list = mylecture_list
            staff = True
        else:
            name = request.user.username
            staff = False
            mylecture_list = mylecture_list.filter(
                Q(name__icontains=name),  # 강사명검색
            ).distinct()

        # print(mylecture_list)
        # print(set_data)
        # print(yoil_list)

    else:
        form = MylectureListForm()
        mylecture_list = Lectureinfo.objects.order_by('camp_nm', 'lect_grade', 'name')

        if request.user.is_staff:
            mylecture_list = mylecture_list
            staff = True
        else:
            name = request.user.username
            staff = False
            mylecture_list = mylecture_list.filter(
                Q(name__icontains=name),  # 강사명검색
            ).distinct()

    if message_list: #수정후 보여질 리스트 (강사)
        set_data = {'season_nm': season_nm,
                    'camp_nm': camp_nm,
                    'name': name,
                    'grade': '',
                    'yoil_nm': ''}

        f = MylectureListForm(set_data)
        form = f

        print(set_data)

        mylecture_list = mylecture_list.filter(
            Q(season_nm__icontains=season_nm),  # 학기검색
            Q(camp_nm__icontains=camp_nm),  # 캠퍼스검색
            Q(name__icontains=name),  # 강사명검색
        ).distinct()


    context = {'form': form, 'season_list': season_list, 'teacher_list': teacher_list, 'campus_list': campus_list,
               'mylecture_list': mylecture_list, 'grade_list': grade_list, 'yoil_list': yoil_list,
               'username': request.user.username, 'staff': staff}

    # print("관리자===>", request.user.is_staff)

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

        # print('moditfy:', lect_grade_check)
        # print('moditfy:', lect_yoil_check)
        # print('moditfy:', lect_time_check)
        # print('moditfy:', lect_time2_check)

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
            # return redirect('lecture:lecture_list')

            # mylecture_list = Lectureinfo.objects.order_by('camp_nm', 'lect_grade')
            #
            # if request.user.is_staff:
            #     mylecture_list = mylecture_list
            #     staff = True
            # else:
            #     name = request.user.username
            #     staff = False

            #     mylecture_list = mylecture_list.filter(
            #         Q(name__icontains=name),  # 강사명검색
            #         Q(season_nm__icontains=lectureinfo.season_nm), #학기검색
            #         Q(camp_nm__icontains=lectureinfo.camp_nm)
            #     ).distinct()

            # set_data = {'season_nm': request.POST['season_nm'],
            #                    'camp_nm': request.POST['camp_nm'],
            #                    'name': request.POST['name'],
            #                    'grade': '',
            #                    'yoil_nm': ''}
            # f = MylectureListForm(set_data)
            # form = f

            # context = {'form': form, 'season_list': season_list, 'teacher_list': teacher_list,
            #            'campus_list': campus_list,
            #            'mylecture_list': mylecture_list, 'grade_list': grade_list, 'yoil_list': yoil_list,
            #            'username': request.user.username, 'staff': staff}

            # print(form)

            # request.session['season_nm'] = request.POST['season_nm']
            # request.session['camp_nm'] = request.POST['camp_nm']
            # request.session['name'] = request.POST['name']

            # return redirect('{}#list_{}'.format(
            #     resolve_url('lecture:lecture_list'), lectureinfo.id))

            # Create a response
            # response = TemplateResponse(request, 'lecture/lecture_list.html', context)
            # Register the callback
            # response.add_post_render_callback(lecture_list)
            # Return the response
            # return response

            messages.add_message(request, messages.INFO, lectureinfo.season_nm)
            messages.add_message(request, messages.INFO, lectureinfo.camp_nm)
            messages.add_message(request, messages.INFO, lectureinfo.name)

            return HttpResponseRedirect(reverse(lecture_list))
            # return render(request, 'lecture/lecture_list.html', context)
    else:

        form = LectureCreateForm(instance=lectureinfo)

        lecture_modify_state = 'view'
        # print(form.is_valid())
        # print(form)

        if request.user.is_staff:
            staff = True
        else:
            staff = False

        context = {'form': form, 'season_list': season_list, 'teacher_list': teacher_list, 'campus_list': campus_list,
                   'subjects_list': subjects_list, 'science_list': science_list,
                   'lecture_modify_state': lecture_modify_state, 'staff': staff}

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

@login_required(login_url='lecture:login')
def lecture_timetable(request):

    if request.method == "POST":
        # print("======> POST DATA:", request.POST)
        season_nm = request.POST.get('season_nm')
        camp_nm = request.POST.get('camp_nm')
        name = request.POST.get('name')
        grade_nm = request.POST.get('grade_nm')
        yoil_nm = request.POST.get('yoil_nm')
        set_data = {'season_nm': season_nm,
                    'camp_nm': camp_nm,
                    'name': name,
                    'grade': grade_nm,
                    'yoil_nm': yoil_nm,}

        f = MylectureListForm(set_data)
        form = f

        mylecture_list = Lectureinfo.objects.order_by('camp_nm', 'lect_grade', 'name')

        if grade_nm == '중등전체' or grade_nm == '고등전체':
            if grade_nm == '중등전체':
                grade_nm = '중'
            if grade_nm == '고등전체':
                grade_nm = '고'

            mylecture_list = mylecture_list.filter(
                Q(season_nm__icontains=season_nm), # 학기검색
                Q(camp_nm__icontains=camp_nm),  # 캠퍼스검색
                Q(name__icontains=name),  # 강사명검색
                Q(lect_yoil__contains=yoil_nm), # 요일검색
                Q(lect_grade__contains=grade_nm) # 학년

            ).distinct().values_list('season_nm', 'camp_nm', 'name', 'subject', 'lect_nm', 'lect_grade', 'lect_yoil', 'lect_time', 'lect_time2')
        else:
            mylecture_list = mylecture_list.filter(
                Q(season_nm__icontains=season_nm),  # 학기검색
                Q(camp_nm__icontains=camp_nm),  # 캠퍼스검색
                Q(name__icontains=name),  # 강사명검색
                Q(lect_yoil__contains=yoil_nm),  # 요일검색
                Q(lect_grade__icontains=grade_nm)  # 학년

            ).distinct().values_list('season_nm', 'camp_nm', 'name', 'subject', 'lect_nm', 'lect_grade', 'lect_yoil', 'lect_time', 'lect_time2')

        # instance = mylecture_list.values_list('season_nm', 'camp_nm', 'name', 'lect_nm')

        # for item in mylecture_list:
        #     print(item)
        #
        # for item in mylecture_list:
        #     print(len(item[4]))

        # for item in mylecture_list:
        #     p = re.compile('[0-9][0-9]:[0-9][0-9]')
        #     m = p.findall(item[7])
        #     print(m)

        time_info = lecture_time(mylecture_list)

        # print(time_info[0])


        context = {'form': form, 'season_list': season_list, 'teacher_list': teacher_list, 'campus_list': campus_list,
                   'mylecture_list': mylecture_list, 'grade_list': grade_list, 'yoil_list': yoil_list, 'time_list': time_list,
                   'username': request.user.username,
                   'time_info': time_info[0],
                   'yoil_info_dc': time_info[1],
                   'yoil_info_li': time_info[2],
                   'yoil_lect_cnt': time_info[3]}

    else:
        context = {'season_list': season_list, 'teacher_list': teacher_list, 'campus_list': campus_list,
                   'grade_list': grade_list, 'yoil_list': yoil_list,
                   'username': request.user.username}

    return render(request, 'lecture/lecture_timetable.html', context)






