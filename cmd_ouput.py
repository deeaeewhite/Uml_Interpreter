from cmd import Cmd
import file_validator
import file_builder
import view
import os


class Output(Cmd):

    def __init__(self):
        Cmd.__init__(self)
        self.intro = "Welcome to UML builder. Press help or ? for command list"
        self.prompt = ">>>"
        self.view = view.View()

    def do_check(self, file):
        """check {file}
            Check file is valid """
        if file:
            fvalid = file_validator.FileValidator(file)
            if fvalid.check():
                self.view.say("File is Valid for extracting")
            else:
                self.view.say("File is incorrect format or "
                              "may not be PlantUML")
        else:
            self.view.say("File not specified a file")

    def do_path(self, path):
        """path {path}
            Specify file path"""
        if os.path.isdir(path):
            os.chdir(path)
            files = os.listdir(path)
            for name in files:
                self.view.say(name)
        else:
            self.view.say("File path does not exist")

    def do_load(self, file):
        """load {file}
            Load the file data """

        if file:
            a_load = file_builder.FileBuilder(file)
            a_load.load()
        else:
            self.view.say("File not specified")

    def do_bye(self):
        """Close program"""
        return True


if __name__ == '__main__':
    Output().cmdloop()
