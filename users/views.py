from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm
from django.contrib import messages

def ProfileView(request):
    all_profile = Profile.objects.all
    return render(request, 'users/profile.html', {'profile':all_profile})

def JoinView(request):
    if request.method == "POST":
        form = ProfileForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            passwd = request.POST['passwd']


            messages.success(request, ('There was an error in your form! Please try again'))
            return render(request, 'join.html', {
                'fname':fname,
                'lname':lname,
                'email':email,
                'passwd':passwd,
            })

        messages.success(request, ('Your Form Has Been Submitted Sucessfully'))
        return redirect('ProfileView')


    else:
        return render(request, 'users/join.html', {})