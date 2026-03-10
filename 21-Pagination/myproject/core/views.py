from django.shortcuts import render
from core.models import Student
from core.serializer import StudentSerializer
from rest_framework.generics import ListAPIView

# Create your views here.
class Studentlist(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    