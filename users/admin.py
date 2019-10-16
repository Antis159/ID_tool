from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group

admin.site.unregister(Group)

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']
    list_display_links = ['username']

admin.site.register(User, UserAdmin)
# Register your models here.
