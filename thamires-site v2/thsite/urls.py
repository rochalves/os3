from django.conf.urls import url
from thsite import views

urlpatterns = [
    url(r'^principal/$', views.principal),
]