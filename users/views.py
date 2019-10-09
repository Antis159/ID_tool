from django.shortcuts import render
from .forms import NewUserCreationForm


# Create your views here.
def register(request):
    context = {'form': NewUserCreationForm(),
               'purpose': 'Register',
               'title': 'ID Validator'}
    if request.method =='POST':
        form=NewUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'login_register.html', context=context)
