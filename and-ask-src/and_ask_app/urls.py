from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static

urlpatterns = [
    path('supersecret/', admin.site.urls),
    path('api/v1/auth/', include("djoser.urls")),  # Correct this line
    path('api/v1/auth/', include("djoser.urls.jwt")),  # Correct this line
    path('api/v1/profile/', include("apps.profiles.urls")),
    path('api/v1/', include("apps.api.urls")),

    #------Admin-----
    path('auth/', include('apps.authentication.urls')),
    path('auth-v1/', include('apps.users.urls')),
    path('auth-v2/', include('apps.sectors.urls')),
    path('company/', include('apps.company.urls')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = "And Ask Admin"
admin.site.site_title = "And Ask Admin Portal"
admin.site.index_title = "Welcome to And Ask Portal"
