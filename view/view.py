from view.LCD1602 import CharLCD1602
import time

class Vue:
    def __init__(self):
        
        # on initialise l'écran LCD et affiche un message.
        
        self.lcd = CharLCD1602()
        
        if self.lcd.init_lcd(addr=None, bl=1):
            print("LCD initialisé avec succès.")
        else:
            print("Erreur d'initialisation de l'écran LCD.")

    def afficher_message(self, ligne1="", ligne2=""):
        
        # on affiche un message sur deux lignes du LCD
    
        self.lcd.clear()
        self.lcd.write(0, 0, ligne1)
        self.lcd.write(1, 1, ligne2)

    def afficher_distance(self, distance_cm):
        
        # on affiche une distance en centimètres sur l'écran LCD.
 
        self.lcd.clear()
        self.lcd.write(0, 0, "Distance:")
        self.lcd.write(0, 1, f"{distance_cm:.2f} cm")

    def effacer(self):
        
       # Efface l'écran LCD
       
        self.lcd.clear()
