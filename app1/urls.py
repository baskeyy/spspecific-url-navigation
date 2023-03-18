from django.urls import path
from app1.views import *

app_name='nothing'

urlpatterns=[
    path('harly/',harly,name='harly')
]
