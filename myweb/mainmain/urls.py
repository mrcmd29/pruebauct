from django.contrib import admin
from . import views
from django.urls import path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.base, name='base.html'),
    path('main/', views.main, name='main.html'),   
    path('agenda/', views.agenda, name='agenda.html'),
]