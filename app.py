from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder
from kivy.clock import Clock

class WindowManager(ScreenManager):
    pass

class MainScreen(Screen):

    hours = ObjectProperty(None)
    minutes = ObjectProperty(None)
    seconds = ObjectProperty(None)

    hourGrid = ObjectProperty(None)
    minuteGrid = ObjectProperty(None)
    secondGrid = ObjectProperty(None)

    def on_enter(self):
        Clock.schedule_once(self.addSelectbuttons)

    def addSelectbuttons(self):
        self.addHourButtons()
        self.addMinuteButtons()
        self.addSecondButtons()

    def addHourButtons(self):
        self.addButtons(24, self.hourGrid, None)


    def addMinuteButtons(self):
        self.addButtons(60, self.minuteGrid, None)
    

    def addSecondButtons(self):
        self.addButtons(60, self.secondGrid, None)


    def addButtons(self, amount, insertInto, onRelease):

        for i in range(1, amount):
            button = Button(text=str(i), onrelease=onRelease)

            insertInto.add_widget(button)

kv = Builder.load_file("widgets.kv")

class MyApp(App):

    def build(self):
        return kv


if __name__ == '__main__':
    MyApp().run()