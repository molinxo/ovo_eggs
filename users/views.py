from django.shortcuts import render

def ProfileView(request):
    return render(request, 'users/profile.html')

