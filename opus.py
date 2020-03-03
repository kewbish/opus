from csv import reader
from datetime import datetime
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


if __name__ == '__main__':
    Opus().run()
