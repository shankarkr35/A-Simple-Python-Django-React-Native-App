from django.contrib import admin
from .models import Employee

class PropertAdmin(admin.ModelAdmin):
    list_display = ["name","email","mobile_number"]
    list_filter = ["email","mobile_number"]


admin.site.register(Employee)
