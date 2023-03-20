from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # print(dir(request))
    print('='*30)
    print(request.GET)
    print('='*30)

    title = request.GET.get('title')
    content = request.GET.get('content')

    print(title, content)
    
    # ORM
    # class.manager.queryAPI
    # Article.objects.create()
    return render(request, 'articles/create.html')