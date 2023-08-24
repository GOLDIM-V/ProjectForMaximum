from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import AnonymousUser
from django.urls import reverse, reverse_lazy
from .models import Advert
from .forms import AdvertForm

def index(request):
    if isinstance(request.user, AnonymousUser):
        user_is_authenticate = False
    else:
        user = authenticate(request, username=request.user.username, password=request.user.password)
        user_is_authenticate = user is None
    adverts = Advert.objects.all()
    context = {"adverts": adverts,
               'user_is_authenticate': user_is_authenticate
               }
    return render(request, 'add/index.html', context)


def top_sellers(request):
    if isinstance(request.user, AnonymousUser):
        user_is_authenticate = False
    else:
        user = authenticate(request, username=request.user.username, password=request.user.password)
        user_is_authenticate = user is None
    context = {'user_is_authenticate': user_is_authenticate}
    return render(request, 'add/top-sellers.html', context)


@login_required(login_url=reverse_lazy('login'))
def advert_post(request):
    if request.method == "POST":
        form = AdvertForm(request.POST, request.FILES)
        if form.is_valid():
            advertisment = Advert(**form.cleaned_data)
            advertisment.user = request.user
            advertisment.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AdvertForm()
    if isinstance(request.user, AnonymousUser):
        user_is_authenticate = False
    else:
        user = authenticate(request, username=request.user.username, password=request.user.password)
        user_is_authenticate = user is None
    context = {'form': form,
               'user_is_authenticate': user_is_authenticate
               }
    return render(request, 'add/advertisement-post.html', context)