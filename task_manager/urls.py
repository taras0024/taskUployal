from django.urls import path

from task_manager.views import (
    TagListView, TagDetailView, CreateTagView, UpdateTagView,
    TaskListView, TaskDetailView, CreateTaskView, UpdateTaskView,
)

urlpatterns = [

    path('task/', TaskListView.as_view(), name='task'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('task/create/', CreateTaskView.as_view(), name='create_task'),
    path('task/update/<int:pk>/', UpdateTaskView.as_view(), name='update_task'),

    path('tag/', TagListView.as_view(), name='tag'),
    path('tag/<int:pk>/', TagDetailView.as_view(), name='tag_detail'),
    path('tag/create/', CreateTagView.as_view(), name='create_tag'),
    path('tag/update/<int:pk>/', UpdateTagView.as_view(), name='update_tag'),

]
