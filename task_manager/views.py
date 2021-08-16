from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from task_manager.models import Task, Tag
from task_manager.serializers import (
    TagListSerializer,
    TaskDetailSerializer,
    TaskListSerializer,
)

# Tasks Views -->
from task_manager.service import TaskFilter


class TaskListView(generics.ListAPIView):
    """This endpoint list all of the available tasks from the database"""
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TaskFilter


class TaskDetailView(APIView):
    """Get task"""

    def get(self, request, pk):
        task = Task.objects.get(id=pk)
        serializer = TaskDetailSerializer(task)
        return Response(serializer.data)


class CreateTaskView(generics.CreateAPIView):
    """This endpoint allows for creation of a task"""

    queryset = Task.objects.all()
    serializer_class = TaskListSerializer


class UpdateTaskView(generics.UpdateAPIView):
    """This endpoint allows for updating a specific task by passing in the id of the task to update"""

    queryset = Task.objects.all()
    serializer_class = TaskListSerializer


# <-- Tasks Views

# Tags Views -->

class TagListView(generics.ListAPIView):
    """Get list of tags"""
    queryset = Tag.objects.all()
    serializer_class = TagListSerializer


class TagDetailView(APIView):
    """Get tag"""

    def get(self, request, pk):
        tag = Tag.objects.get(id=pk)
        serializer = TagListSerializer(tag)
        return Response(serializer.data)


class CreateTagView(generics.CreateAPIView):
    """This endpoint allows for creation of a tag"""

    queryset = Tag.objects.all()
    serializer_class = TagListSerializer


class UpdateTagView(generics.UpdateAPIView):
    """This endpoint allows for updating a specific tag by passing in the id of the tag to update"""

    queryset = Tag.objects.all()
    serializer_class = TagListSerializer

# <-- Tags Views


def home(self):
    tag = Tag.objects.filter(id=1).prefetch_related('task')[0]
    task_tag = tag._prefetched_objects_cache['task']
    for task in task_tag:
        print(task.status)
    return HttpResponse(status=200)