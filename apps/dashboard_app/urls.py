from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^/chat/(?P<label>[\w]{6})/$', views.chat_room),
    url(r'^/chat$', views.chat),
    #url(r'^$', views.dashboard),
]