from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^InsertAudio', InsertAudio.as_view(), name='InsertAudio'),
    ]
