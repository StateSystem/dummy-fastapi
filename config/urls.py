from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import path


def home(request):
    user = request.session.get('user')
    if user:
        return HttpResponse(f'logged-in:{user}')
    return HttpResponse('logged-out')


def login(request):
    request.session['user'] = 'tester'
    return redirect('/')


urlpatterns = [
    path('', home),
    path('login', login),
]
