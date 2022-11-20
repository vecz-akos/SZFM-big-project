from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('rate/', include('rate.urls')),
    path('', include('auth_system.urls'))
]
