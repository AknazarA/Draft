
from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance


class TerminSerializer(serializers.ModelSerializer):

    class Meta:
        model = Termin
        fields = "__all__"

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.abbreviation = validated_data.get('abbreviation', instance.abbreviation)
        instance.longed = validated_data.get('longed', instance.longed)
        instance.category = validated_data.get('category', instance.category)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = "__all__"
