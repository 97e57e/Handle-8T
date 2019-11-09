from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('post-list/<int:borough>', views.PostList.as_view(), name='PostList'),
]