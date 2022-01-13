from django import forms
from lecture.models import Lectureinfo

class LectureCreateForm(forms.ModelForm):
    class Meta:
        model = Lectureinfo #사용할 모델
        fields = ["season_nm", "camp_nm", "subject", "lect_grade", "name", "lect_nm", "lect_explan", "timeselect", "lect_yoil", "lect_time", "lect_time2", "week_cnt", "in_cnt", "lect_fee", "lect_fee_explan"]
        # fields = '__all__'

        labels = {
            'season_nm': '학기',
            'camp_nm': '캠퍼스명',
            'subject': '과목',
            'lect_grade': '대상학년',
            'name': '강사명',
            'lect_nm': '강의명',
            'lect_explan': '강의설명',
            'timeselect': '등원시간협의',
            'lect_yoil': '등원요일',
            'lect_time': '시작시간',
            'lect_time2': '종료시간',
            'week_cnt': '시간개수',
            'in_cnt': '수강개수',
            'lect_fee': '수강료',
            'lect_fee_explan': '수강료추가설명',
        }

class MylectureListForm(forms.Form):
    season_nm = forms.CharField(max_length=255)
    camp_nm = forms.CharField(max_length=255)
    name = forms.CharField(max_length=50)

# class LectureCreateForm_set(forms.Form):
#     season_nm = forms.CharField(max_length=255)
#     camp_nm = forms.CharField(max_length=255)
#     subject = forms.CharField(max_length=255)
#     lect_grade = forms.CharField(max_length=255)
#     name = forms.CharField(max_length=50)
#     lect_nm = forms.CharField(max_length=255)
#     lect_explan = forms.CharField(widget=forms.Textarea, required=False)
#     timeselect = forms.BooleanField(required=False)
#     lect_yoil = forms.CharField(max_length=255, required=False)
#     lect_time = forms.CharField(max_length=255, required=False)
#     lect_time2 = forms.CharField(max_length=255, required=False)
#     week_cnt = forms.CharField(max_length=50, required=False)
#     in_cnt = forms.CharField(max_length=50, required=False)
#     lect_fee = forms.CharField(max_length=50, required=False)
#     lect_fee_explan = forms.CharField(widget=forms.Textarea, max_length=50, required=False)


