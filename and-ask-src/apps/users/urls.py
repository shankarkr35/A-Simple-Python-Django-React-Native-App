from django.urls import path,include
from . import views

urlpatterns = [
    path('company-management/',views.Company.index,name="company-management"),
    path('add-company/',views.Company.add,name="add-company"), 
    path('create-company/',views.Company.create, name="create-company"),
    path('edit-company/<int:id>',views.Company.edit,name="edit-company"), 
    path('update-company/',views.Company.update, name="update-company"), 
    path('delete-company/',views.Company.delete, name="delete-company"),
    path('update-status/',views.Company.update_status, name="update-status"),
    
]