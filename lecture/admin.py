from django.contrib import admin
from .models import Season, Lectureinfo, Teacher

# Register your models here.

class SeasonAdmin(admin.ModelAdmin):
    search_fields = ['season_nm']

admin.site.register(Season, SeasonAdmin)

class LectureinfoAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Lectureinfo, LectureinfoAdmin)

class TeacherAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(Teacher, TeacherAdmin)
