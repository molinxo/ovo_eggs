from django.shortcuts import render

def HomeView(request):
    return render(request, 'store/home.html')

def CartView(request):
    return render(request, 'store/cart.html')

def ListView(request):
    return render(request, 'store/list.html')



# Create your views here.
