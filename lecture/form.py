from django import forms
from lecture.models import Lectureinfo

class LectureCreateForm(forms.ModelForm):
    class Meta:
        model = Lectureinfo #사용할 모델
        fields = ["season_nm", "camp_nm", "subject", "lect_grade", "name", "lect_nm", "lect_explan", "timeselect", "lect_yoil", "lect_time", "lect_time2", "week_cnt", "in_cnt", "lect_fee", "lect_fee_explan"]

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