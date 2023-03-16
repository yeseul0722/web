from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')


def new(request):
    return render(request, 'articles/new.html')

def create(request):

    title = request.Get.get('title')
    content = request.Get.get('content')

    # ORM
    # class.manager.queryAPI
    # Article.objects.create()

    # 3가지 방법이 있다.
    # 1. article instance 생성하는 방법
    article = Article()
    return render(request, 'articles/create.html')