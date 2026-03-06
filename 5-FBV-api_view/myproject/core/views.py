from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import StudentSerializer
from .models import Student
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@api_view(['GET'])
def get_data(request):
    if request.method == 'GET':
        data = Student.objects.all()
        serializer = StudentSerializer(data, many=True)
        return Response(serializer.data)
    

@csrf_exempt
@api_view(['POST'])
def create_data(request):
    if request.method == 'POST':
        data = request.data
        serializer = StudentSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data added successfully'}
            return Response(res)
        return Response(serializer.errors)


@csrf_exempt
@api_view(['PUT', 'PATCH'])
def update_data(request, pk):
    if request.method == 'PUT' or request.method == 'PATCH':
        data = request.data
        s_data = Student.objects.get(id = pk)
        serializer = StudentSerializer(s_data, data = data, partial = True)
        
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data update successfulllu'}
            return Response(res)
        return Response(serializer.errors)



@api_view(['DELETE'])
def delete_data(request, pk):
    if request.method == 'DELETE':
        s_data = Student.objects.get(id = pk)
        s_data.delete()

        res = {'msg': 'data deleted sxxfully'}
        return Response(res)




    


