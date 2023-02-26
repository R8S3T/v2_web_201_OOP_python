from views.school_subjects import SchoolSubjects
from models.subject import SchoolSubject


class TestSchoolSubject:
    # Check correct subject name is returned
    def test_get_subject_name(self):
        subject = SchoolSubject(name="Physics")
        assert subject.get_name() == "Physics"

    def test_put_syllabus(self):
        subject = SchoolSubject(name="Gymnastics")
        subject.put_syllabus(chapter_name="Gymnastics", chapter_number=1)
        assert subject.get_syllabus()[1] == "Gymnastics"
