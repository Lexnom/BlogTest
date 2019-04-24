from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from auth_person.models import User
from django.http import HttpResponseRedirect
# Create your views here.

err = {'error': 'Неверный логин или пароль!'}

def auth_main(request):
    return render(request, 'auth_person/auth.html')

def get_author(request):
    if request.method == 'POST':
        login = request.POST['login']
        password = request.POST['pas']
        if User.objects.all().filter(login=login, password=password):
            return redirect('blog', foo=login)
        else:
            return render(request, 'auth_person/auth.html', context=err)




