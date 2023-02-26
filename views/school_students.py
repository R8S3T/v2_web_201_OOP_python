# This class is used to store/maintain the collection of students in the school.
class SchoolStudents:

    # constructor for the class
    # initilizes the class variable enroll_students to an empty list
    def __init__(self):
        self.enrolled_students = []

    # func to add a student to the list of enrolled students
    def enroll_student(self, student):
        self.enrolled_students.append(student)

    #  func to print out the details of all enrolled students
    def all_students(self):
        for each_student in self.enrolled_students:
            print("Name :" + each_student.name)

    # TODO Task1.1:implement a func to get all students' data
    def fetch_all_student_data(self):
        return self.enrolled_students

    # TODO Task1.2:implement a function get student with name
    def fetch_data_with_student_name(self, student_name):
        new_list = [student for student in self.enrolled_students if student.name == student_name]
        return new_list
