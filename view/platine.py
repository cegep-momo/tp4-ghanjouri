from gpiozero import Button
import time

class Platine:
    def __init__(self):
        self.boutons = {
            "demarer": Button(19), 
            "arreter": Button(26)    
        }

    def attendre_bouton(self):
        # on attend qu'un bouton soit appuyé et retourne son fonctionnalité
        while True:
            for couleur, bouton in self.boutons.items():
                if bouton.is_pressed:
                    while bouton.is_pressed:  # on attend que le bouton soit relaché
                        time.sleep(0.1)
                    time.sleep(0.3)  
                    return couleur

    def bouton_appuye(self):
        # on vérifie si un bouton est appuyé 
        for couleur, bouton in self.boutons.items():
            if bouton.is_pressed:
                return couleur
        return 
