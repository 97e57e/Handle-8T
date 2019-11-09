from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('register', views.RegistrationAPI, base_name='register')
# router.register('login', views.LoginView, base_name='login')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.LoginView, name='login'),
    path('logout/', views.Logout, name='logout'),
]