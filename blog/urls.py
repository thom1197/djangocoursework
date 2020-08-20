from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about', views.about_view, name='about'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('gallery', views.gallery_view, name='gallery'),
    path('contact', views.contact_view, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    