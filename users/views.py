from django.shortcuts import render, redirect
from .forms import NewUserCreationForm, UserUpdateForm
from django.contrib.auth.decorators import login_required


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
