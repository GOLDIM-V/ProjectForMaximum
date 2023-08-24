from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout

# Create your views here.

@login_required(login_url=reverse_lazy('login'))
def profile_views(request):
    user = authenticate(request, username=request.user.username, password=request.user.password)
    context = {'name': request.user.username,
               'user_is_authenticate': user is not None,
               }
    return render(request, 'app_auth/profile.html', context)

def login_view(request):
    redirect_url = reverse('profile')
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect(redirect_url)
        else:
            return render(request, 'app_auth/login.html', {'user_is_authenticate': True})
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(redirect_url)
    return render(request, 'app_auth/login.html', {'error': 'Пользователь не найден',
                                                   'user_is_authenticate': True})

def logout_view(request):
    logout(request)
    return redirect(reverse('login'))