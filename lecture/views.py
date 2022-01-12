from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Season, Lectureinfo, Teacher, campus, subjects
from .form import LectureCreateForm, MylectureList
from django.forms import modelformset_factory


# Create your views here.

def lecture_home(request):
    return render(request, 'lecture/lecture_home.html')


def lecture_create(request):
    season_list = Season.objects.order_by('-create_date')
    teacher_list = Teacher.objects.order_by('name')
    campus_list = campus.objects.order_by('num')
    subjects_list = subjects.objects.order_by('num')

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
                        'lect_fee_explan': lectureinfo.lect_fee_explan,}

            f = LectureCreateForm(set_data)
            # print(f)
            form = f

    else:
        form = LectureCreateForm()

        # print(form)

    context = {'form': form, 'season_list': season_list, 'teacher_list': teacher_list, 'campus_list': campus_list, 'subjects_list': subjects_list}

    return render(request, 'lecture/lecture_create.html', context)

def lecture_list(request):
    season_list = Season.objects.order_by('-create_date')
    teacher_list = Teacher.objects.order_by('name')
    campus_list = campus.objects.order_by('num')

    if request.method == "POST":
        print("======> POST DATA:", request.POST)
        mylectureList = Lectureinfo.objects



    form = MylectureList()
    context = {'form': form, 'season_list': season_list, 'teacher_list': teacher_list, 'campus_list': campus_list}

    return render(request, 'lecture/lecture_list.html', context)


def lecture_timetable(request):
    return render(request, 'lecture/lecture_timetable.html')
