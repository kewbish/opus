from csv import reader
from datetime import datetime
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.properties import BooleanProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from requests import get

kivy.require('1.11.1')


class MainPage(Screen):
    acc_shown = BooleanProperty(False)


class SomethingElsePage(Screen):
    pass


class Opus(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainPage(name='main_page'))
        sm.add_widget(SomethingElsePage(name='something_else_page'))
        return sm

    def same_thing_button(self):
        rates = []
        with open("data.csv", "r+") as x:
            r = reader(x)
            d = next(r)
            alls = x.readlines()
            x.writelines(alls[1:])
            date = datetime.now()
            t = datetime.strftime(date, " %B %d %Y")
            rates = [d[0], d[1], d[2], t]
            x.seek(0, 0)
            x.write(",".join(rates))

    def get_author(book):
        d = get(f"https://www.googleapis.com/books/v1/volumes?q={book}")
        auth = d['items'][0]['authors'][0]
        return auth

    def something_else_button(self):
        with open("data.csv", "r+") as x:
            x.seek(0, 0)

    def parse_text(self, value):
        return value[1]


if __name__ == '__main__':
    Opus().run()
