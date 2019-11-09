from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
# router.register('register-user/', views.UserCreateAPIView)
router.register('province', views.ProvinceViewSet)
# router.register('borough', views.BoroughList.as_view(), base_name='borough')

urlpatterns = [
    path('', include(router.urls)),
    path('borough/', views.BoroughList.as_view(), name='BoroughList'),
]