from rest_framework import serializers

from task_manager.models import Tag, Task


class TagSerializer(serializers.ModelSerializer):
    """List of tags"""

    class Meta:
        model = Tag
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    """List of Task"""

    class Meta:
        model = Task
        fields = "__all__"


class TaskDetailSerializer(serializers.ModelSerializer):
    """Task"""

    tags = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)

    class Meta:
        model = Task
        fields = "__all__"
