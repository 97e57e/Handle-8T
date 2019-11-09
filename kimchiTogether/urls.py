from django.contrib import admin
from django.urls import path, include

import accounts_api.urls
import city_api.urls

from rest_framework import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts_api.urls')),
    path('city/', include('city_api.urls')),
    path('rest-auth/', include('rest_auth.urls')),
]
