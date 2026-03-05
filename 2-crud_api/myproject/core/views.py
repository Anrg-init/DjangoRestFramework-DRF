from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import io


def get_data(request):

    if request.method == 'GET':
        data = Student.objects.all()
        serializer = StudentSerializer(data, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type = 'application/json')
    

@csrf_exempt
def create_data(request):

    if request.method == 'POST':
         json_data = request.body
         stream = io.BytesIO(json_data)
         pythondata = JSONParser().parse(stream)
         serializer = StudentSerializer(data = pythondata)

         if serializer.is_valid():
             serializer.save()
             res = {'msg':'data added succesfully'}
             res_json = JSONRenderer().render(res)
             return HttpResponse(res_json, content_type = 'application/json')
         
         res_json = JSONRenderer().render(serializer.errors)
         return HttpResponse(res_json, content_type = 'application/json')
    


@csrf_exempt
def update_data(request, pk):
    if request.method == 'PUT' or request.method == 'PATCH':
        json_data = request.body
        stream = io.BytesIO(json_data)

        python_data = JSONParser().parse(stream)

        student = Student.objects.get(id=pk)
        serializer = StudentSerializer(student, data = python_data, partial=True)

        if serializer.is_valid():
            serializer.save()

            res = {'msg':'updated succssfully'}
            json_res = JSONRenderer().render(res)
            return HttpResponse(json_res, content_type = 'application/json')
        json_res = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_res, content_type='application/json')
    


@csrf_exempt
def delete_data(request, pk):

    if request.method == 'DELETE':
            student = Student.objects.get(id = pk)
            student.delete()

            res = {'msg':'deleted successfully'}
            json_res = JSONRenderer().render(res)
            return HttpResponse(json_res, content_type = 'application/json')
     





         

    