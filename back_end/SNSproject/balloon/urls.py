from django.urls import include, path
from .views import *

app_name = 'balloon'

urlpatterns = [
    path('get/', GetTestAPI.as_view()),
    # path('viewing/', )
]