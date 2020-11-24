from rest_framework import viewsets
from .serializers import StudentSerializer
from .models import Student
# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('age')
    serializer_class  = StudentSerializer