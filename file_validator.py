import os.path


class FileValidator(object):

    def __init__(self, new_file):
        self.file = new_file

    def file_extension_check(self):
        (file_dir, extension) = os.path.splitext(self.file)

        if extension != '.txt':
            return False
        else:
            return True

    def check_plant(self):
        try:
            with open(self.file, "r") as file:
                contents = file.read()
                if contents.startswith('@startuml') and contents.endswith('@enduml'):
                    return True
                else:
                    return False

        except FileNotFoundError:
            print("File Does not Exist")

    def check(self):
        if self.check_plant():
            if self.file_extension_check():
                return True
            else:
                return False
        else:
            return False