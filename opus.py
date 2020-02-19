import kivy
from kivy.app import App
from kivy.uix.label import Label

kivy.require('1.11.1')


class Opus(App):

    def build(self):
        return Label(text='Opus - an elegant booktracker system.')


if __name__ == '__main__':
    Opus().run()
