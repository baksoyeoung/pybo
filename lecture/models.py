from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Season(models.Model):
    season_nm = models.CharField(max_length=255)
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.season_nm


class Teacher(models.Model):
    name = models.CharField(max_length=50) #강사명
    subject = models.CharField(max_length=50) #담당과목
    num = models.IntegerField() #과목별 출력순번

    def __str__(self):
        return (self.name)

class campus(models.Model):
    camp_nm = models.CharField(max_length=255)
    num = models.IntegerField() #캠퍼스 출력순번

    def __str__(self):
        return (self.camp_nm)

class subjects(models.Model):
    subject_nm = models.CharField(max_length=255)
    num = models.IntegerField() #캠퍼스 출력순번

    def __str__(self):
        return (self.subject_nm)

class science(models.Model):
    science_nm = models.CharField(max_length=255)
    num = models.IntegerField() #과학세부과목 출력순서

class grade(models.Model):
    grade_nm = models.CharField(max_length=255)
    num = models.IntegerField() #학년 출력순서

class yoil(models.Model):
    yoil_nm = models.CharField(max_length=50)
    num = models.IntegerField() #요일 출력순서

class time(models.Model):
    time_nm = models.CharField(max_length=50)
    num = models.IntegerField()


class Lectureinfo(models.Model):
    season_nm = models.CharField(max_length=255) #학기
    camp_nm = models.CharField(max_length=255)    #캠퍼스명
    subject = models.CharField(max_length=255)    #과목
    lect_grade = models.CharField(max_length=255) #수강학년
    name = models.CharField(max_length=50)   #강사명
    name2 = models.CharField(max_length=50, null=True, blank=True)  # 팀수업강사명
    lect_nm = models.CharField(max_length=255)    #강의명
    lect_explan = models.TextField(null=True, blank=True) #강의설명
    timeselect = models.BooleanField(default=False) #등원시간협의
    lect_yoil = models.CharField(max_length=255, null=True, blank=True)  #등원요일
    lect_time = models.CharField(max_length=255, null=True, blank=True)  #시작시간
    lect_time2 = models.CharField(max_length=255, null=True, blank=True)  # 종료시간
    week_cnt = models.CharField(max_length=50, null=True, blank=True)    #시간개수
    in_cnt = models.CharField(max_length=50, null=True, blank=True)      #수강개수
    lect_fee = models.CharField(max_length=50, null=True, blank=True)    #수강료
    lect_fee_explan = models.TextField(null=True, blank=True)            #수강료추가설명
    science = models.CharField(max_length=50, null=True, blank=True)     #과학세부과목
    create_date = models.DateTimeField()          #생성날짜시간
    modify_date = models.DateTimeField(null=True, blank=True) #수정날짜시간
    display_order = models.IntegerField(null=True, blank=True) #표시순선
    lect_bigo = models.TextField(null=True, blank=True) #비고

    def __str__(self):
        return (self.lect_nm)




