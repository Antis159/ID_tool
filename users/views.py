from django.shortcuts import render, redirect
from .forms import NewUserCreationForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages


# Create your views here.
def register(request):
    context = {'form': NewUserCreationForm(),
               'purpose': 'Register',
               'title': 'ID Validator'}
    if request.method == 'POST':
        form = NewUserCreationForm(request.POST)
        context['form'] = form
        if form.is_valid():
            form.save()
            return redirect('login-page')

    return render(request, 'login_register.html', context=context)


@login_required
def update_user(request):
    context = {'form': UserUpdateForm(instance=request.user),
               'purpose': 'Update Data',
               'title': 'Update User'}
    return render(request, 'login_register.html', context=context)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.warning(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'login_register.html', {
        'form': form,
        'purpose': 'Update Password'
    })
