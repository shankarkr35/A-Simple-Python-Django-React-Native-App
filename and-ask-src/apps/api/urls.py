from django.contrib import admin
from django.urls import path,include
from . import views
from .views import * 

urlpatterns = [
     path('employee-login', EmployeeLoginView.as_view(), name='employee-login'),
     path('sectors',Sectors.as_view(),name="sectors")

]
   