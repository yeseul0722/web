from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')


def create(request):
    return render(request, 'articles/create.html')


# profile(request, name=name)
def profile(request, name):
    # context 이름은 관념적인것...django가 기본 구조 짤 때 그렇게 이름 지었음
    # 꼭 이 이름일 필요는 없는데, 굳이 다른 이름으로 지을 이유도 없음
    
    context = {
        # key: value
        'name': name
    }
    return render(request, 'articles/profile.html', context)


def info(request, age):
    context = {
        'age': age
    }
    return render(request, 'articles/info.html', context)