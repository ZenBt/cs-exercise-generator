from io import UnsupportedOperation
from apps.cs_gen.choices import SupportedExerciseType
from apps.cs_gen.services.exceptions import UnsupportedTypeError
from apps.cs_gen.services.exercise_generators.base_generator import AbstractExerciseGenerator
from apps.cs_gen.services.exercise_generators.encoding_task import EncodingExerciseTaskGenerator
from apps.cs_gen.services.exercise_generators.path_task import PathExerciseTaskGenerator


class ExerciseTypeFactory:
    
    def __init__(self, selected_type: SupportedExerciseType, amount: int) -> None:
        self._type = selected_type
        self._amount = amount
    
    
    def create_exercise_generator(self) -> AbstractExerciseGenerator:
        exercise_gen_class = self._get_exercise_gen_class()
        exercise_gen = exercise_gen_class(self._amount)

        return exercise_gen
    

    def _get_exercise_gen_class(self):
        
        match self._type:
            
            case SupportedExerciseType.ENCODING_TASK:
                return EncodingExerciseTaskGenerator
            
            case SupportedExerciseType.PATH_TASK:
                return PathExerciseTaskGenerator
            
            case _:
                raise UnsupportedTypeError(self._type)