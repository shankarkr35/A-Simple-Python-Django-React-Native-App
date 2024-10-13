from apps.utils import *

class Sectors:
    @auth_middleware 
    def index(request):
        try:
            if request.user.is_authenticated and request.user.is_superuser:
                admin_id = request.user.pkid
            data = Sector.objects.all().order_by('-id')
            records = {
                'list':data,
            }
            return render(request,"backend/sectors/index.html",records)
        except Exception as e:
            return JsonResponse({"status":False,"msg":str(e)})
        
        
    @auth_middleware
    def add(request):
        return render(request,'backend/sectors/add.html')
    
    @auth_middleware
    def create(request):
        if request.method == 'POST': 
            if request.user.is_authenticated and request.user.is_superuser:
                admin_id = request.user.pkid
            title = request.POST.get('name')
            
            if Sector.objects.filter(title = title).exists():
                return JsonResponse({'status':False,'msg':'already exist'})

            else:
                obj = Sector(title=title)
                obj.save()
                return JsonResponse({'status': True,'msg':'Added'})
        else:
            return JsonResponse({'status': False,'msg':'Something Went Wrong'})
        
    @auth_middleware  
    def edit(request,id):
        try:
            record = Sector.objects.get(id=id)
            data = {
                'list':record,
            }
            return render(request,'backend/sectors/edit.html',data)
        except Exception as e:
            return JsonResponse({'status': False,'msg':str(e)})

    @auth_middleware  
    def update(request):
        try:
            if request.method == 'POST':
                if request.user.is_authenticated and request.user.is_superuser:
                    admin_id = request.user.id
                title = request.POST.get('name')
                id = request.POST.get('id')
                
                if Sector.objects.filter(Q(title=title) & ~Q(id=id)).exists():
                    return JsonResponse({'status':False,'msg':'already exist'})
                else:
                    sector = Sector.objects.get(id=id)
                    sector.title = title
                    sector.save()  # This will trigger the AutoSlugField to update the slug

                    return JsonResponse({'status': True, 'msg': 'Updated'})

        except Exception as e:
            return JsonResponse({'status': False,'msg':str(e)})
        
    
    def delete(request):
        try:
            if request.method == 'POST':
                id = request.POST.get('id')
                deleteRecord = Sector.objects.filter(id=id).delete()
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
                updatedRecord = Sector.objects.filter(id=id).update(status=status)
                if updatedRecord is not None:
                    return JsonResponse({'status': True,'msg':'Updated'})
                else:
                    return JsonResponse({'status': False,'msg':'Not Updated'})
        except:
            return JsonResponse({'status': False,'msg':'Something Went Wrong'})