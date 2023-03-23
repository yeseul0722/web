from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_POST
from django.shortcuts import redirect

@require_POST
def delete(request):
    if request.user.is_authenticated:
        auth_logout(request)
        request.user.delete()
    return redirect('articles:index')
