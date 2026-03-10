from django.shortcuts import render
from core.serializer import StudentSerializer
from core.models import Student
from rest_framework.generics import ListAPIView

# Create your views here.
class TokenJob(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_queryset(self):
        user = self.request.user
        return Student.objects.filter(passby = user)

