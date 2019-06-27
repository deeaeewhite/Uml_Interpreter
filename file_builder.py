import class_grabber


class FileBuilder(object):

    def __init__(self, file):
        self.file = file
        self.dict = {}
        self.file_contents = []
        self.my_classes = []
        self.str = ''
        self.rel = []
        self.fin = ''
        self.partner = ''

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

    def get_details(self):

        for x, y in self.dict.items():
            a_class = class_grabber.ClassGrabber(new_class_name=x, new_data=y)

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
                    if line == '':
                        continue
                    if a_class.check_ret(line):
                        r = line.split(" ")
                        while True:
                            try:
                                r.remove('')
                            except ValueError:
                                break
                        print("\tdef", r[1].strip(" "), "->", r[0].strip(" "), ": ")
                    elif line == "\n":
                        break

                    else:
                        a_class.return_val = "None"
                        print("\tdef", line.strip(" "), "-> None: ")
                    print("\t\tpass \n")

            print("# =========================================================================\n")
