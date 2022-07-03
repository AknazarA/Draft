from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from .forms import *

from django.shortcuts import render

from drf_spectacular.utils import extend_schema

from rest_framework import viewsets


# def bad_request(request, exception=None):
#     return render(request, "404.html", {"form": form})


class CategoryViewSet(viewsets.ViewSet):

    template_category = "category.html"

    @extend_schema(request=None, responses=CategorySerializer)
    def list(self, request):
        if request.GET.get('name'):
            queryset = Category.objects.filter(name__contains=request.GET['name'])
        else:
            queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)

        form = serializer.data
        if form == []:
            form = [{'name': "No results"}]
            # print(form)

        create_form = CategoryForm(None)
        return render(request, self.template_category, {"form": form, "create_form": create_form})


    @extend_schema(request=CategorySerializer, responses=CategorySerializer)
    def create(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return self.list(request)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(request=None, responses=CategorySerializer)
    def retrieve(self, request, pk=None):
        draft = Termin.objects.filter(category=pk)
        posts = Post.objects.filter(category=pk, posttype='post')
        tools = Post.objects.filter(category=pk, posttype='tool')


        termins_serializer = TerminSerializer(draft, many=True)
        posts_serializer = PostSerializer(posts, many=True)
        tools_serializer = PostSerializer(tools, many=True)

        context = {"termins": termins_serializer.data, "posts": posts_serializer.data, "tools": tools_serializer.data}

        return render(request, 'draft_list.html', context)

    @extend_schema(request=CategorySerializer, responses=CategorySerializer)
    def partial_update(self, request, pk=None):
        queryset = Category.objects.get(id=pk)
        serializer = CategorySerializer(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        Category.objects.get(id=pk).delete()
        return Response('Category was deleted')


class TerminViewSet(viewsets.ViewSet):

    template_category = "termin_list.html"

    @extend_schema(request=None, responses=TerminSerializer)
    def list(self, request):
        if request.GET.get('title'):
            queryset = Termin.objects.filter(title__startswith=request.GET['title']).order_by('title')
        else:
            queryset = Termin.objects.all().order_by('title')
        serializer = TerminSerializer(queryset, many=True)

        context = {"form": serializer.data}
        return render(request, self.template_category, context)


    @extend_schema(request=TerminSerializer, responses=TerminSerializer)
    def create(self, request):
        serializer = TerminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Termin is created', status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(request=None, responses=TerminSerializer)
    def retrieve(self, request, pk=None):
        draft = Termin.objects.get(id=pk)
        serializer = TerminSerializer(draft)


        context = {'form': serializer.data}
        return render(request, 'termin.html', context)


    @extend_schema(request=TerminSerializer, responses=TerminSerializer)
    def partial_update(self, request, pk=None):
        queryset = Termin.objects.get(id=pk)
        serializer = TerminSerializer(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        Termin.objects.get(id=pk).delete()
        return Response('Termin was deleted')


class PostViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        post = Post.objects.get(id=pk)
        serializer = PostSerializer(queryset)
        return Response(serializer.data)

    def create(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Post is created', status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)