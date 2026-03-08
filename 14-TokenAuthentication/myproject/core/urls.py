from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core import views
from rest_framework.authtoken.views import ObtainAuthToken


router = DefaultRouter()

router.register('studentapi', views.StudentModelviewset, basename='abcd')


urlpatterns = [
    path('', include(router.urls)),
    path('gettoken/', ObtainAuthToken.as_view())
]
