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

import time

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
        Clock.schedule_once(self.runOnEnter)

    def runOnEnter(self, instance):
        self.addSelectbuttons()



    def addSelectbuttons(self):
        self.addHourButtons()
        self.addMinuteButtons()
        self.addSecondButtons()

    def addHourButtons(self):
        self.addButtons(24, self.hourGrid, self.hourButtonOnRelease)

    def addMinuteButtons(self):
        self.addButtons(60, self.minuteGrid, self.minuteButtonOnRelease)

    def addSecondButtons(self):
        self.addButtons(60, self.secondGrid, self.secondButtonOnRelease)



    def hourButtonOnRelease(self, instance):
        self.hours.text = str(instance.text)

    def minuteButtonOnRelease(self, instance):
        self.minutes.text = str(instance.text)

    def secondButtonOnRelease(self, instance):
        self.seconds.text = str(instance.text)

    def addButtons(self, amount, insertInto, onRelease):

        for i in range(1, amount):
            button = ScrollViewButton(text= str(i))
            button.bind(on_press= onRelease)

            insertInto.add_widget(button)



    def getTimerDisplayText(self):
        timeLeft = (
            int(self.hours.text),
            int(self.minutes.text),
            int(self.seconds.text) 
            )

        return timeLeft    

    def convertToSeconds(self, hours, minutes, seconds):
        return (hours * 3600) + (minutes * 60) + seconds   

    def formatTimeLeft(self, hours, minutes, seconds):
        if seconds < 0:
            seconds = 59

            minutes -= 1

            if minutes < 0:
                minutes = 59

                hours -= 1

        return hours, minutes, seconds


    def updateTimeLeftLabels(self, hours, minutes, seconds):
        self.hours.text = str(hours)
        self.minutes.text = str(minutes)
        self.seconds.text = str(seconds)
        

    def timerTick(self, instance):
        hours, minutes, seconds = self.getTimerDisplayText()
        self.updateTimeLeftLabels(*self.formatTimeLeft(hours, minutes, seconds - 1))

    def resetTimeLeftLabels(self):
        self.updateTimeLeftLabels(0, 0, 0)

    def timerStop(self):
        Clock.unschedule(self.timerTick)
        Clock.unschedule(self.checkTimerStop)

    def timerStart(self):
        self.timerRun(self.convertToSeconds(*self.getTimerDisplayText()))

    def timerReset(self):
        self.timerStop()
        self.resetTimeLeftLabels()



    def timerRun(self, seconds):
        Clock.schedule_interval(self.timerTick, 1)
        Clock.schedule_interval(self.checkTimerStop, 1)

    def checkTimerStop(self, instance):
        if self.convertToSeconds(*self.getTimerDisplayText()) == 0:
            self.timerStop() 


class ScrollViewGridLayout(GridLayout):
    pass

class BackgroundLabel(Label):
    pass

class ColorLabel(Label):
    pass

class ScrollViewButton(Button):
    pass




kv = Builder.load_file("widgets.kv")

class MyApp(App):

    def build(self):
        return kv


if __name__ == '__main__':
    MyApp().run()