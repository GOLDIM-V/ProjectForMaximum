from django.contrib import admin
from django.urls import path
from .views import index, top_sellers, advert_post

urlpatterns = [
    path('', index,  name='main-page'),
    path("top-sellers/", top_sellers, name='top-sellers'),
    path('advertisement-post/', advert_post, name='adv-post'),
]