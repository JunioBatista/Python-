# pip install Kivy

from kivy.app import App
from kivy.uix.button import Button

class ExemploApp(App):
    def build(self):
        return Button(text='Olá, Mundo!')