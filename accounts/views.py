from django.shortcuts import render, redirect
from .forms import SignupForm, UserActivateForm
from .models import Profile, UserPhoneNumber, UserAddress
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            myform = form.save(commit=False)
            myform.active = False
            myform.save()
            profile = Profile.objects.get(user__username=username)
            send_mail(
                subject = "Activate your account",
                 message = f"use this code {profile.code} to activate your account",
                from_email = settings.EMAIL_HOST_USER,
                recipient_list = [email,],
                fail_silently=False,
            )
            return redirect(f'/accounts/{username}/activate')

    else:
        form = SignupForm()

    return render(request, 'registration/register.html', {'form':form})

def user_activate(request,username):
    profile = Profile.objects.get(user__username=username)
    if request.method== 'POST':
        form = UserActivateForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            if profile.code == code:
                profile.code_used = True
                profile.save()
                return redirect('/accounts/login')

    else:
        form = UserActivateForm()
    return render(request,  'registration/activate.html', {'form':form})

def profile(request):
    profile = Profile.objects.get(user=request.user)
    user_address = UserAddress.objects.filter(user=request.user)
    user_number = UserPhoneNumber.objects.filter(user=request.user)
    return render(request, 'registration/profile.html', {'profile':profile, 'user_address':user_address, 'user_number':user_number})