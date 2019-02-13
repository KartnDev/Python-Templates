from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.codeinput import CodeInput
from kivy.config import Config


Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '1024')
Config.set('graphics', 'height', '768')
from kivy.uix.floatlayout import FloatLayout

class MyApp(App):
    pass

    def btn_press(self, instance):  
        instance.text = 'Returning args..' 
        
if __name__ == "__main__" :
    MyApp().run()