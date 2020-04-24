from django.db import models

# Create your models here.
class Reservation(models.Model): # Reservation 모델을 선언해줍니다.
    date = models.DateField() # date를 datefield로 받습니다.
    personnel = models.IntegerField() # personnel은 intergerfield로 받습니다.
    location = models.CharField(max_length=20) # location은 charfield로 받습니다.

# Q3-1
class Reply(models.Model): # (Reservation) 1 : N (Reply) 구조를 위한 Reply class를 선언해 줍니다.
    comment = models.TextField() # comment는 textfield로 받습니다.
    reservation=models.ForeignKey(Reservation,on_delete=models.CASCADE)
    # Foreignkey를 이용해서 Reservation과 1:N 관계설정을 합니다.
    # on_delete=models.CASCADE를 작성해 줌으로써 부모 테이블의 데이터(reservation)가 삭제되었을 때 자식 데이터(comment)도 삭제되게 해줍니다.
