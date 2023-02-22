from unittest import TestCase, main
from project.student import Student


class TestStudent(TestCase):

    def setUp(self):
        self.student = Student("TestGuy1")
        self.student_with_course = Student("TestGuy2", {'math': ['some notes']})

    def test_successful_initializing(self):
        self.assertEqual("TestGuy1", self.student.name)
        self.assertEqual({}, self.student.courses)
        self.assertEqual({'math': ['some notes']}, self.student_with_course.courses)

    def test_enroll_successful_append_and_return_for_existing_courses(self):
        result = self.student_with_course.enroll("math", ["one", "two"])
        self.assertEqual({'math': ["some notes", "one", "two"]}, self.student_with_course.courses)
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_enroll_add_note_to_non_existing_course_without_third_parameter(self):
        result = self.student.enroll('python', ['python is really cool'])
        self.assertEqual(['python is really cool'], self.student.courses['python'])
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_add_note_to_non_existing_course_with_third_param_y(self):
        result = self.student.enroll('python', ['python is really cool'], "Y")
        self.assertEqual(['python is really cool'], self.student.courses['python'])
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_new_course_added_without_notes(self):
        result = self.student.enroll('python', ['python is really cool'], "n")
        self.assertEqual([], self.student.courses['python'])
        self.assertEqual("Course has been added.", result)

    def test_add_notes_on_existing_course(self):
        result = self.student_with_course.add_notes('math','thats new note')
        self.assertEqual(['some notes', 'thats new note'], self.student_with_course.courses['math'])
        self.assertEqual("Notes have been updated",result)

    def test_add_notes_to_non_existing_course_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("math", "some note")
        self.assertEqual("Cannot add notes. Course not found.",str(ex.exception))

    def test_leave_existing_course(self):
        result = self.student_with_course.leave_course("math")

        self.assertEqual({}, self.student_with_course.courses)

    def test_leave_non_existing_course_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course('python')

        self.assertEqual("Cannot remove course. Course not found.",str(ex.exception))

if __name__ == "__main__":
    main()
