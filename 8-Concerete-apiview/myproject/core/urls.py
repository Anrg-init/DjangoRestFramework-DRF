from django.urls import path
from . import views

urlpatterns = [
    path('getdata/', views.StudentList.as_view()),
    path('updatedata/', views.StudentCreate.as_view())
]
