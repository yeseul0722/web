from django.shortcuts import render
from .forms import ArticleForm

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')


# 게시글 생성 페이지 조회
# 게시글 생성을 위해 DB에 저장
def create(request):
    # 사용자가 어떤 method로 요청을 보냈는지에 따라서 조건 분기
    # GET 요청에 대한 처리 먼저 한다.
    form = ArticleForm()
    return render(request, 'articles/create.html')
