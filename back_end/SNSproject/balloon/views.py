from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status, viewsets, filters
from django.http import HttpResponse, JsonResponse
from rest_framework import permissions
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view

from rest_framework import generics
from django.contrib.auth import get_user_model
from .models import PostBalloon
from .serializers import PostBalloonSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

class GetTestAPI(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        return Response(data={'status': 'Hello World!'}, status=status.HTTP_200_OK)





class HelloWorld(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        return Response(data={'status': 'Wow! Hello World!'}, status=status.HTTP_200_OK)



# class CategoryListAPIView(generics.ListAPIView):
#     """カテゴリモデルの取得（一覧）APIクラス"""
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


class PostListAPIView(generics.ListAPIView):
    """投稿モデルの取得（一覧）APIクラス"""
    queryset = PostBalloon.objects.all()
    serializer_class = PostBalloonSerializer


class PostBalloonView(viewsets.ModelViewSet):
    queryset = PostBalloon.objects.all()
    serializer_class = PostBalloonSerializer
    """ログイン済みの人だけ投稿できる（現在はオフ）"""
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]


# class PostBalloonView(APIView):
#     @csrf_exempt
#     def snippet_list(request):
#         """
#         List all code snippets, or create a new snippet.
#         """
#         if request.method == 'GET':
#             snippets = PostBalloon.objects.all()
#             serializer = PostBalloonSerializer(snippets, many=True)
#             return JsonResponse(serializer.data, safe=False)
#         elif request.method == 'POST':
#             data = JSONParser().parse(request)
#             serializer = PostBalloonSerializer(data=data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return JsonResponse(serializer.data, status=201)
#             return JsonResponse(serializer.errors, status=400)

#     @csrf_exempt
#     def snippet_detail(request, pk):
#         """
#         Retrieve, update or delete a code snippet.
#         """
#         try:
#             snippet = PostBalloon.objects.get(pk=pk)
#         except PostBalloon.DoesNotExist:
#             return HttpResponse(status=404)

#         if request.method == 'GET':
#             serializer = PostBalloonSerializer(snippet)
#             return JsonResponse(serializer.data)

#         elif request.method == 'PUT':
#             data = JSONParser().parse(request)
#             serializer = PostBalloonSerializer(snippet, data=data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return JsonResponse(serializer.data)
#             return JsonResponse(serializer.errors, status=400)

#         elif request.method == 'DELETE':
#             snippet.delete()
#             return HttpResponse(status=204)