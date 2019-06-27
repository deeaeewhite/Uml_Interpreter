import file_builder
import view


class Controller:

    def __init__(self):
        self.view = view.View()

    def go_starter(self):

        a = input('Enter File: ')
        a_file = file_builder.FileBuilder(a)
        a_file.load()

        self.view.say("Finished.")

