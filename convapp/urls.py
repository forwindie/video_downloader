from django.conf.urls import url
from convapp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]