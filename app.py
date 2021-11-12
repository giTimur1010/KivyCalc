from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_file("main_train.kv")
Window.size = [380, 620]


class MainScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.first_digit = 0
        self.second_digit = 1
        self.operation = "+"
        self.operand_flag = False

    def add_divisors(self):
        self.label.text = '1, 2, 3, 4, 5,' \
                          ' 6, 9, 10, 12, 15' \
                          ', 18, 20, 25, 30, 36' \
                          ', 45, 50, 60, 75, 90,' \
                          ' 100, 150, 180, 225, 300,' \
                          ' 450, 900'

    def delete(self):
        self.label.text = ""
        self.first_digit = 0
        self.second_digit = 1
        self.operation = "+"

    def add_string(self, btn):
        self.label.text += btn.text
        if btn.text == "=":
            self.second_digit = float((self.label.text[self.label.text.find(self.operation) + 1:-1]))
            if self.operation == "+":
                self.label.text = str(self.first_digit + self.second_digit)
                self.operand_flag = False
            elif self.operation == "-":
                self.label.text = str(self.first_digit - self.second_digit)
                self.operand_flag = False
            elif self.operation == "x":
                self.label.text = str(self.first_digit * self.second_digit)
                self.operand_flag = False
            elif self.operation == "/" and self.second_digit != 0:
                self.label.text = str(self.first_digit / self.second_digit)
                self.operand_flag = False
            else:
                self.label.text = "Error"
        elif not btn.text.isdigit() and not self.operand_flag:
            self.operation = btn.text
            self.first_digit = float(self.label.text[:-1])
            self.operand_flag = True


class CalcApp(App):
    def __init__(self):
        super().__init__()
        self.screen_manager = ScreenManager()
        self.screen_manager.add_widget(main_screen)

    def build(self):
        return self.screen_manager


if __name__ == '__main__':
    main_screen = MainScreen(name="main")

    password_manager = CalcApp()
    password_manager.run()
