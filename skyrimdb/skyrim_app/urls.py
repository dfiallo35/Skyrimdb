from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('tables/players', views.players, name='players'),
    path('tables/battles', views.battles, name='battles'),
    path('tables/beasts', views.beasts, name='beasts'),
    path('tables/spells', views.spells, name='spells'),
]