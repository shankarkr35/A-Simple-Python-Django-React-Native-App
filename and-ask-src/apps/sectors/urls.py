from django.urls import path,include
from . import views

urlpatterns = [
    path('sector-management/',views.Sectors.index,name="sector-management"),
    path('add-sector/',views.Sectors.add,name="add-sector"), 
    path('create-sector/',views.Sectors.create, name="create-sector"),
    path('edit-sector/<int:id>',views.Sectors.edit,name="edit-sector"), 
    path('update-sector/',views.Sectors.update, name="update-sector"), 
    path('delete-sector/',views.Sectors.delete, name="delete-sector"),
    path('update-status/',views.Sectors.update_status, name="update-status"),
    
]