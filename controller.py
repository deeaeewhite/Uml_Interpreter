import file_interpreter
import view


class Controller:

    def __init__(self):
        self.view = view.View()

    def go_starter(self):

        a = input('Enter File: ')
        a_file = file_interpreter.Interpreter(a)
        a_file.load()

        self.view.say("Finished.")
