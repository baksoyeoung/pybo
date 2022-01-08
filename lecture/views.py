from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Season, Lectureinfo, Teacher
from .form import LectureCreateForm

# Create your views here.

def lecture_home(request):
    return render(request, 'lecture/lecture_home.html')


def lecture_create(request):
    season_list = Season.objects.order_by('-create_date')
    teacher_list = Teacher.objects.order_by('name')
    if request.method == 'POST':
        print("======> POST DATA:", request.POST)
        lect_grade_check = request.POST.getlist('lect_grade[]')
        lect_yoil_check = request.POST.getlist('lect_yoil[]')
        lect_time_check = request.POST.getlist('lect_time[]')
        lect_time2_check = request.POST.getlist('lect_time2[]')

        form = LectureCreateForm(request.POST)
        print(form)
        if form.is_valid():
            lectureinfo = form.save(commit=False)
            lectureinfo.lect_grade = lect_grade_check[]
            lectureinfo.lect_yoil = lect_yoil_check[]
            lectureinfo.lect_time = lect_time_check[]
            lectureinfo.lect_time2 = lect_time2_check[]
            lectureinfo.create_date = timezone.now()
            lectureinfo.save()

            print("강의등록정보",lectureinfo)
    else:
        form = LectureCreateForm()

    context = {'form': form, 'season_list': season_list, 'teacher_list': teacher_list}

    return render(request, 'lecture/lecture_create.html', context)


def lecture_timetable(request):
    return render(request, 'lecture/lecture_timetable.html')
