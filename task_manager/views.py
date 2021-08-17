from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from task_manager.models import Task, Tag
from task_manager.serializers import (
    TagSerializer,
    TaskDetailSerializer,
    TaskSerializer, TagDetailSerializer,
)

# Tasks Views -->
from task_manager.service import TaskFilter


class TaskListView(generics.ListAPIView):
    """This endpoint list all of the available tasks from the database"""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TaskFilter


class TaskDetailView(APIView):
    """Get task"""

    def get(self, request, pk):
        task = Task.objects.get(id=pk)
        serializer = TaskDetailSerializer(task)
        return Response(serializer.data)


class CreateTaskView(APIView):
    """This endpoint allows for creation of a task"""

    def post(self, request):
        task = TaskSerializer(data=request.data)
        if task.is_valid():
            tags_list = request.data.get('tags')
            for id in tags_list:
                tag = Tag.objects.filter(id=id).prefetch_related('task').first()
                task_tag = tag._prefetched_objects_cache['task']
                for _task in task_tag:
                    if request.data.get('priority') == _task.priority:
                        return Response({'status': 400, 'message': 'tag have such priority'})
            task.save()
            return Response({'status': 201, 'message': 'created'})
        return Response({'status': 400, 'message': 'invalid data'})


class UpdateTaskView(APIView):
    """This endpoint allows for updating a specific task by passing in the id of the task to update"""

    def put(self, request, pk):
        task = Task.objects.get(id=pk)
        data = request.data
        if task.status == 'BG' and data['status'] == 'DN':
            return Response(status=400)
        elif task.status == 'IP' and data['status'] == 'BG':
            return Response(status=400)
        elif task.status == 'DN' and data['status'] == 'IP':
            return Response(status=400)
        task.title = data['title']
        task.description = data.get('description', None)
        task.created = data['created']
        task.priority = data['priority']
        task.status = data['status']
        task.updated = data['updated']
        task.tags.set(data['tags'])
        task.save()
        serializer = TaskSerializer(task)
        return Response(serializer.data)

# <-- Tasks Views

# Tags Views -->

class TagListView(generics.ListAPIView):
    """Get list of tags"""
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDetailView(APIView):
    """Get tag"""

    def get(self, request, pk):
        tag = Tag.objects.get(id=pk)
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
