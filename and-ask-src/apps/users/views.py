from apps.utils import *

class Company:
    @auth_middleware 
    def index(request):
        try:
            if request.user.is_authenticated and request.user.is_superuser:
                admin_id = request.user.pkid
            data = User.objects.filter(is_superuser=False).order_by('-pkid')
            records = {
                'list':data,
            }
            return render(request,"backend/companies/index.html",records)
        except Exception as e:
            return JsonResponse({"status":False,"msg":str(e)})
        
        
    @auth_middleware
    def add(request):
        return render(request,'backend/companies/add.html')
    
    @auth_middleware
    def create(request):
        if request.method == 'POST': 
            if request.user.is_authenticated and request.user.is_superuser:
                admin_id = request.user.pkid
            email = request.POST.get('email')
            company_name = request.POST.get('name')
            password = request.POST.get('password')
            
            if User.objects.filter(email = email).exists():
                return JsonResponse({'status':False,'msg':'email already exist'})

            else:
                hashed_password = make_password(password)
                obj = User(company_name=company_name,email=email,username=email,is_superuser=False,password=hashed_password)
                obj.save()
                # Sending the registration email
                subject, from_email, to = 'Register', settings.DEFAULT_FROM_EMAIL, email
                html_content = render_to_string('emails/registration_email.html', {'fullname': company_name,'email':email,'password':password})
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
            record = User.objects.get(pkid=id)
            data = {
                'list':record,
            }
            return render(request,'backend/companies/edit.html',data)
        except Exception as e:
            return JsonResponse({'status': False,'msg':str(e)})

    @auth_middleware  
    def update(request):
        try:
            if request.method == 'POST':
                if request.user.is_authenticated and request.user.is_superuser:
                    admin_id = request.user.id
                company_name = request.POST.get('name')
                email = request.POST.get('email')
                id = request.POST.get('id')
                
                if User.objects.filter(Q(email=email) & ~Q(pkid=id)).exists():
                    return JsonResponse({'status':False,'msg':'email already exist'})
                else:
                    updated = User.objects.filter(pkid=id).update(company_name=company_name,email=email,username=email)
                    if updated:
                        return JsonResponse({'status': True,'msg':'Updated'})

        except Exception as e:
            return JsonResponse({'status': False,'msg':str(e)})
        
    
    def delete(request):
        try:
            if request.method == 'POST':
                id = request.POST.get('id')
                deleteRecord = User.objects.filter(pkid=id).delete()
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
                deleteRecord = User.objects.filter(pkid=id).update(is_active=status)
                if deleteRecord is not None:
                    return JsonResponse({'status': True,'msg':'Updated'})
                else:
                    return JsonResponse({'status': False,'msg':'Not Updated'})
        except:
            return JsonResponse({'status': False,'msg':'Something Went Wrong'})