from django.conf.urls import url
from rest_framework import routers

from api.employees.views import EmployeeModelViewSet

router = routers.DefaultRouter()
router.register(r'project', EmployeeModelViewSet)

urlpatterns = [
]
urlpatterns += router.urls

# app_name = 'projects'