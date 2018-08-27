from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.views.generic import View
from django.views import generic
from django.contrib.auth import login as auth_login
from django.contrib import messages
from .forms import SignUpForm, UserLoginForm
from django.contrib.auth.models import User


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        # Further validation
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account successfully created')

            return redirect('gallery')

    else:
        form = SignUpForm()

    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)

            if 'next' in request.POST:

                return redirect(request.POST.get('next'))

            else:

                return redirect('gallery')

        else:
            form = UserLoginForm()

        return render(request, 'accounts/signup.html', {'form': form})


def logout_view(request):
    logout(request)

    return redirect('gallery')


def profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile.html', args)

