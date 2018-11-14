from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'app'

urlpatterns = [
	path('', views.home, name='home'),
	path('vlogin/', views.vlogin, name='vlogin'),
	path('slogin/', views.slogin, name='slogin'),
	path('ssignup/', views.ssignup, name='ssignup'),
	path('vsignup/', views.vsignup, name='vsignup'),
	path('ind/', views.ind, name='ind'),
	path('shg/', views.shg, name='shg'),
	path('vdashboard/', views.vdashboard, name='vdashboard'),
]