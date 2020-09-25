from rest_framework import serializers
from .models import Task

# class TaskSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=255)
#     status = serializers.CharField(max_length=255)
#     date = serializers.DateTimeField()

#     def create(self, validated_data):
#         return Task.objects.create(validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.task)
#         instance.status = validated_data.get('status', instance.task)
#         instance.date = validated_data.get('date', instance.date)
#         return instance

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        # fields = ['id', 'name', 'status', 'date']
        fields = '__all__'