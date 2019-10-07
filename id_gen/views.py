from django.shortcuts import render
from .calculations import calc
from .forms import IdUpload
from .forms import IdGenerate


# from django.http import response

# Create your views here.
def home(request):
    return render(request, 'home.html', context={'title': 'ID Tools Home'})


def upload_ids(request):
    context = {'form': IdUpload(),
                'title':'ID Validator'}
    if request.method == 'POST':
        form = IdUpload(request.POST)
        if form.is_valid():
            result = calc.find_ids(request.POST['text'])
            result2 = calc.validate_ids(result)
            context = {'form': form,
                       'title':'ID validator',
                       'result': result2}
    return render(request, 'id_upload.html', context=context)


def generate_ids(request):
    context = {'form': IdGenerate(),
               'title':'ID Generator'}
    if request.method == 'GET':
        form = IdGenerate(request.GET)
        if form.is_valid():
            result3 = calc.create_id(request.GET['text'])
            context = {'form': form,
                       'title':'ID Generator',
                       'result': result3}
    return render(request, 'id_generate.html', context=context)
