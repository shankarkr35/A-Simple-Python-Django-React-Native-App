from django.contrib import admin
from .models import Sector

class Sectors(admin.ModelAdmin):
    list_display = ["title"]
    list_filter = ["title"]


admin.site.register(Sector)