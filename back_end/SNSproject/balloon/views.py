from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status, viewsets, filters
from rest_framework import permissions
from rest_framework.response import Response

from rest_framework.decorators import api_view

from rest_framework import generics
from django.contrib.auth import get_user_model
from .models import Post, Category
from .serializers import CategorySerializer, PostSerializer

class GetTestAPI(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        return Response(data={'status': 'Hello World!'}, status=status.HTTP_200_OK)





class HelloWorld(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        return Response(data={'status': 'Wow! Hello World!'}, status=status.HTTP_200_OK)



class CategoryListAPIView(generics.ListAPIView):
    """カテゴリモデルの取得（一覧）APIクラス"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostListAPIView(generics.ListAPIView):
    """投稿モデルの取得（一覧）APIクラス"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer