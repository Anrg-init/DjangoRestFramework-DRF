from django.urls import path
from core import views

urlpatterns = [
    path("api/", views.Studentlist.as_view())
]
