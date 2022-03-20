from .models import Season, Lectureinfo, Teacher, campus, subjects, science, grade, yoil, time
from django.db.models import Q

teacher_list = Teacher.objects.all().order_by('name')

def mylecture_form_list(season_nm, camp_nm, subject, name, grade_nm):
    mylecture_list = Lectureinfo.objects.all().order_by('display_order', 'subject', 'name', 'lect_grade')

    mylecture_list = mylecture_list.filter(
        Q(season_nm__icontains=season_nm),  # 학기검색
        Q(camp_nm__icontains=camp_nm),  # 캠퍼스검색
        Q(subject__icontains=subject),  # 과목검색
        Q(name__icontains=name),  # 강사명검색
        Q(lect_grade__icontains=grade_nm)  # 학년

    ).distinct().values_list('season_nm', 'camp_nm', 'name', 'subject', 'lect_nm', 'lect_grade', 'lect_yoil',
                             'lect_time', 'lect_time2', 'display_order', 'week_cnt', 'in_cnt', 'lect_fee', 'timeselect',
                             'lect_bigo')

    mylecture_list_order = []
    for item in mylecture_list:
        for member in teacher_list:
            if member.name == item[2]:
                num = []
                num.append(member.num)
                mylecture_list_order.append(list(item) + num)

    # mylecture_list_order.sort(key=lambda x: x[9])
    # f = sorted(e, key=lambda x: (x[0], -x[1]))

    mylecture_list = sorted(mylecture_list_order, key=lambda x: (x[15], x[9]))

    mylecture_list = mylecture_list

    return mylecture_list