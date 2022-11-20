#Nao foi possivel acessar os arquivos.. Desde o dia 19/11/22. O server simplesmente nao me deixa entrar.
#Vou improvisar sem aquela funcao que ele criou que torna o desenvolvimento mais dinamico
#https://www.youtube.com/watch?v=AS3b70pLYEU
#https://www.techwithtim.net/tutorials/kivy-tutorial/the-kv-design-language-kv-file/
#https://phosphoricons.com/

from kivy.app import App 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout #https://kivy.org/doc/stable/api-kivy.uix.boxlayout.html
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

class MyRootWidget(BoxLayout):
    pass
#To work with .kv, its is requiered to create that (Widget) class, AND the .kv need to have the first word (Started with Uppercase).kv

class MyApp(App):
    def build(self): #It needs to have a class named build that receives as atribute the APP (imported module)        
        return MyRootWidget()

if __name__ == "__main__":
    MyApp().run()


#Aparently, .kv separates style from the code.