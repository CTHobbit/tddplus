from django.conf.urls import url
from assignmentData import views

urlpatterns = [
    url(r'^$', views.home_page, name='home'),
]