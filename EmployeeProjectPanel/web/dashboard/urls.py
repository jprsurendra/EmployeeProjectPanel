from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
	url(r'^$', TemplateView.as_view(template_name='dashboard/dashboard.html')),
	url(r'^projects$', TemplateView.as_view(template_name='dashboard/projects.html')),
]