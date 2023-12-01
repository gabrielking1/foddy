from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# app_name = 'Myapp'
urlpatterns = [
        path('',views.index, name='index'),
        path('product/', views.product, name='product'),
        path('category/', views.category, name='category'),
        path('food/', views.food, name='food'),

       
]

urlpatterns = urlpatterns+static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)
urlpatterns = urlpatterns+static(settings.STATIC_URL,
document_root=settings.STATIC_ROOT)