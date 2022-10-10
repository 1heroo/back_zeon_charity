from django.contrib import admin
from .models import *
# Register your models here.


class MyUserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'last_name')
    list_display_links = ('pk', 'first_name', 'last_name')


admin.site.register(MyUser, MyUserAdmin)
