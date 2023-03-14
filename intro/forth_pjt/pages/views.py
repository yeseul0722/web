from django.shortcuts import render

# Create your views here.
def index(request):
    # app_name/templates/app_name/
    # articles/templates/articles/index.html
    # pages/templates/pages/index.html
    context = {
        'num': 50
    }
    return render(request,
                   'pages/index.html',
                   context)

