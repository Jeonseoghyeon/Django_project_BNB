# Q2-1
from django import forms # ModelForm 상속을 위해 forms를 불러옵니다.
from .models import Reservation # ReservationForm의 model을 설정해주기 위해 Reservation class를 불러옵니다.

class ReservationForm(forms.ModelForm): # Reservation 모델 작성을 위한 모델 폼 설정
    class Meta:
        model = Reservation # 모델폼의 모델을 models.py에서 선언한 Reservation Class로 설정
        fields = '__all__' # 모든 필드의 값을 받습니다.