from django.core.exceptions import ObjectDoesNotExist
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from task_manager.models import Task, Tag
from task_manager.serializers import (
    TagSerializer,
    TaskDetailSerializer,
    TaskSerializer, TagDetailSerializer,
)
from task_manager.service import TaskFilter


# Tasks Views -->

class TaskListView(generics.ListAPIView):
    """This endpoint list all of the available tasks from the database"""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TaskFilter


# class TaskDetailView(APIView):
#     """Get task"""
#     def get(self, request, pk):
#         try:
#             task = Task.objects.get(id=pk)
#             serializer = TaskDetailSerializer(task)
#             return Response(serializer.data)
#         except ObjectDoesNotExist:
#             return Response(['Element with this ID not found'], status=404)
#         # ---------------
#         task = get_object_or_404(Task, id=pk)
#         serializer = TaskDetailSerializer(task)
#         return Response(serializer.data)

class TaskDetailView(generics.RetrieveAPIView):
    """Get task"""
    queryset = Task
    serializer_class = TaskDetailSerializer


class CreateTaskView(APIView):
    """This endpoint allows for creation of a task"""

    def post(self, request):
        task = TaskSerializer(data=request.data)
        if task.is_valid(raise_exception=True):
            task.save()
            return Response(status=201)
        return Response(status=400)


class UpdateTaskView(generics.RetrieveUpdateAPIView):
    """This endpoint allows for updating a specific task by passing in the id of the task to update"""

    queryset = Task.objects.all()
    serializer_class = TaskSerializer


# <-- Tasks Views

# Tags Views -->

class TagListView(generics.ListAPIView):
    """Get list of tags"""
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDetailView(APIView):
    """Get tag"""

    def get(self, request, pk):
        tag = get_object_or_404(Tag, id=pk)
        serializer = TagDetailSerializer(tag)
        return Response(serializer.data)


class CreateTagView(generics.CreateAPIView):
    """This endpoint allows for creation of a tag"""

    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class UpdateTagView(generics.RetrieveUpdateAPIView):
    """This endpoint allows for updating a specific tag by passing in the id of the tag to update"""

    queryset = Tag.objects.all()
    serializer_class = TagSerializer

# <-- Tags Views
