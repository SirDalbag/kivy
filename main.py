from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import random


class Generator(GridLayout):
    def __init__(self, **kwargs):
        super(Generator, self).__init__(**kwargs)
        self.cols = 1

        self.lb1 = Label(text="Генератор случайных чисел")
        self.add_widget(self.lb1)

        self.val1 = TextInput(multiline=False, hint_text="Введите минимальное число")
        self.add_widget(self.val1)

        self.val2 = TextInput(multiline=False, hint_text="Введите максимальное число")
        self.add_widget(self.val2)

        self.result = Label(text="Результат:")
        self.add_widget(self.result)

        self.generate = Button(text="Генерировать")
        self.generate.bind(on_press=self.generate_random_number)
        self.add_widget(self.generate)

    def generate_random_number(self, instance):
        try:
            random_number = random.randint(int(self.val1.text), int(self.val2.text))
            self.result.text = f"Результат: {random_number}"
        except ValueError:
            self.result.text = "Ошибка ввода"
        except Exception as error:
            self.result.text = f"Ошибка: {error}"


class MyApp(App):
    def build(self):
        return Generator()


if __name__ == "__main__":
    MyApp().run()
