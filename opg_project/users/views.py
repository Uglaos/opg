from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileForm, ReadOnlyProfileForm


def home(request):
    return render(request, 'users/home.html', {'title': 'Početna stranica'})


def register(request):
    if request.method == 'POST':
        u_form = UserRegisterForm(request.POST)
        p_form = ProfileForm(request.POST)
        if u_form.is_valid() and p_form.is_valid():
            user = u_form.save()
            profile = p_form.save(commit=False)
            profile.user = user
            profile.save()
            username = u_form.cleaned_data.get('username')
            messages.success(request, f'Vaš račun {username} je kreiran!')
            return redirect('login')
    else:
        u_form = UserRegisterForm()
        p_form = ProfileForm()

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'title': 'Registracija korisnika i OPG-a',
    }
    return render(request, 'users/register.html', context)


@login_required()
def profile(request):
    if request.method == 'POST':
        p_form = ProfileForm(request.POST, instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Vas račun je ažuriran!')
            return redirect('profile')
    else:
        p_form = ProfileForm(instance=request.user.profile)

    context = {
        'p_form': p_form,
        'title': 'Editiranje profila',
    }
    return render(request, 'users/edit_profile.html', context)


@login_required()
def profile_readonly(request):
    p_form = ReadOnlyProfileForm(instance=request.user.profile)
    context = {
        'p_form': p_form,
        'title': 'Pregled profila'
    }
    return render(request, 'users/profile.html', context)

