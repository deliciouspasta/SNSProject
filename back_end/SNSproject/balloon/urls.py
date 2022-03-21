from django.urls import include, path
from .views import *
from rest_framework_jwt.views import obtain_jwt_token
from .serializers import PostBalloonSerializer
from rest_framework import routers

app_name = 'balloon'

router = routers.DefaultRouter()
router.register(r'release', PostBalloonView)
# urlpatterns = router.urls

urlpatterns = [
    path('get/', GetTestAPI.as_view()),
    # path('viewing/', )
    path('test/', HelloWorld.as_view()),

    # path('categories/', CategoryListAPIView.as_view()),
    path('posts/', PostListAPIView.as_view()),
    path('auth/', obtain_jwt_token),
    path('', include(router.urls))
]