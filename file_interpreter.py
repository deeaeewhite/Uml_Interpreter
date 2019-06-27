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
        self.result = []

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

    def data_parser(self):
        count = 0
        class_count = 0
        temp_str = ''

        for line in self.file_contents:

            if 'class' in line and '{\n':
                temp = line.split(' ')
                self.my_classes.append(temp[1])
                class_count += 1
                count = 1
                continue

            elif '}\t\n' in line or '}\n' in line:
                count = 0

            if count == 1:
                temp_str += ''.join(line)

            else:
                self.fin = temp_str
                self.dict[self.my_classes[class_count-1]] = self.fin

                temp_str = ''

        return self.dict

    def get_rel(self, class_name):

        has_rel = False

        self.partner = ''

        for x in self.rel:
            temp_x = x.split(" ")
            if class_name == temp_x[2]:
                self.partner = temp_x[0]
                has_rel = True

            else:
                has_rel = False

            if has_rel is True:
                break

        return has_rel