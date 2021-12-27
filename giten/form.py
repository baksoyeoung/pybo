from django import forms
from giten.models import Gitenstudent

class GitenCreateForm(forms.ModelForm):
    class Meta:
        model = Gitenstudent #사용할 모델
        fields = ['nameis', 'schoolis', 'gradeis', 'phoneis', 'bboosamis', 'emailis', 'monthis', 'firstweek',
                  'secondweek', 'thirdweekone', 'thirdweektwo', 'fourthweek'] #GitenCreateForm 사용할 Gitenstudent 모델의 속성

        labels = {
            'nameis':'이름',
            'schoolis': '학교',
            'gradeis': '학년',
            'phoneis': '전화번호',
            'bboosamis': '재원/비재원',
            'emailis': '이메일',
            'monthis': '신청월',
            'firstweek': '등원요일(1주차)',
            'secondweek': '등원요일(2주차)',
            'thirdweekone': '등원요일(3주자)',
            'thirdweektwo': '등원요일(3주자)',
            'fourthweek': '등원요일(4주자)',

        }