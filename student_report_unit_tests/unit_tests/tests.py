from unittest import TestCase, main
from student_report_unit_tests.student_report_card import StudentReportCard


class StudentReportCardTests(TestCase):
    def setUp(self) -> None:
        self.student = StudentReportCard("Anabel", 1)

    def test_init(self):
        name = "Anabel"
        year = 1
        student = StudentReportCard(name, year)

        self.assertEqual(name, student.student_name)
        self.assertEqual(year, student.school_year)
        self.assertEqual({}, student.grades_by_subject)

    def test_student_name_if_empty_string_raise(self):
        with self.assertRaises(ValueError) as err:
            StudentReportCard("", 1)
        self.assertEqual("Student Name cannot be an empty string!", str(err.exception))

    def test_if_school_year_invalid_raise(self):
        with self.assertRaises(ValueError) as err:
            StudentReportCard("Anabel", -1)

        with self.assertRaises(ValueError) as err:
            StudentReportCard("Anabel", 0)

        with self.assertRaises(ValueError) as err:
            StudentReportCard("Anabel", 13)

        self.assertEqual("School Year must be between 1 and 12!", str(err.exception))

    def test_school_year_edge_case_equal_12(self):
        name_1 = "Anabel"
        first_student_year = 12
        student = StudentReportCard(name_1, first_student_year)
        name_2 = "Ana"
        second_student_year = 1
        student_2 = StudentReportCard(name_2, second_student_year)
        self.assertEqual(12, student.school_year)
        self.assertEqual(1, student_2.school_year)

    def test_add_grade_if_subject_not_in_grades_by_subject(self):
        subject = "math"
        grade = 5.6
        self.student.grades_by_subject[subject] = [grade]
        self.assertEqual({"math": [5.6]}, self.student.grades_by_subject)
        self.assertEqual(1, len(self.student.grades_by_subject))

    def test_add_grade_if_subject_in_grades_by_subject(self):
        self.student.add_grade("math", 5.0)
        self.student.add_grade("math", 6.0)
        self.assertEqual({"math": [5.0, 6.0]}, self.student.grades_by_subject)
        self.assertEqual(1, len(self.student.grades_by_subject))

    def test_average_grade_by_subject(self):
        self.student.grades_by_subject = {"Math": [5.00, 6.00], "English": [6.00, 6.00]}
        expected = f"Math: 5.50\n" +\
         f"English: 6.00"

        actual = self.student.average_grade_by_subject()
        self.assertEqual(expected, actual)

    def test_average_grade_for_all_subjects(self):
        self.student.grades_by_subject = {"Math": [5.00, 6.00], "English": [6.00, 6.00]}
        expected = f"Average Grade: 5.75"

        self.assertEqual(expected, self.student.average_grade_for_all_subjects())

    def test_repr_if_returns_proper_string(self):
        self.student.grades_by_subject = {"Math": [5.00, 6.00], "English": [6.00, 6.00]}
        result = f"Name: {self.student.student_name}\n" \
                 f"Year: {self.student.school_year}\n" \
                 f"----------\n" \
                 f"{self.student.average_grade_by_subject()}\n" \
                 f"----------\n" \
                 f"{self.student.average_grade_for_all_subjects()}"

        expected = repr(self.student)
        self.assertEqual(expected, result)

if __name__ == "__main__":
    main()




