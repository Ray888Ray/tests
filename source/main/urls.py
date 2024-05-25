import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.routers.accounts_urls')),
    path('api/', include('api.routers.api_main_urls')),
    path('api/auth/', include('api.routers.api_authentication_urls')),
    path('', include('webapp.routers.test_urls')),
    path('__debug__/', include(debug_toolbar.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
