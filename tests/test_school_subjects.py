from models.subject import SchoolSubject
from views.school_subjects import SchoolSubjects


class TestSchoolSubjects:
    def test_enlist_a_subject(self):
        subjects = SchoolSubjects()

        # Create subject and add it to the SchoolSubjects instance
        math = SchoolSubject("Math")
        math.put_syllabus("Algebra", 1)
        math.put_syllabus("Geometry", 2)
        subjects.enlist_a_subject(math)

        # Verify that subject was added to the SchoolSubjects instance
        assert math in subjects.subjects

    def test_view_all_subjects(self):
        subjects = SchoolSubjects()
        math = SchoolSubject("Math")
        physics = SchoolSubject("Physics")
        subjects.enlist_a_subject(math)
        subjects.enlist_a_subject(physics)

        assert set(subjects.view_all_subjects()) == {"Math", "Physics"}

    def test_view_subject_syllabus(self):
        # Create subject and add syllabus
        subjects = SchoolSubjects()
        math = SchoolSubject("Math")
        math.put_syllabus("Algebra", 1)
        math.put_syllabus("Geometry", 2)
        subjects.enlist_a_subject(math)

        # Check that it's the correct syllabus
        assert subjects.view_subject_syllabus("Math") == {1: "Algebra", 2: "Geometry"}
