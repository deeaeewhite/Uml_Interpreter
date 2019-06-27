import file_validator
import file_builder


class Interpreter(object):

    def __init__(self, file):
        self.file = file
        self.dict = {}
        self.file_contents = []
        self.my_classes = []
        self.str = ''
        self.rel = []
        self.fin = ''
        self.partner = ''

    def read_file(self):

        with open(self.file, "r") as file:
            contents = file.readlines()
            for line in contents[1:]:
                if line == '@startuml\n' or line == '@enduml':
                    continue  # Takes out the header and footer parts of the txt file
                if line == '\n':
                    continue  # Takes out the extra lines
                elif "*--" in line.split(" ") or "<|--" in line.split(" ") or "o--" in line.split(" "):
                    self.rel.append(line)
                else:
                    self.file_contents.append(line)  # only adds the vital information to the actual content array

            return self.file_contents

    def load(self):
        file_validate = file_validator.FileValidator(new_file=self.file)

        if file_validate.check():
            file_build = file_builder.FileBuilder(file=self.file)
            self.read_file()
            file_build.data_parser()
            # print(self.dict)
            # print(self.rel)
            file_build.get_details()
        else:
            print("Incorrect File")
