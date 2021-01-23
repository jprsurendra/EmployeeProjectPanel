from rest_framework.response import Response
from rest_framework import viewsets

from .models import Employee
from .serializers import EmployeeSerializer


class AuthorModelViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all() # SELECT * FROM tbl_authors
    serializer_class = EmployeeSerializer