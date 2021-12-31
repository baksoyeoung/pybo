from django.contrib import admin
from .models import Gitenstudent

# Register your models here.

class GitenstudentAdmin(admin.ModelAdmin):
    search_fields = ['nameis']

admin.site.register(Gitenstudent)
