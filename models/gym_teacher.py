from .teacher import SchoolTeacher


# TODO Task2.1: This class inherits from parent class: SchoolTeacher
class GymTeacher(SchoolTeacher):

    # paramterized constructor: initializes class parameters name, xxx
    def __init__(self, name, sport) -> None:
        # super() is a function call to the constructor of the parent class.
        # (hint: check the parent class constructor definition.)
        super().__init__(name=name)
        self.sport = sport

    # function to fetch class parameter values
