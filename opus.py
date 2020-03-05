from csv import reader
from datetime import datetime
import kivy
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from os import chdir, path
from requests import get

kivy.require('1.11.1')


class MainPage(Screen):

    def same_thing_button(self):
        rates = []
        with open("data.csv", "r+") as x:
            r = reader(x)
            d = [str(x).strip() for x in next(r)]
            alls = x.readlines()
            x.writelines(alls[1:])
            t = datetime.strftime(datetime.now(), "%B %d %Y")
            rates = [d[0], d[1], d[2], t]
            x.seek(0, 0)
            x.write(",".join(rates))

    def something_else_button(self):
        self.manager.get_screen("something_else_page").\
            ids.book_item.collapse = False
        self.manager.current = "something_else_page"


class SomethingElsePage(Screen):

    def parse_book(self, value):
        b = value[1].replace(" ", "_")
        d = get(f"https://www.googleapis.com/books/v1/volumes?q={b}").\
            json()
        a = d['items'][0]['volumeInfo']['authors'][0]
        auth = ObjectProperty()
        self.ids.author.text = a

    def enter_data(self):
        t = datetime.strftime(datetime.now(), "%B %d %Y")
        rates = [self.ids.book.text, self.ids.author.text, t, t]
        with open("data.csv", "r+") as x:
            alls = x.readlines()
            x.seek(0, 0)
            x.write(",".join(rates) + "\n")
            x.writelines(alls)
        self.parent.current = "main_page"


class Opus(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainPage(name='main_page'))
        sm.add_widget(SomethingElsePage(name='something_else_page'))
        return sm


if __name__ == '__main__':
    if not path.isfile("data.csv"):
        open("data.csv", "w+")
    Opus().run()
