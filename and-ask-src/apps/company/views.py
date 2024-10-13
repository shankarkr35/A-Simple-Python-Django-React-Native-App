from apps.utils import *

class AuthCompanyCheck:
    def index(request):
        if request.user.is_authenticated and not request.user.is_superuser:
            return redirect("/company/dashboard/")
        else:
            return render(request,"company/company-login.html")
    
    def login_check(request):
        if request.method == 'POST':
            data = json.loads(request.body)
            email = data.get('username')
            password = data.get('password')
            user = authenticate(email=email,password=password)
            
            if user is not None:
                if(user.is_active == 1):
                    if(not user.is_superuser):
                        login(request, user)
                        return JsonResponse({'success': True,'msg':'logginSCS'})
                    else:
                        return JsonResponse({'success': False,'msg':'NotCompany'})
                else:
                    return JsonResponse({'success': False,'msg':'ACC0'})
            else:
                return JsonResponse({'success': False, 'msg': 'account404'})
        else:
            return JsonResponse({'success': False, 'msg': 'Swrong'})
        
    def signout(request):
        if request.user.is_authenticated and not request.user.is_superuser:
            logout(request)
            return redirect('/company/login/')
        else: 
            return redirect('/company/dashboard/')  

    def company_dashboard(request):
        courier_id = request.user.id
        if request.user.is_authenticated and not request.user.is_superuser:
            return render(request,"company/dashboard.html")
        else:
            return redirect("/company/login/")
        

class Employees:
    @auth_company_middleware 
    def index(request):
        try:
            if request.user.is_authenticated and not request.user.is_superuser:
                company_id = request.user.pkid
            print("My Company Ids is,",company_id)
            data = Employee.objects.filter(user_id = company_id).select_related('user').order_by('-id')
            
            records = {
                'list':data,
            }
            return render(request,"company/employees/index.html",records)
        except Exception as e:
            return JsonResponse({"status":False,"msg":str(e)})
        
        
    @auth_company_middleware
    def add(request):
        return render(request,'company/employees/add.html')
    
    @auth_company_middleware
    def create(request):
        if request.method == 'POST': 
            if request.user.is_authenticated and not request.user.is_superuser:
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
        
    @auth_company_middleware  
    def edit(request,id):
        try:
            record = Employee.objects.get(id=id)
            data = {
                'list':record,
            }
            return render(request,'company/employees/edit.html',data)
        except Exception as e:
            return JsonResponse({'status': False,'msg':str(e)})

    @auth_company_middleware  
    def update(request):
        try:
            if request.method == 'POST':
                if request.user.is_authenticated and not request.user.is_superuser:
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
        



    def import_excel(request):
        if request.user.is_authenticated and not request.user.is_superuser:
            company_id = request.user.pkid

        if request.method == 'POST' and 'importSubmit' in request.POST:
            # Check if a file was uploaded
            file = request.FILES.get('file')
            if file:
                # Validate the file extension
                file_extension = file.name.split('.')[-1].lower()
                
                if file_extension in ['xls', 'xlsx']:
                    try:
                        # Use appropriate engine based on file extension
                        if file_extension == 'xls':
                            df = pd.read_excel(file, engine='xlrd')
                        else:
                            df = pd.read_excel(file, engine='openpyxl')
                        
                        # Loop through the DataFrame and save the data
                        for index, row in df.iterrows():
                            email = row['email']
                            password = str(row['password'])
                            
                            # Check if the email already exists in the database
                            if Employee.objects.filter(email=email).exists():
                                messages.warning(request, f"Duplicate entry for email: {email}")
                                continue  # Skip saving this entry
                            
                            hashed_password = make_password(password)

                            # Save new employee entry to the database
                            Employee.objects.create(
                                name=row['name'],
                                email=email,
                                password=hashed_password,
                                mobile_number= str(row['mobile_number']),
                                user_id=company_id,
                                status=row['status']
                            )

                        messages.success(request, "Employees imported successfully!")
                    except Exception as e:
                        messages.error(request, f"Error occurred while processing the file: {str(e)}")
                else:
                    messages.error(request, "Invalid file format. Please upload an Excel file.")
                
            else:
                messages.error(request, "No file uploaded. Please upload a valid Excel file.")

            return redirect('employee-management')  # Redirect back to the employee list page

        # Get the list of employees to display on the page
        employees = Employee.objects.filter(user_id=company_id).select_related('user').order_by('-id')
        return render(request, 'company/index.html', {'list': employees})

                














            