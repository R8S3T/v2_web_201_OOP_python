from views.school_teachers import SchoolTeachers
from models.teacher import SchoolTeacher


class TestSchoolTeachers:

    # 2.3 fetch data for all teachers (test)
    def test_fetch_all_teacher_data(self):
        teacher = SchoolTeacher(name="Sarah Flanigan")
        teacher_list = SchoolTeachers()
        teacher_list.enroll_teacher(teacher)
        all_teacher = teacher_list.fetch_all_teacher_data()
        assert len(all_teacher) == 1
        assert teacher in all_teacher

    # 2.4 fetch data via teacher name (test)
    def test_fetch_data_with_teacher_name(self):
        teacher = SchoolTeacher(name="Bob Builder")
        teacher_list = SchoolTeachers()
        teacher_list.enroll_teacher(teacher)
        a_teacher = teacher_list.fetch_data_with_teacher_name(teacher.name)
        assert teacher in a_teacher
