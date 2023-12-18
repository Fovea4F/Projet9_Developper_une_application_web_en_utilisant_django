# The line `from django.conf import settings` is importing the `settings` module from the Django
# configuration. The `settings` module contains various settings and configurations for the Django
# project, such as database settings, installed apps, static files configuration, etc.
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from . import forms


def login_page(request):
    formLogin = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        formLogin = forms.LoginForm(request.POST)
        if formLogin.is_valid():
            user = authenticate(
                username=formLogin.cleaned_data['username'],
                password=formLogin.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                message = 'Identifiants invalides'
    return render(request, 'authentication/login.html',
                  context={'form': formLogin, 'message': message})


def signup_page(request):
    form = forms.SignupForm(request.POST)
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentication/signup.html', context={'form': form})


@login_required
def logout_page(request):
    logout(request)
    return redirect('login')


@login_required
def profile_photo_update(request):
    form = forms.UpLoadProfilePhotoForm()
    if request.method == 'POST':
        form = forms.UpLoadProfilePhotoForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save(commit=False)
            # set the avatar to the good user before saving the model
            # user.profile_photo = request.FILES
            # now we can save
            form.save()
            return redirect('home')
    return render(request, 'authentication/profile_photo_update.html', context={'form': form})


@login_required
def follow_users(request):

    follow_form = forms.UserFollowsForm(instance=request.user)
    if request.method == 'POST':
        follow_form = forms.UserFollowsForm(request.POST, instance=request.user)
        if follow_form.is_valid():
            follow_form.save()
            return redirect('home')
    context = {'follow_form': follow_form}
    return render(request, 'authentication/follow_user.html', context)
