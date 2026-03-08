from .models import Student
from .serializer import StudentSerializer
from rest_framework import viewsets
from rest_framework.response import Response



class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        st = Student.objects.all()
        serializer = StudentSerializer(st, many=True)
        return Response(serializer.data)
    
    def create(self,request):
        js_data = request.data
        serializer = StudentSerializer(data = js_data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'create successfully'})
        
    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            st = Student.objects.get(id = id)
            serializer = StudentSerializer(st)
            return Response(serializer.data)
        
    def update(self, request, pk):
        dt = request.data
        st = Student.objects.get(id = pk)
        serializer = StudentSerializer(st, data = dt)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'updated successfully'})
        
        
    def destroy(self,request,pk):
        st = Student.objects.get(id = pk)
        st.delete()
        return Response({'msg': 'deleted successfully'})
    



        
    

    

        


