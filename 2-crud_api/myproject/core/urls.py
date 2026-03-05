from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_data),
    path("create_data/", views.create_data),
    path("update_data/<int:pk>/", views.update_data),
    path("delete_data/<int:pk>/", views.delete_data),
]
