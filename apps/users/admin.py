from django.contrib import admin
from .models import User, Boss, Manager, Hitmen

# Register your models here.
admin.site.register(User)

admin.site.register(Boss)

admin.site.register(Manager)

admin.site.register(Hitmen)