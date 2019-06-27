class ClassGrabber(object):

    def __init__(self, new_class_name, new_data):
        self.class_name = new_class_name
        self.details = new_data
        self.methods = []
        self.attrib = []
        self.para = []
        self.return_val = ""
        self.ret = False
        self.new_str = ''
        self.get_details()

    def get_details(self):
        self.attrib = []
        self.methods = []
        temp = self.details.split("\n\t" and "\t" and "\n")

        for line in temp:
            x = line.replace("\t", "")
            if "(" and ")" in line:
                self.append_details(array=self.methods, detail=x)
            else:
                self.append_details(array=self.attrib, detail=x)
        return self.attrib, self.methods

    def append_details(self, array, detail):
        array.append(self.formatter(n=detail))

    # def get_details(self):
    #     temp = self.details.split("\n\t" and "\t" and "\n")
    #
    #     for line in temp:
    #         if "(" and ")" in line or line == "":
    #             self.get_method(line.replace("\t", ""))
    #         else:
    #             self.get_attrib(line.replace("\t", ""))
    #     return self.attrib

    def get_attrib(self, new_attrib):
        temp = self.formatter(new_attrib)
        self.attrib.append(temp)

    def get_method(self, new_method):
        temp = self.formatter(new_method)
        self.methods.append(temp)

    def get_return_val(self, new_val):
        self.return_val = new_val

    def get_para(self, new_para):
        self.para.append(new_para)

    def check_ret(self, method):
        x = method.split("\t")
        if "int" in x[0] or "str" in x[0]:
            self.ret = True
        else:
            self.ret = False
        return self.ret

    def formatter(self, n):
        self.new_str = ''
        char_list = list(n)
        temp_a = []
        for i in char_list:
            if i.isupper():
                temp_a.append('_')
                temp_a.append(i.lower())
            else:
                temp_a.append(i)

        self.new_str = self.new_str.join(temp_a)
        return self.new_str
