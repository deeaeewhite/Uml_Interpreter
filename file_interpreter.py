import class_grabber
import file_validator


class Interpreter(object):
    file = ''
    file_contents = []
    my_classes = []
    str = ''
    rel = []
    fin = ''
    partner = ''

    def __init__(self, file):
        self.file = file
        self.dict = {}

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
        temp_fin = ''

        for line in self.file_contents:

            if 'class' in line and '{\n':
                temp = line.split(' ')
                self.my_classes.append(temp[1])
                # print(self.my_classes)
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

    def load(self):
        file_validate = file_validator.FileValidator(new_file=self.file)
        if file_validate.check():
            self.read_file()
            self.data_parser()
            # print(self.dict)
            # print(self.rel)
            self.get_details()
        else:
            print("Incorrect File")

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

    def get_details(self):

        for x, y in self.dict.items():
            a_class = class_grabber.ClassGrabber(new_class_name=x, new_data=y)
            # print(a_class.methods)

            if self.get_rel(a_class.class_name.replace("{", "")):
                a_class = class_grabber.ClassGrabber(new_class_name=x, new_data=y)
                print("import ", self.partner, "\n\n")
                print("class", a_class.class_name.replace("{", ":"))
                print("\tdef __init__(self, ", self.partner.lower(), ":", self.partner, "):\n")

                for line in a_class.attrib:
                    if 'all' in line:
                        print("\t\tself." + line.strip(" ") + " = []")
                    elif 'int' in line:
                        print("\t\tself." + line.strip(" ") + " = 0")
                    else:
                        print("\t\tself." + line.strip(" "))
                print("\n")

                for line in a_class.methods:
                    if line == '':
                        continue
                    if a_class.check_ret(line):
                        r = line.split(" ")

                        # print(r)
                        print("\tdef", r[1].strip(" "), "->", r[0].strip(" "), ": \n")
                    else:
                        a_class.return_val = "None"
                        print("\tdef", line.strip(" "), "-> None: \n")

            else:
                print("class", a_class.class_name.replace("{", ":"))

                print("\tdef __init__(self):\n\t")

                for line in a_class.attrib:
                    if 'all' in line:
                        print("\t\tself." + line.strip(" ") + " = []")
                    elif 'int' in line:
                        print("\t\tself." + line.strip(" ") + " = 0")
                    else:
                        print("\t\tself." + line.strip(" "))
                print("\n")

                for line in a_class.methods:
                    # print(a_class.check_ret(line))
                    if line == '':
                        continue
                    if a_class.check_ret(line):
                        r = line.split(" ")
                        while True:
                            try:
                                r.remove('')
                            except ValueError:
                                break
                        # print(r)
                        print("\tdef", r[1].strip(" "), "->", r[0].strip(" "), ": ")
                    elif line == "\n":
                        break

                    else:
                        a_class.return_val = "None"
                        print("\tdef", line.strip(" "), "-> None: ")
                    print("\t\tpass \n")

            print("# =========================================================================\n")