from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about', views.about_view, name='about'),
    path('posts', views.posts_view, name='posts'),
    path('gallery', views.gallery_view, name='gallery'),
    path('contact', views.contact_view, name='contact'),
]