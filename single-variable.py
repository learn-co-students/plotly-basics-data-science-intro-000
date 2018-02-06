import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()

#
# class TestDistance(unittest.TestCase):
#     def test_attendance(self):
#         self.assertEqual(attendance(100), 150)
#         self.assertEqual(attendance(50), 75)
#
#     def test_attendance_with_friends(self):
#         self.assertEqual(attendance_with_friends(100), 170)
#         self.assertEqual(attendance_with_friends(50), 70)
#
#     def test_distance_between_students_squared(self):
#         self.assertEqual(marginal_return_on_budget(first_show, second_show), 1.5)
#         self.assertEqual(marginal_return_on_budget(imaginary_third_show, imaginary_fourth_show))
#
#     def test_y_intercept(self):
#         self.assertEqual(y_intercept(shows), 100)
#
#     def test_comedy_show_regression_line(self):
#         self.assertEqual(comedy_show_regression_line(shows, 350), 101.5)
#
#     def test_distance_all(self):
#         first_show = {'budget': 300, 'attendance': 700}
#         second_show = {'budget': 400, 'attendance': 900}
#
#         shows = [first_show, second_show]
#         self.assertEqual(regression_line_two_points(shows, 350), 800)
#
# if __name__ == '__main__':
#     unittest.main()
