from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('studentapi/', views.StudentViewSet, basename='stdapi')

urlpatterns = [
    path('getdata/', views.get_data),

]
