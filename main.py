from typing import Text
from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.core.window import Window


Window.size=(320,600)

class Gerenciador(ScreenManager):
    pass

class Fundo(Screen):
    pass

class TelaLogin(Screen):
    pass

class Main(MDApp):
    def build(self):
        return Gerenciador()


Main().run()