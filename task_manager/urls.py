from django.urls import path

from task_manager.views import TaskListView, TagListView, TaskDetailView, TagDetailView

urlpatterns = [
    path('task/', TaskListView.as_view(), name='task'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('tag/', TagListView.as_view(), name='tag'),
    path('tag/<int:pk>/', TagDetailView.as_view(), name='tag_detail'),

]
