from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
import djoser
from apps.cs_gen.serializers import ExerciseSerializer, OutputExerciseSerializer
from apps.cs_gen.services.exercise_factory import ExerciseTypeFactory

@extend_schema(
    responses={
        201: OutputExerciseSerializer,
    }
)
class ExerciseView(GenericAPIView):
    serializer_class = ExerciseSerializer


    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        factory = ExerciseTypeFactory(serializer.data['task_type'], serializer.data['amount'])
        generator = factory.create_exercise_generator()
        tasks = generator.generate()

        output_serializer = OutputExerciseSerializer(tasks, many=True)

        return Response(output_serializer.data, status=201)
