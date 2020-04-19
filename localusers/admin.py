from django.contrib import admin

# Register your models here.
from .models import LocalUser

admin.site.register(LocalUser)
