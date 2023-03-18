from django.urls import path
from app2.views import *

app_name='nothing1'

urlpatterns=[
    path('harly1/',harly1,name='harly1')
]