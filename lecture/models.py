from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Season(models.Model):
    season_nm = models.CharField(max_length=255)
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.season_nm


class Lectureinfo(models.Model):
    season_nm = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='season_name') #학기
    camp_nm = models.CharField(max_length=255)   #캠퍼스명
    subject = models.CharField(max_length=255)   #과목
    teacher = models.CharField(max_length=255)   #강사명
    lect_nm = models.CharField(max_length=255)   #강의명
    lect_explan = models.TextField(null=True, blank=True) #강좌설명
    lect_yoil = models.CharField(max_length=50, null=True, blank=True)  #등원요일
    lect_time = models.CharField(max_length=50, null=True, blank=True)  #등원시간
    week_cnt = models.CharField(max_length=50, null=True, blank=True)   #등원횟수
    lect_fee = models.CharField(max_length=50, null=True, blank=True)   #수강료
    lect_fee_explan = models.CharField(max_length=255, null=True, blank=True) #수강료추가설명
    create_date = models.DateTimeField()         #생성날짜시간
    modify_date = models.DateTimeField(null=True, blank=True) #수정날짜시간
