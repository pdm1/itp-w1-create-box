import unittest

from create_box import create_box,create_outer_box


first_box_expected = """
****
****
****
""".lstrip()

second_box_expected = """
@
""".lstrip()

third_box_expected = """
xxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxx
""".lstrip()

fourth_box_expected = """
!!!!!!!!!
!       !
!       !
!       !
!       !
!!!!!!!!!
""".lstrip()

class TestCreateBox(unittest.TestCase):
    def test_box(self):
        self.assertEqual(create_box(3, 4, '*'), first_box_expected)

    def test_small_box(self):
        self.assertEqual(create_box(1, 1, '@'), second_box_expected)
        
    def test_middle_box(self):
        self.assertEqual(create_box(3,24, 'x'), third_box_expected)
        
    def test_outer_box(self):
        self.assertEqual(create_outer_box(6,9,'!'), fourth_box_expected)

    # Add your own test using third_box_expected
