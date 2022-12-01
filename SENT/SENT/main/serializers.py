from rest_framework import serializers

from user.serializers import ProfileRegisterSerializer
from .models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    profile = ProfileRegisterSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ("pk", "profile", "post", "text")


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("post", "text")


class PostSerializer(serializers.ModelSerializer):
    profile = ProfileRegisterSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ("pk", "profile", "title", "published_date",
                  "likes", "color", "comments")


class PostCreateSerializer(serializers.ModelSerializer):
    # image = serializers.ImageField(use_url=True, required=False)

    class Meta:
        model = Post
        fields = ("title", "category")