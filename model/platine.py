import time
from gpiozero import Button, DistanceSensor
import datetime

class Platine:
    def __init__(self):
        self.boutons = {
            "demarrer": Button(19),
            "arreter": Button(26)
        }
        
        self.capteur = DistanceSensor(echo=12, trigger=17, max_distance=3)

    def attendre_bouton(self):
        while True:
            for couleur, bouton in self.boutons.items():
                if bouton.is_pressed:
                    while bouton.is_pressed:
                        time.sleep(0.1)
                    time.sleep(0.3)
                    return couleur

    def bouton_appuye(self):
        for couleur, bouton in self.boutons.items():
            if bouton.is_pressed:
                return couleur
        return None

    def lire_mesure(self):
        cm = self.capteur.distance * 100  
        moment = datetime.datetime.now()
        return {
            "date": moment,
            "distance": round(cm, 2)
        }
