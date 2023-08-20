from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Advert
from .forms import AdvertForm

def index(request):
    adverts = Advert.objects.all()
    context = {"adverts": adverts}
    return render(request, 'index.html', context)

def top_sellers(request):
    return render(request, 'top-sellers.html')

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
    context = {'form': form}
    return render(request, 'advertisement-post.html', context)