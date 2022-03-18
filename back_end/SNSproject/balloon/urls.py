from django.urls import include, path
from .views import *
from rest_framework_jwt.views import obtain_jwt_token

app_name = 'balloon'

urlpatterns = [
    path('get/', GetTestAPI.as_view()),
    # path('viewing/', )
    path('test/', HelloWorld.as_view()),

    # path('categories/', CategoryListAPIView.as_view()),
    path('posts/', PostListAPIView.as_view()),
    path('auth/', obtain_jwt_token),
]