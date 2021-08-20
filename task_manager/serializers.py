from rest_framework import serializers
from rest_framework.response import Response

from task_manager.models import Tag, Task


class TagSerializer(serializers.ModelSerializer):
    """List of tags"""

    class Meta:
        model = Tag
        fields = "__all__"


class TagDetailSerializer(serializers.ModelSerializer):
    """Tag"""

    task = serializers.StringRelatedField(many=True)

    class Meta:
        model = Tag
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    """List of Task"""

    class Meta:
        model = Task
        fields = "__all__"

    # def validate(self, data):
    #     tags = data.get('tags')
    #     for tag in tags:
    #         tag_obj = Tag.objects.filter(id=tag.id).prefetch_related('task').first()
    #         tasks = tag_obj._prefetched_objects_cache['task']
    #         for task in tasks:
    #             if data.get('priority') == task.priority:
    #                 raise serializers.ValidationError({'error': 'such priority already exist'})
    #     return data

    def create(self, data):
        tags = data.get('tags')
        for tag in tags:
            tasks = Task.objects.filter(tags=tag.id)
            for task in tasks:
                if data.get('priority') == task.priority:
                    raise serializers.ValidationError({'error': 'such priority already exist'})

        new_task = Task(title=data['title'], description=data.get('description', None), priority=data['priority'],
                        status=data['status'])
        new_task.save()
        new_task.tags.set(data['tags'])
        return data

    def update(self, instance, data):
        if instance.status == 'BG' and data['status'] == 'DN':
            raise serializers.ValidationError({'error': 'wrong ordering of changing data'})
        elif instance.status == 'IP' and data['status'] == 'BG':
            raise serializers.ValidationError({'error': 'wrong ordering of changing data'})
        elif instance.status == 'DN' and data['status'] == 'IP':
            raise serializers.ValidationError({'error': 'wrong ordering of changing data'})
        instance.title = data.get('title', instance.title)
        instance.description = data.get('description', instance.description)
        instance.priority = data.get('priority', instance.priority)
        instance.status = data.get('status', instance.status)
        instance.tags.set(data.get('tags', instance.tags))
        instance.save()
        return instance


class TaskDetailSerializer(serializers.ModelSerializer):
    """Task"""

    tags = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)

    class Meta:
        model = Task
        fields = "__all__"
