from django.shortcuts import render, redirect # redirect를 위해 해당 경로에서 redirect를 불러옵니다.
from .forms import ReservationForm # ReservationForm 사용을 위해 해당 경로에서 모델폼을 불러옵니다.
from .models import Reservation # Reservation 사용을 위해 해당 경로에서 모델을 불러옵니다.
# 각 문제를 해결하기 위하여 필요한 import문은 이곳에 작성합니다.

def index(request): # 예약내역에 대한 데이터를 얻고 index페이지로 render하기 위한 함수
    # Q2-3
    reservations=Reservation.objects.order_by('-date') # reservations이라는 변수 안에 Reservation이라는 모델에 있는 객체들을 date 기준 내림차순으로 넣어줍니다.
    context={ # context라는 딕셔너리에 reservations 정보를 저장해주고
        'reservations':reservations
    }
    return render(request,'reservations/index.html',context) # reservations/index.html 경로로 정보를 전달해주며 render합니다. 이 데이터는 index.html에서 쓰일 것입니다.

def create(request): # reservation을 만들어주기 위한 함수
    # Q2-2
    # 2) POST 방식으로 요청이 들어왔을 때
    if request.method == 'POST':
        form=ReservationForm(request.POST) #form을 ReservationForm과 함께 넘어온 data로 구현해주고
        if form.is_valid(): # 유효성 검사를 합니다.
            form.save() # valid하다면, form을 저장해준 뒤
            return redirect('reservations:index') # reservations:index로 redirect 해줍니다.

    # 1) GET 방식으로 요청이 들어왔을 때
    else:
        form = ReservationForm() # form을 ReservationForm으로 구현해주고
    context={ # context에 form 내용을 넣어줍니다.
        'form':form
    }
    return render(request,'reservations/create.html',context) # form을 reservations/create.html 경로로 넘겨줍니다.
