import json
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

kivy.require('1.11.1')


class main_page(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.add_widget(Label(text='OPUS - what have you read today?'))
        self.add_widget(Button(text='the same thing'))
        self.add_widget(Button(text='something new'))


class Opus(App):

    def build(self):
        return main_page()


if __name__ == '__main__':
    Opus().run()
