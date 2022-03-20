from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import PostBalloon

# ユーザーシリアライザ
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'


# class CategorySerializer(serializers.ModelSerializer):
#     """カテゴリシリアライザ"""
#     class Meta:
#         model = Category
#         fields = ('id', 'name')


# 投稿シリアライザ
class PostBalloonSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostBalloon
        fields = '__all__'

    def create(self, validated_data):
        return PostBalloon.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # instance.id = validated_data.get('id', instance.id)
        instance.author = validated_data.get('author', instance.author)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance
    