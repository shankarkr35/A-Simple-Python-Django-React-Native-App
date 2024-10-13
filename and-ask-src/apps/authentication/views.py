from apps.utils import *

class AuthAdminCheck:
    def index(request):
        if request.user.is_authenticated and request.user.is_superuser:
            return redirect("/auth/admin-dashboard")
        else:
            return render(request,"backend/admin-login.html")
    
    def login_check(request):
        if request.method == 'POST':
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
                
            user = authenticate(username=username,password=password)
            if user is not None:
                if(user.is_active == 1):
                    if(user.is_superuser == 1):
                        login(request, user)
                        return JsonResponse({'success': True,'msg':'logginSCS'})
                    else:
                        return JsonResponse({'success': False,'msg':'NotAdmin'})
                else:
                    return JsonResponse({'success': False,'msg':'ACC0'})
            else:
                return JsonResponse({'success': False, 'msg': 'account404'})
        else:
            return JsonResponse({'success': False, 'msg': 'Swrong'})
        
    def signout(request):
        if request.user.is_authenticated and request.user.is_superuser:
            logout(request)
            return redirect('/auth/admin-login')
        else:
            return redirect('/auth/admin-login')

    def admin_dashboard(request):
        if request.user.is_authenticated and request.user.is_superuser:
            return render(request,"backend/dashboard.html")
        else:
            return redirect("/auth/admin-login")
        

class Employees:
    @auth_middleware 
    def index(request):
        try:
            if request.user.is_authenticated and request.user.is_superuser:
                admin_id = request.user.pkid
            data = Employee.objects.select_related('user').order_by('-id')
            #data = Driver.objects.all().order_by('-id')
            records = {
                'list':data,
            }
            return render(request,"backend/employees/index.html",records)
        except Exception as e:
            return JsonResponse({"status":False,"msg":str(e)})
        
        
    @auth_middleware
    def add(request):
        return render(request,'backend/employees/add.html')
    
    @auth_middleware
    def create(request):
        if request.method == 'POST': 
            if request.user.is_authenticated and request.user.is_superuser:
                admin_id = request.user.pkid
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            password = request.POST.get('password')
            
            if Employee.objects.filter(email = email).exists():
                return JsonResponse({'status':False,'msg':'email already exist'})

            else:
                hashed_password = make_password(password)
                obj = Employee(name=name,email=email,mobile_number=phone,password=hashed_password,user_id=admin_id,)
                obj.save()
                # Sending the registration email
                subject, from_email, to = 'Register', settings.DEFAULT_FROM_EMAIL, email
                html_content = render_to_string('emails/registration_email.html', {'fullname': name,'email':email,'password':password})
                text_content = strip_tags(html_content)
                email_msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                email_msg.attach_alternative(html_content, "text/html")
                email_msg.send()
                return JsonResponse({'status': True,'msg':'Added'})
        else:
            return JsonResponse({'status': False,'msg':'Something Went Wrong'})
        
    @auth_middleware  
    def edit(request,id):
        try:
            record = Employee.objects.get(id=id)
            data = {
                'list':record,
            }
            return render(request,'backend/employees/edit.html',data)
        except Exception as e:
            return JsonResponse({'status': False,'msg':str(e)})

    @auth_middleware  
    def update(request):
        try:
            if request.method == 'POST':
                if request.user.is_authenticated and request.user.is_superuser:
                    admin_id = request.user.id
                name = request.POST.get('name')
                email = request.POST.get('email')
                phone = request.POST.get('phone')
                id = request.POST.get('id')
                
                if Employee.objects.filter(Q(email=email) & ~Q(id=id)).exists():
                    return JsonResponse({'status':False,'msg':'email already exist'})
                else:
                    updated = Employee.objects.filter(id=id).update(name=name,email=email,mobile_number=phone)
                    if updated:
                        return JsonResponse({'status': True,'msg':'Updated'})

        except Exception as e:
            return JsonResponse({'status': False,'msg':str(e)})
        
    
    def delete(request):
        try:
            if request.method == 'POST':
                id = request.POST.get('id')
                deleteRecord = Employee.objects.filter(id=id).delete()
                if deleteRecord is not None:
                    return JsonResponse({'status': True,'msg':'Deleted'})
                else:
                    return JsonResponse({'status': False,'msg':'Not Deleted'})
        except:
            return JsonResponse({'status': False,'msg':'Something Went Wrong'})

    
    def update_status(request):
        try:
            if request.method == 'POST':
                id = request.POST.get('id')
                status = request.POST.get('status')
                deleteRecord = Employee.objects.filter(id=id).update(status=status)
                if deleteRecord is not None:
                    return JsonResponse({'status': True,'msg':'Updated'})
                else:
                    return JsonResponse({'status': False,'msg':'Not Updated'})
        except:
            return JsonResponse({'status': False,'msg':'Something Went Wrong'})
