from django.urls import path
from shopping.views import *
app_name='dress'
urlpatterns=[
    path('dress/',dress,name='dress'),
]