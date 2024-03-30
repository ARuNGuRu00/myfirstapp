from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
class myappli(App):
    def build(self):
        self.window=GridLayout()
        self.window.add_widget(Button(text="233"))
        return self.window
if __name__=="__main__":
    myappli().run()
