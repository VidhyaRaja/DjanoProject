from django.contrib import admin
from .models import Sin1

# Register your models here.
class Sin1Admin(admin.ModelAdmin):
    list_display = ["name", "userID", "site"]

admin.site.register(Sin1, Sin1Admin)
