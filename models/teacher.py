import string


class SchoolTeacher:

    # parametrized contructor to initialize class variable name.
    def __init__(self, name):
        self.name = name

    # function to get the name of the teacher
    def get_name(self) -> string:
        return self.name
