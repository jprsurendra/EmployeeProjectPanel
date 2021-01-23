from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('web.dashboard.urls')),
    url(r'^emplapi', include('api.employees.urls')),
    url(r'^prjapi', include('api.projects.urls')),
    # url(r'^emplapi/', include(('api.employees.urls', 'employee'), namespace='employee_apis')),
    url(r'^admin/', admin.site.urls),
]
