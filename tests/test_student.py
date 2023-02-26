from models.student import Student


class TestStudent:
    def test_calculate_year_of_birth_happy_case(self):
        st = Student(name="Test name", age=29, class_number=2)
        assert st.calculate_year_of_birth(2023) == 1994

    def test_calculate_year_of_birth_happy_case(self):
        current_year = 2023
        student = Student(name="Anni", age=35, class_number=2)
        year_of_birth = student.calculate_year_of_birth(current_year)
        assert year_of_birth == 1988
