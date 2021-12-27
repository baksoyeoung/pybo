from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class Gitenstudent(models.Model):
    nameis = models.CharField(max_length=50)
    schoolis = models.CharField(max_length=100)
    gradeis = models.CharField(max_length=50)
    phoneis = models.CharField(max_length=200)
    bboosamis = models.CharField(max_length=50)
    emailis = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    monthis = models.CharField(max_length=50)
    firstweek = models.CharField(max_length=100)
    secondweek = models.CharField(max_length=100)
    thirdweekone = models.CharField(max_length=100)
    thirdweektwo = models.CharField(max_length=100)
    fourthweek = models.CharField(max_length=100)
    create_date = models.DateTimeField(null=True, blank=True)
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.nameis, self.schoolis, self.gradeis, self.phoneis







