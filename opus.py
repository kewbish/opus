from datetime import datetime
from json import load, dump
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

    def same_thing(self):
        with open("data.json", "r") as x:
            d = load(x)
        now = datetime.now()
        date = datetime.strftime(now, "%B %d %Y")
        d["Bonus Poetry"]["date_ended"] = date
        with open("data.json", "w") as x:
            dump(d, x)


if __name__ == '__main__':
    Opus().run()
