from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index),
    url('^rank/$', views.rank),
    url('^(\d+)/$', views.challenge_list_detail, name='challenge-list-detail'),
]
