from unittest import TestCase
import class_grabber
import file_validator


class TestRefactoredCode(TestCase):

    def test_file_extension_check1(self):
        self.assertTrue(file_validator.FileValidator("some.txt").
                        file_extension_check())

    def test_file_extension_check2(self):
        self.assertFalse(file_validator.FileValidator("some.doc").
                         file_extension_check())

    def test_file_extension_check3(self):
        self.assertTrue(file_validator.FileValidator("READ.txt").
                        file_extension_check())

    def test_file_extension_check4(self):
        self.assertTrue(file_validator.FileValidator("test.txt").
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
        input_text = "getBlock()"
        expected = 'get_block()'
        x = class_grabber.ClassGrabber(new_class_name="Tester", new_data="()")
        self.assertEqual(x.formatter(input_text), expected)

    def test_formatter2(self):
        input_text = "getBox()"
        expected = 'get_box()'
        x = class_grabber.ClassGrabber(new_class_name="Tester", new_data="()")
        self.assertEqual(x.formatter(input_text), expected)

    def test_formatter3(self):
        input_text = "someMethod()"
        expected = 'some_method()'
        x = class_grabber.ClassGrabber(new_class_name="Tester", new_data="()")
        self.assertEqual(x.formatter(input_text), expected)

    def test_check_ret1(self):
        input_text = "int getWall()"
        expect = True
        x = class_grabber.ClassGrabber(new_class_name="Tester", new_data="()")
        self.assertEqual(x.check_ret(input_text), expect)

    def test_check_ret2(self):
        input_text = "getWall()"
        expect = False
        x = class_grabber.ClassGrabber(new_class_name="Tester", new_data="()")
        self.assertEqual(x.check_ret(input_text), expect)
