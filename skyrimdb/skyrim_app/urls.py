from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('tables/players', views.players, name='players'),
    path('tables/battles', views.battles, name='battles'),
    path('tables/beasts', views.beasts, name='beasts'),
    path('tables/spells', views.spells, name='spells'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
