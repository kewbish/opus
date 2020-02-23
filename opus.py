import json
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

kivy.require('1.11.1')


class MainPage(GridLayout):
    pass


class Opus(App):

    def build(self):
        return MainPage()


if __name__ == '__main__':
    Opus().run()
