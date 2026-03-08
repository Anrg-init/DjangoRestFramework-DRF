from django.urls import path, include
from core import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('studentapi/', views.StudentModelviewset, basename='student')

urlpatterns = [
    path('', include(router.urls))
]
