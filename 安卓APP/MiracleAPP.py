from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label

class TutorialApp(App):
    def build(self):
        s = Scatter()
        l = Label(text='Miracle', font_size=50)
        s.add_widget(l)
        return s


if __name__ == "__main__":
    TutorialApp().run()