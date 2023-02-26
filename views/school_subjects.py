class SchoolSubjects:
    def __init__(self):
        self.subjects = []

    def enlist_a_subject(self, subject):
        self.subjects.append(subject)

    def view_all_subjects(self):
        return [subject.name for subject in self.subjects]

    def view_subject_syllabus(self, subject_name):
        for subject in self.subjects:
            if subject.name == subject_name:
                return subject.get_syllabus()
        return None
