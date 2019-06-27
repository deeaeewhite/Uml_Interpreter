import class_grabber
import file_validator
from file_interpreter import Interpreter


class FileBuilder(Interpreter):
    def __init__(self, file):
        super().__init__(file)
        self.final = ""

    def get_details(self):
        for x, y in self.dict.items():
            a_class = class_grabber.ClassGrabber(new_class_name=x, new_data=y)

            if self.get_rel(a_class.class_name.replace("{", "")):
                a_class = class_grabber.ClassGrabber(new_class_name=x, new_data=y)
                self.result.append("import " + self.partner + "\n\n\n")
                self.result.append("class " + a_class.class_name.replace("{", ":"))
                self.result.append("\tdef __init__(self, " + self.partner.lower() + ":" + self.partner + "):\n")

                for line in a_class.attrib:
                    x = "\t\tself." + line.strip(" ")
                    if 'all' in line:
                        self.result.append(x + " = []" + "\n")
                    elif 'int' in line:
                        self.result.append(x + " = 0" + "\n")
                    else:
                        self.result.append(x + "\n")
                self.result.append("\n")

                for line in a_class.methods:
                    if line == '':
                        continue
                    if a_class.check_ret(line):
                        r = line.split(" ")

                        self.result.append("\tdef " + r[1].strip(" ") + "->" + r[0].strip(" ") + ": \n")
                    else:
                        a_class.return_val = "None"
                        self.result.append("\tdef " + line.strip(" ") + "-> None: \n")
                    self.result.append("\t\tpass \n")

            else:
                self.result.append("class " + a_class.class_name.replace("{", ":"))

                self.result.append("\tdef __init__(self):\n")

                for line in a_class.attrib:
                    x = "\t\tself." + line.strip(" ")
                    if 'all' in line:
                        self.result.append(x + " = []" + "\n")
                    elif 'int' in line:
                        self.result.append(x + " = 0" + "\n")
                    else:
                        self.result.append(x + "\n")
                self.result.append("\n")

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
                        self.result.append("\tdef " + r[1].strip(" ") + "->" + r[0].strip(" ") + ": " + "\n")
                    elif line == "\n":
                        break

                    else:
                        a_class.return_val = "None"
                        self.result.append("\tdef " + line.strip(" ") + "-> None: " + "\n")
                    self.result.append("\t\tpass \n")

            self.result.append("# =========================================================================\n")

        # returns new output
        for i in self.result:
            self.final = self.final + i
        print(self.final)

    def load(self):
        file_validate = file_validator.FileValidator(new_file=self.file)
        if file_validate.check():
            self.read_file()
            self.data_parser()
            self.get_details()
        else:
            print("Incorrect File")

