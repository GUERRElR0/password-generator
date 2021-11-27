import logic
from kivy.app import App
from kivmob import KivMob
from functools import lru_cache
from kivy.uix.screenmanager import ScreenManager, Screen  

@lru_cache(maxsize=10)

class ScreenManager(ScreenManager):
    pass

class First(Screen):

    def logic(self,digitos,screen):

        try:

            if screen.ids.all.active == True or screen.ids.numbers.active == True and screen.ids.letters.active == True and screen.ids.symbols.active == True or screen.ids.numbers.active == True and screen.ids.letters.active == True and screen.ids.symbols.active == True and screen.ids.lower.active == True and screen.ids.upper.active == True or screen.ids.numbers.active == True and screen.ids.symbols.active == True and screen.ids.lower.active == True and screen.ids.upper.active == True:
                
                self.display.text = str(logic.todos(digitos))
                
            elif screen.ids.letters.active == True and screen.ids.numbers.active == True or screen.ids.numbers.active == True and screen.ids.lower.active == True and screen.ids.upper.active == True:
                
                self.display.text = str(logic.NumLet(digitos))

            elif screen.ids.lower.active == True and screen.ids.numbers.active == True and screen.ids.symbols.active == True:
                
                self.display.text = str(logic.NumSymLow(digitos))  
                
            elif screen.ids.upper.active == True and screen.ids.numbers.active == True and screen.ids.symbols.active == True:
                
                self.display.text = str(logic.NumSymUpp(digitos))  

            elif screen.ids.symbols.active == True and screen.ids.numbers.active == True:
                
                self.display.text = str(logic.NumSym(digitos))

            elif screen.ids.letters.active == True and screen.ids.symbols.active == True or screen.ids.symbols.active == True and screen.ids.lower.active == True and screen.ids.upper.active == True:
                
                self.display.text = str(logic.LetSym(digitos)) 
                
            elif screen.ids.lower.active == True and screen.ids.numbers.active == True:
                
                self.display.text = str(logic.NumLow(digitos))  
                
            elif screen.ids.numbers.active == True and screen.ids.upper.active == True:
                
                self.display.text = str(logic.NumUpp(digitos)) 

            elif screen.ids.lower.active == True and screen.ids.symbols.active == True:
                
                self.display.text = str(logic.LowSym(digitos)) 

            elif screen.ids.symbols.active == True and screen.ids.upper.active == True:
                
                self.display.text = str(logic.UppSym(digitos)) 

            elif screen.ids.letters.active == True or screen.ids.lower.active == True and screen.ids.upper.active == True:
                
                self.display.text = str(logic.letters(digitos))
                
            elif screen.ids.numbers.active == True:
                
                self.display.text = str(logic.numbers(digitos))

            elif screen.ids.symbols.active == True:
                
                self.display.text = str(logic.symbols(digitos))  

            elif screen.ids.lower.active == True:
                
                self.display.text = str(logic.LowerCase(digitos))

            elif screen.ids.upper.active == True:
                
                self.display.text = str(logic.UpperCase(digitos)) 

        
        except Exception:
            self.display.text = "Error"

class Option(Screen):
    pass

class app(App):

    #ads
    ads = KivMob('ca-app-pub-3940256099942544 ~ 3347511713')

    def build(self):
        #ads
        self.ads.new_banner('ca-app-pub-3940256099942544/6300978111',False)
        self.ads.request_banner()
        self.ads.show_banner()

        #ScreenManager
        sm = ScreenManager()
        sm.add_widget(First(name='first'))
        sm.add_widget(Option(name='option'))
        return sm

if __name__ == "__main__":
    app().run()