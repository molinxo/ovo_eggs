from django.shortcuts import render
from .models import Carousel

def HomeView(request):
    obj = Carousel.objects.all()
    context = {
        'obj':obj
    }
    return render(request, 'store/home.html', context)

def CartView(request):
    return render(request, 'store/cart.html')

def ListView(request):
    return render(request, 'store/list.html')

def ProfileView(request):
    return render(request, 'store/profile.html')


# Create your views here.
