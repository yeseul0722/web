from django.shortcuts import render

# Create your views here.
def index(requset):
    return render(requset, 'pages/index.html')

def create(requset):
    return render(requset, 'pages/create.html')
