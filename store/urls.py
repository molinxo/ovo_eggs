from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView, name='HomeView'),
    path('list', views.ListView, name='ListView'),
    path('cart', views.CartView, name='CartView')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
