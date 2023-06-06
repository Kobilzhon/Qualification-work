from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm


# def profile(request):
#     return render(request, 'auth_user/profile.html')
# # Create your views here.


def sign_up(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        again_password = request.POST.get('again_password')
        if password == again_password:
            if User.objects.filter(username=username).exists():
                return redirect('users-login')
            else:
                if User.objects.filter(email=email).exists():
                    return redirect('users-login')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.first_name = first_name
                    user.last_name = last_name
                    user.save()
                    auth.login(request, user)
                    return redirect('users-login')
        else:
            return redirect('users-sign-up')
    else:
        return render(request, 'users/sign_up.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            redirect('users-login')
    return render(request, 'users/login.html')


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST or None, instance=request.user)
        p_form = ProfileUpdateForm(request.POST or None,
                                   request.FILES or None, instance=request.user.profilemodel)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            redirect('users-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profilemodel)
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'users/profile.html', context)












