from rest_framework import status
from rest_framework.views import APIView
from .serializer import StudentSerializer
from .models import Student
from rest_framework.response import Response



class Studentapiview(APIView):

    def get(self,request, format = None):
        s_data = Student.objects.all()
        serializer =  StudentSerializer(s_data, many=True)
        return Response(serializer.data)
    
    
    def post(self, request, format=None):
        data = request.data
        serializer = StudentSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            res = {'msg':'added succesfully'}
            return Response(res)
        return Response(serializer.errors)
    
    def put(self, request, pk, format=None):
        id = pk
        data = request.data
        s_data = Student.objects.get(id = pk)
        serializer = StudentSerializer(s_data, data = data)


        if serializer.is_valid():
            serializer.save()
            res = {'msg':'added succesfully'}
            return Response(res)
        return Response(serializer.errors)
    
    def delete(self,request,pk,format=None):
        id = pk
        s_data = Student.objects.get(id = pk)
        s_data.delete()

        return Response(
            {'msg':'msss deleted sucessfuly'}
        )
    



    

