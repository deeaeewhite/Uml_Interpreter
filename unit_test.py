from unittest import TestCase
import class_grabber
import file_validator


class TestRefactoredCode(TestCase):

    def test_file_extension_check1(self):
        arrange = "some.txt"
        self.assertTrue(file_validator.FileValidator(arrange).
                        file_extension_check())

    def test_file_extension_check2(self):
        arrange = "some.doc"
        self.assertFalse(file_validator.FileValidator(arrange).
                         file_extension_check())

    def test_file_extension_check3(self):
        arrange = "READ.txt"
        self.assertTrue(file_validator.FileValidator(arrange).
                        file_extension_check())

    def test_file_extension_check4(self):
        arrange = "test.txt"
        self.assertTrue(file_validator.FileValidator(arrange).
                        file_extension_check())

    def test_plant1(self):
        input_file = "READ.txt"
        i = file_validator.FileValidator(input_file)
        self.assertTrue(i.file_extension_check())

    def test_plant2(self):
        input_file = "Rel.txt"
        i = file_validator.FileValidator(input_file)
        self.assertTrue(i.file_extension_check())

    def test_plant3(self):
        input_file = "view.py"
        i = file_validator.FileValidator(input_file)
        self.assertFalse(i.file_extension_check())

    def test_formatter1(self):
        arrange = "getBlock()"
        expected = 'get_block()'
        x = class_grabber.ClassGrabber(new_class_name="Tester", new_data="()")
        self.assertEqual(x.formatter(arrange), expected)

    def test_formatter2(self):
        arrange = "getBox()"
        expected = 'get_box()'
        x = class_grabber.ClassGrabber(new_class_name="Tester", new_data="()")
        self.assertEqual(x.formatter(arrange), expected)

    def test_formatter3(self):
        arrange = "someMethod()"
        expected = 'some_method()'
        x = class_grabber.ClassGrabber(new_class_name="Tester", new_data="()")
        self.assertEqual(x.formatter(arrange), expected)

    def test_check_ret1(self):
        arrange = "int getWall()"
        expect = True
        x = class_grabber.ClassGrabber(new_class_name="Tester", new_data="()")
        self.assertEqual(x.check_ret(arrange), expect)

    def test_check_ret2(self):
        arrange = "getWall()"
        expect = False
        x = class_grabber.ClassGrabber(new_class_name="Tester", new_data="()")
        self.assertEqual(x.check_ret(arrange), expect)
