from django.shortcuts import render, redirect
from django.contrib.auth import logout


# Главная страница приложения
def main_view(request):
    return render(request, 'index.html')


# Представление для авторизированных юзеров
def get_authentificated_view(request):
    # немного глупо, но из-за фейла с гуглом спешил
    if request.user.is_authenticated:
        context = {
            'name': request.user.get_full_name()
        }
        return render(request, 'authentificated.html', context)
    else:
        return render(request, 'not_authentificated.html')


def logout_from_app(request):
    logout(request)
    return redirect('/')
