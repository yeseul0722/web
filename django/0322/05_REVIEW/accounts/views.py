from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.

#login이라는 행위는 결국 session을 `생성`하는 행위
# Get 요청이 우선이 되어야 한다. -> POST 요청을 보낼 수 있는 페이지가 필요하므로
# POST 요청

def login(request):
    # 인증 절차를 위한 form 태그
    if request.method == 'POST':
        form = AuthenticationForm()
        if form.is_valid():
            # Article
            user = form.get_user()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form
    }

    return render(request, 'accounts/login.html', context)


# db에서 session 정보를 삭제 하는 행위: db를 변동시키는 요청
# POST 요청
# POST 요청에 대한 응답으로 session 정보 삭제 했으면 내 할일 끝
def logout(request):
    # 게시글 삭제 -> 특정 게시글을 찾아서 그 게시글을 삭제
    # 어떠한 유저의 로그인 정보를 삭제 -> 특정 유저
    auth_logout(request)
    # 다른 부서로 이관시켜준다.
    return redirect('accounts:login')