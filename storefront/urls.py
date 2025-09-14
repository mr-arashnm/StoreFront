from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin, auth
from django.urls import path, include

admin.site.site_header = "Storefront Admin"
admin.site.index_title = "admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('store/', include('store.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt'))
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
