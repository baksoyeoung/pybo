from django.contrib import admin
from .models import Season, Lectureinfo, Teacher, campus, subjects, science, grade, yoil, time

# Register your models here.

class SeasonAdmin(admin.ModelAdmin):
    search_fields = ['season_nm']
    list_display = ['season_nm', 'create_date']

admin.site.register(Season, SeasonAdmin)

class LectureinfoAdmin(admin.ModelAdmin):
    search_fields = ['season_nm', 'name']
    list_display = ['season_nm', 'camp_nm', 'subject', 'name', 'lect_grade', 'lect_nm', 'science', 'lect_yoil', 'lect_time', 'lect_time2']

admin.site.register(Lectureinfo, LectureinfoAdmin)

class TeacherAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'num']

admin.site.register(Teacher, TeacherAdmin)

class campusAdmin(admin.ModelAdmin):
    search_fields = ['camp_nm']

admin.site.register(campus, campusAdmin)

class subjectsAdmin(admin.ModelAdmin):
    search_fields = ['subject_nm']
    list_display = ['subject_nm', 'num']

admin.site.register(subjects, subjectsAdmin)

class scienceAdmin(admin.ModelAdmin):
    search_fields = ['science_nm']
    list_display = ['science_nm', 'num']

admin.site.register(science, scienceAdmin)

class gradeAdmin(admin.ModelAdmin):
    list_display = ['grade_nm', 'num']

admin.site.register(grade, gradeAdmin)

class yoilAdmin(admin.ModelAdmin):
    list_display = ['yoil_nm', 'num']

admin.site.register(yoil, yoilAdmin)

class timeAdmin(admin.ModelAdmin):
    list_display = ['time_nm', 'num']

admin.site.register(time, timeAdmin)

