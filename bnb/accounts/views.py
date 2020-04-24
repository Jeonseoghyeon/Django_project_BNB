from django.shortcuts import render, redirect # redirect 기능 구현을 위해 해당 경로에서 redirect를 불러옵니다
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # login, signup을 위해 해당 경로에서 UserCreationForm, AuthenticationForm을 불러옵니다.
from django.contrib.auth import login as auth_login # login 기능 구현을 위해 login을 불러오되, views.py 내 함수와 이름이 겹치지 않도록 auth_login으로 불러옵니다.
from django.contrib.auth import logout as auth_logout # logout 기능 구현을 위해 logout을 불러오되, views.py 내 함수와 이름이 겹치지 않도록 auth_logout으로 불러옵니다.
# 각 문제를 해결하기 위하여 필요한 import문은 이곳에 작성합니다.

def index(request): # index 페이지로 돌아가기 위한 함수
    return render(request, 'accounts/index.html') # index 페이지로 render해줍니다.

def signup(request): # signup 하기 위한 함수
    if request.method == 'POST': # 2) request 방식이 POST이라면 (Form에 signup을 위한 데이터가 넘어왔을 때)
        form = UserCreationForm(request.POST) # 해당 데이터로 form에 저장해 줍니다.
        if form.is_valid(): # 이후 유효성 검사를 진행합니다.
            form.save() # valid 하다면 form을 저장해준 뒤
            return redirect('accounts:index') # accounts:index로 redirect 해줍니다.
    else: # 1) request 방식이 GET이라면
        form = UserCreationForm() # form에 UserCreationForm을 구현해주고
    context = { # context 내에 넣어줍니다.
        'form':form
    }
    return render(request, 'accounts/form.html',context) # 그 후에 해당 정보를 accounts/form.html 경로로 넘겨줍니다.


def login(request): # login을 하기 위한 함수
    if request.method == 'POST':# 2) request 방식이 POST이라면 (Form에 login을 위한 데이터가 넘어왔을 때)
        form = AuthenticationForm(request,request.POST) # 해당 데이터로 form에 저장해 줍니다. (페이지 정보와 데이터 정보 두가지를 받아옵니다.)
        if form.is_valid(): # 이후 유효성 검사를 진행합니다.
            auth_login(request,form.get_user()) #valid 하다면 위에서 불러온 login에 form에서의 user 정보를 받아옵니다.
            return redirect('accounts:index') # accounts:index로 redirect 해줍니다.

    else: # 1) request 방식이 GET이라면
        form = AuthenticationForm() # form에 AuthenticationForm을 구현해주고
    context={ # context 내에 넣어줍니다.
        'form':form
    }
    return render(request, 'accounts/form.html', context) # 그 후에 해당 정보를 accounts/form.html 경로로 넘겨줍니다.


def logout(request): # logout을 하기 위한 함수
    auth_logout(request) # 위에서 불러온 logout함수를 통해 logout을 해줍니다.
    return redirect('accounts:index') # 로그아웃 후에 accounts:index로 redirect 해줍니다.