from django.urls import path
from food.views import *
app_name='nonveg'
urlpatterns=[
    path('nonveg/',nonveg,name='nonveg'),
]