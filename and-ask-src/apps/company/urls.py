from django.urls import path,include
from . import views

urlpatterns = [
    path('login/',views.AuthCompanyCheck.index,name="login"),
    path('login-auth/',views.AuthCompanyCheck.login_check, name='login-auth'),
    path('dashboard/',views.AuthCompanyCheck.company_dashboard, name='dashboard'),
    path('logout/',views.AuthCompanyCheck.signout, name='logout'),

    path('employee-management/',views.Employees.index,name="employee-management"),
    path('add-employee/',views.Employees.add,name="add-employee"), 
    path('create-employee/',views.Employees.create, name="create-employee"),
    path('edit-employee/<int:id>',views.Employees.edit,name="edit-employee"), 
    path('update-employee/',views.Employees.update, name="update-employee"), 
    path('delete-employee/',views.Employees.delete, name="delete-employee"),
    path('update-status/',views.Employees.update_status, name="update-status"),
    path('import/', views.Employees.import_excel, name='import_excel'),
    

    # ------- Forgot Password -----
    # path('forgot-password/',views.ResetPassword.index, name='forgot-password'),
    # path('courier-email-check/',views.ResetPassword.courier_email_check, name='courier-email-check'),
    # path('reset-password/',views.ResetPassword.resetPass, name='reset-password'),
    # path('verify-otp-and-reset-password/', views.ResetPassword.verify_otp_and_reset_password, name='verify_otp_and_reset_password'),
    
    
]