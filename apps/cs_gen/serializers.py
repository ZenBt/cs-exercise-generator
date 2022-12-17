from rest_framework import serializers

from apps.cs_gen.choices import SupportedExerciseType
from apps.cs_gen.services.tasks.base_task import AbstractTask


class ExerciseSerializer(serializers.Serializer):

    task_type = serializers.ChoiceField(choices=SupportedExerciseType.choices)
    amount = serializers.IntegerField()


class OutputExerciseSerializer(serializers.Serializer):

    description = serializers.SerializerMethodField()
    answer = serializers.SerializerMethodField()

    def get_description(self, obj: AbstractTask) -> str:
        return obj.get_description()
    
    def get_answer(self, obj: AbstractTask) -> str:
        return obj.get_answer()

