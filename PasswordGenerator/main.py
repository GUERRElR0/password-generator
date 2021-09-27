from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
#from kivmob import KivMob, TestIds
import logic

class box(TabbedPanel):
    def logic(self,password,digitos):

        if password:
            if self.ids.all.active == True or self.ids.numbers.active == True and self.ids.letters.active == True and self.ids.symbols.active == True or self.ids.numbers.active == True and self.ids.letters.active == True and self.ids.symbols.active == True and self.ids.lower.active == True and self.ids.upper.active == True or self.ids.numbers.active == True and self.ids.symbols.active == True and self.ids.lower.active == True and self.ids.upper.active == True:
                try:
                    self.display.text = str(logic.todos(digitos))
                except Exception:
                    self.display.text = "Error"
            
            elif self.ids.letters.active == True and self.ids.numbers.active == True or self.ids.numbers.active == True and self.ids.lower.active == True and self.ids.upper.active == True:
                try:
                    self.display.text = str(logic.NumLet(digitos))
                except Exception:
                    self.display.text = "Error"

            elif self.ids.lower.active == True and self.ids.numbers.active == True and self.ids.symbols.active == True:
                try:
                    self.display.text = str(logic.NumSymLow(digitos))
                except Exception:
                    self.display.text = "Error"  
            
            elif self.ids.upper.active == True and self.ids.numbers.active == True and self.ids.symbols.active == True:
                try:
                    self.display.text = str(logic.NumSymUpp(digitos))
                except Exception:
                    self.display.text = "Error"  

            elif self.ids.symbols.active == True and self.ids.numbers.active == True:
                try:
                    self.display.text = str(logic.NumSym(digitos))
                except Exception:
                    self.display.text = "Error"

            elif self.ids.letters.active == True and self.ids.symbols.active == True or self.ids.symbols.active == True and self.ids.lower.active == True and self.ids.upper.active == True:
                try:
                    self.display.text = str(logic.LetSym(digitos))
                except Exception:
                    self.display.text = "Error" 
            
            elif self.ids.lower.active == True and self.ids.numbers.active == True:
                try:
                    self.display.text = str(logic.NumLow(digitos))
                except Exception:
                    self.display.text = "Error"  
            
            elif self.ids.numbers.active == True and self.ids.upper.active == True:
                try:
                    self.display.text = str(logic.NumUpp(digitos))
                except Exception:
                    self.display.text = "Error" 

            elif self.ids.lower.active == True and self.ids.symbols.active == True:
                try:
                    self.display.text = str(logic.LowSym(digitos))
                except Exception:
                    self.display.text = "Error" 

            elif self.ids.symbols.active == True and self.ids.upper.active == True:
                try:
                    self.display.text = str(logic.UppSym(digitos))
                except Exception:
                    self.display.text = "Error" 

            elif self.ids.letters.active == True or self.ids.lower.active == True and self.ids.upper.active == True:
                try:
                    self.display.text = str(logic.letters(digitos))
                except Exception:
                    self.display.text = "Error"
            
            elif self.ids.numbers.active == True:
                try:
                    self.display.text = str(logic.numbers(digitos))
                except Exception:
                    self.display.text = "Error"

            elif self.ids.symbols.active == True:
                try:
                    self.display.text = str(logic.symbols(digitos))
                except Exception:
                    self.display.text = "Error"  

            elif self.ids.lower.active == True:
                try:
                    self.display.text = str(logic.LowerCase(digitos))
                except Exception:
                    self.display.text = "Error"

            elif self.ids.upper.active == True:
                try:
                    self.display.text = str(logic.UpperCase(digitos))
                except Exception:
                    self.display.text = "Error" 

class app(App):
    def build(self):
        self.icon = "small_icon.png"
    
        return box()

# I still don't know how to include advertisements in the app.
"""    def build(self):
        self.ads = KivMob(TestIds.APP)
        self.ads.new_interstitial(TestIds.INTERSTITIAL)
        self.ads.request_interstitial()
        return Button(text='Show Interstitial',
                      on_release=lambda a:self.ads.show_interstitial())

    def on_resume(self):
        self.ads.request_interstitial()
"""
app().run()

