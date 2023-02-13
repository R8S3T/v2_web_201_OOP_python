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
        pass

    # TODO Task1.2: write test for fetch_data_with_student_name()

