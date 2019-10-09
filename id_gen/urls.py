from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name='home-page'),
    path('id-upload', views.upload_ids, name='upload-ids'),
    path('id-generate', views.generate_ids, name='generate-ids'),
]