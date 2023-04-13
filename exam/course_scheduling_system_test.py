import unittest
from unittest.mock import Mock,patch
from course_scheduling_system import CSS

class CSSTest(unittest.TestCase):            
        # test q1_1
        @patch('course_scheduling_system.CSS.check_course_exist')
        def test_q1_1(self,mock_check_course_exist):
            self.css = CSS()
            def fake_check_course_exist(course):
                return True
            mock_check_course_exist.side_effect = fake_check_course_exist
            self.css.add_course(course = ('Math', 'Monday', 1, 2))
            self.assertEqual(self.css.get_course_list(), [('Math', 'Monday', 1, 2)])
        
        # test q1_2
        @patch('course_scheduling_system.CSS.check_course_exist')
        def test_q1_1(self,mock_check_course_exist):
            self.css = CSS()
            def fake_check_course_exist(course):
                return True
            mock_check_course_exist.side_effect = fake_check_course_exist
            self.css.add_course(course = ('Math', 'Monday', 1, 2))
            self.assertEqual(self.css.add_course(course = ('English', 'Monday', 2, 4)), False)
            self.assertEqual(self.css.get_course_list(), [('Math', 'Monday', 1, 2)])

        # test q1_3
        @patch('course_scheduling_system.CSS.check_course_exist')
        def test_q1_1(self,mock_check_course_exist):
            self.css = CSS()
            def fake_check_course_exist(course):
                return False
            mock_check_course_exist.side_effect = fake_check_course_exist
            self.assertEqual(self.css.add_course(course = ('Math', 'Monday', 1, 2)), False)
            self.assertEqual(self.css.get_course_list(), [])
        
        # test q1_4
        @patch('course_scheduling_system.CSS.check_course_exist')
        def test_q1_1(self,mock_check_course_exist):
            self.css = CSS()
            def fake_check_course_exist(course):
                return True
            mock_check_course_exist.side_effect = fake_check_course_exist
            self.assertRaises(TypeError, self.css.add_course, course = ('Math', 'Monday', 1, 2, 3))
            self.assertRaises(TypeError, self.css.add_course, course = (0, 'Monday', 1, 2))
            self.assertRaises(TypeError, self.css.add_course, course = ('Math', 'MoMday', 1, 2))
            self.assertRaises(TypeError, self.css.add_course, course = ('Math', 'Monday', -1, 2))
        
        # test q1_5 Let check_course_exist return True by mocking. Try to add three courses that don’t overlapp with each other and then remove the second one by remove_course, verify the result, and then check the call count of check_course_exist. Also, try to print out the schedule in a formatted way.
        @patch('course_scheduling_system.CSS.check_course_exist')
        def test_q1_5(self,mock_check_course_exist):
            self.css = CSS()
            def fake_check_course_exist(course):
                return True
            mock_check_course_exist.side_effect = fake_check_course_exist
            self.css.add_course(course = ('Math', 'Monday', 1, 2))
            self.css.add_course(course = ('English', 'Monday', 3, 4))
            self.css.add_course(course = ('Science', 'Tuesday', 1, 2))
            self.css.remove_course(course = ('English', 'Monday', 3, 4))
            self.assertEqual(self.css.get_course_list(), [('Math', 'Monday', 1, 2), ('Science', 'Tuesday', 1, 2)])
            self.assertEqual(mock_check_course_exist.call_count, 4)
            print(self.css.__str__())

        # test q1_6 
        @patch('course_scheduling_system.CSS.check_course_exist')
        def test_q1_6(self,mock_check_course_exist):
            # line 46, 56
            self.css = CSS()
            def fake_check_course_exist(course):
                return False
            mock_check_course_exist.side_effect = fake_check_course_exist
            self.assertEqual(self.css.add_course(course = ('Math', 'Monday', 1, 2)), False)
            self.assertEqual(self.css.remove_course(course = ('Math', 'Monday', 1, 2)), False)

            # line 49, 58
            self.css = CSS()
            def fake_check_course_exist(course):
                return True
            mock_check_course_exist.side_effect = fake_check_course_exist
            self.assertEqual(self.css.add_course(course = ('Math', 'Monday', 1, 2)), True)
            self.assertEqual(self.css.add_course(course = ('Algo', 'Monday', 1, 2)), False)
            self.assertEqual(self.css.remove_course(course = ('Algo', 'Monday', 1, 2)), False)

if __name__ == "__main__":
    unittest.main()