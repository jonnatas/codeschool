from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index),
    url('^new/$', views.new, name='new'),
    url('^rank/$', views.rank),
    url('^(\d+)/$', views.challenge_list_detail, name='challenge-list-detail'),
    url('^(\d+)/(\d+)/$', views.challenge_question, name='question-detail'),
]
