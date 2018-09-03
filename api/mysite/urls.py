from django.contrib import admin
from django.urls import path, include
import nested_admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'nested_admin/', include('nested_admin.urls')),
]
