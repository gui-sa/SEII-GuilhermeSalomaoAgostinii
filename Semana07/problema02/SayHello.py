#pip3 install kivy
#Importing Widget
from kivy.app import App 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class SayHello(App):
    def build(self): #It needs to have a class named build that receives as atribute the APP (imported module)
        self.window = GridLayout()
        self.window.cols = 1 #Putting just one col into this blank window
        
        #This afects only the cols
        self.window.size_hint = (0.6,0.7) #itx column will have 60% of the window default size on x and 70% on y
        self.window.pos_hint = {"center_x":0.5,"center_y":0.5} #It will be opened at the center
        
        self.window.add_widget(Image(source='logo.png')) #addd_widget will let you add something to the windows...adding an Image to it.
        self.greeting = Label(
            text="What's yout name?",
            font_size=18,
            color='#00FFCE' 
            ) #it looks like css
            #this atribute is custom for maintaining it componentized
        self.window.add_widget(self.greeting) #As it ia bellow the image it will appear at bottom.
        self.user = TextInput(
            multiline=0,
            padding_y = (20,20),
            padding_x = (10),
            size_hint=(1,0.5)
            ) #custom class atribute.. TextInput is a widget... multline dont let you type mult lines.
        self.window.add_widget(self.user) #As it ia bellow the image it will appear at bottom.
        self.button = Button(
                            text="GREET",
                            size_hint = (1,0.5),
                            bold= True,
                            background_color = '#00FFCE',
                            background_normal = "",
                            color="#000000"
                            )
        self.button.bind(on_press=self.anyFunction) #bind a callbackfuntion to the button trigger
        self.window.add_widget(self.button)

        return self.window

    def anyFunction(self, instance): #it is a callfunction for when I press the button
        self.greeting.text = f"Hello, {self.user.text}!"
 
if __name__ == "__main__":
    SayHello().run()

# It runs and puts up a blank window with the name of your file.