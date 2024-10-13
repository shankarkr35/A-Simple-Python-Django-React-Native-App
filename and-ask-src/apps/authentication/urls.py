from django.urls import path,include
from . import views

urlpatterns = [
    path('admin-login',views.AuthAdminCheck.index,name="admin-login"),
    path('login-auth/',views.AuthAdminCheck.login_check,name="login-auth"),
    path('signout/',views.AuthAdminCheck.signout,name="signout"),
    path('admin-dashboard/', views.AuthAdminCheck.admin_dashboard, name="admin-dashboard"),

    path('employee-management/',views.Employees.index,name="employee-management"),
    path('add-employee/',views.Employees.add,name="add-employee"), 
    path('create-employee/',views.Employees.create, name="create-employee"),
    path('edit-employee/<int:id>',views.Employees.edit,name="edit-employee"), 
    path('update-employee/',views.Employees.update, name="update-employee"), 
    path('delete-employee/',views.Employees.delete, name="delete-employee"),
    path('update-status/',views.Employees.update_status, name="update-status"),
    
]