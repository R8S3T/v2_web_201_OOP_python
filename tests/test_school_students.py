from views.school_students import SchoolStudents
from models.student import Student


class TestSchoolStudents:

    # TODO Task1.0: write test
    def test_enroll_student(self):
        student = Student(name="Jyotsna", age=29, class_number=3)
        studentList = SchoolStudents()
        studentList.enroll_student(student)
        assert len(studentList.enrolled_students) == 1

    # TODO Task1.1: write test
    def test_fetch_all_student_data(self):
        student = Student(name="Anni", age=35, class_number=2)
        student_list = SchoolStudents()
        student_list.enroll_student(student)
        all_studis = student_list.fetch_all_student_data()
        assert len(all_studis) == 1
        assert student in all_studis

    # TODO Task1.2: write test for fetch_data_with_student_name()
    def test_fetch_data_with_student_name(self):
        student = Student(name="Anni", age=35, class_number=2)
        student_list = SchoolStudents()
        student_list.enroll_student(student)
        a_student = student_list.fetch_data_with_student_name(student.name)
        assert student in a_student


