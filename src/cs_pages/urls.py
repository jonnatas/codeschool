from django.conf.urls import url
from cs_pages import views

urlpatterns = [
    url(r'^send-input-block/$', views.send_input_block.as_view())
]
