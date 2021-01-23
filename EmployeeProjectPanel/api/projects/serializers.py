from rest_framework import serializers
from .models import Project
from ..employees.models import Employee
from ..employees.serializers import EmployeeSerializer


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = fields = ['id', 'name']


class ProjectWithEmployeesSerializer(serializers.ModelSerializer):
    #
    employees = serializers.SerializerMethodField()
    class Meta:
        model = Project
        fields = fields = ['id', 'name']

    def get_employees(self, obj):
        db_list = Employee.objects.filter()
        employees = EmployeeSerializer(data=db_list, fields={'employee_id', 'full_name', 'desgination'}, read_only=True, many=True)
        return employees