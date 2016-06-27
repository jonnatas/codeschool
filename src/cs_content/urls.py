from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('^$', views.content_index, name='content_index'),

]
