from django.contrib import admin
from django.urls import path, include

from .views import PostView, PostIdView, ProfileView, AboutView, ContactsView, Test404, AdminView, SetView, GetView, \
    index

urlpatterns = [
    path('posts', PostView),
    path('post/<int:id>', PostIdView, name='post'),
    path('profile/', ProfileView, name='profile'),
    path('about', AboutView, name='about'),
    path('contacts', ContactsView, name='contacts'),
    path('test404', Test404, name='404'),
    path('access', AdminView, name='admin'),
    path('set/', SetView, name='set'),
    path('get/', GetView, name='set'),
    path('json', index, name='index')
]