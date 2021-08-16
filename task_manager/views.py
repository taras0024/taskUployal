from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from task_manager.models import Task, Tag
from task_manager.serializers import TaskListSerializer, TagListSerializer, TaskDetailSerializer


# Tasks Views -->

class TaskListView(generics.ListAPIView):
    """Get list of tasks"""
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer


class TaskDetailView(APIView):
    """Get task"""

    def get(self, request, pk):
        task = Task.objects.get(id=pk)
        serializer = TaskDetailSerializer(task)
        return Response(serializer.data)


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

# <-- Tags Views
