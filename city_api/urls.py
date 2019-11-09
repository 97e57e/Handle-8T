from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
# router.register('register-user/', views.UserCreateAPIView)
router.register('province', views.ProvinceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]