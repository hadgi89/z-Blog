from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class FeedBackSerailizer(serializers.Serializer):
    """Сериализатор 
    формы обратной связи
    """
    name = serializers.CharField()
    email = serializers.CharField()
    subject = serializers.CharField()
    message = serializers.CharField()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('title',)
        lookup_field = 'title'
        extra_kwargs = {
            'url': {'lookup_field': 'title'}
        }


class PostSerializer(serializers.ModelSerializer):

    user = serializers.SlugRelatedField(
        slug_field="user", 
        queryset=User.objects.all(),)
    
    category = serializers.StringRelatedField(
        many=True,)
    
    tags = serializers.SlugRelatedField(
        many=True,
        slug_field="title", 
        queryset=Tag.objects.all(),)
    
    class Meta:
        model = Post
        fields = ('id', 'user', 'category', 'tags', 'is_draft', 'created_at', 'updated_at', 'views', 'post_sourse', 'image', 'title', 'slug', 'desc', 'content')
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class SignupSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "password2",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        username = validated_data["username"]
        password = validated_data["password"]
        password2 = validated_data["password2"]
        if password != password2:
            raise serializers.ValidationError({"password": "Пароли не совпадают"})
        user = User(username=username)
        user.set_password(password)
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    user = serializers.SlugRelatedField(slug_field="username", queryset=User.objects.all())
    post = serializers.SlugRelatedField(slug_field="slug", queryset=Post.objects.all())

    class Meta:
        model = Comment
        fields = ("id", "post", "user", "comment", "created_at")
        lookup_field = 'id'
        extra_kwargs = {
            'url': {'lookup_field': 'id'}
        }