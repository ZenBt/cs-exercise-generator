from apps.cs_gen.choices import SupportedExerciseType


class UnsupportedTypeError(Exception):
    
    def __init__(self, unsupported_t: int) -> None:
        self.unsupported_t = unsupported_t
        
        super().__init__(
            f"Recieved type: {unsupported_t} is not a valid option. \n"
            f"Choices are {[k for k, v in SupportedExerciseType.choices]}"
            )
