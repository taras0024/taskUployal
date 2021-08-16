from django_filters import rest_framework as filters

from task_manager.models import Task


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class TaskFilter(filters.FilterSet):
    status = CharFilterInFilter(field_name='status', lookup_expr='in')
    priority = CharFilterInFilter(field_name='priority', lookup_expr='in')

    class Meta:
        model = Task
        fields = ['status', 'priority',]