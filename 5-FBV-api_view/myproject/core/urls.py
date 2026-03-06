from django.urls import path
from . import views

urlpatterns = [
    path('getdata/', views.get_data),
    path('createdata/', views.create_data),
    path('updatedata/<int:pk>/', views.update_data),
    path('deletedata/<int:pk>/', views.delete_data)   
]
