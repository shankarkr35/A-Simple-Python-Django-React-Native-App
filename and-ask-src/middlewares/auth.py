from django.shortcuts import render,redirect
        
def auth_middleware(get_response):
    # one time integration
    def middleware(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_superuser:
            response = get_response(request, *args, **kwargs)
            return response
        else:
            return redirect('/auth/admin-login')
        
    return middleware

def auth_company_middleware(get_response):
    # one time integration
    def company_middleware(request, *args, **kwargs):
        if request.user.is_authenticated and not request.user.is_superuser:
            response = get_response(request, *args, **kwargs)
            return response
        else:
            return redirect('/company/login/')
    return company_middleware
