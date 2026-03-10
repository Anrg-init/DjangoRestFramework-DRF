from django.urls import path, include
from core import views
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('studentapi', views.TokenJob, basename='abcd')

urlpatterns = [
    path('', include(router.urls)),
]
