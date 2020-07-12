from django.urls import path
from . import views





urlpatterns = [
    path('', views.index, name='Home'),
    path('about', views.about, name='About-us'),
    path('services', views.services, name='Services'),
    path('portfolio', views.portfolio, name='Portfolio'),
    path('login', views.login, name='login'),




]
