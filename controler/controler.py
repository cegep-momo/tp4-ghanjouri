from model.platine import Platine
from model.mesure import Mesure
from view.view import Vue
import time

class Controler:
    def __init__(self):

        self.platine = Platine()
        self.vue = Vue()
        self.systeme_en_marche = False
        self.dernier_temps_mesure = time.time()  


    def demarrer_systeme(self):
        
        # on met le système en marche et on affiche un message sur l'écran
       
        self.systeme_en_marche = True
        print("Système démarré")
        self.vue.afficher_message("Systeme", "Demarer")
        time.sleep(2)

    def arreter_systeme(self):
        
        # on arrête le système et affiche un message sur l'écran
        
        self.systeme_en_marche = False
        print("Système arrêté")
        self.vue.afficher_message("Systeme", "Arreter")
        time.sleep(2)

    def prendre_mesure(self):
        
        # on prend une mesure avec le capteur et affiche la distance sur l'écran et sauvegarde dans JSON
        
        print("Prise de mesure...")
        self.vue.afficher_message("Prise", "Mesure...")
        time.sleep(2)
        
        mesure_data = self.platine.lire_mesure()
        if mesure_data:
            mesure = Mesure(
                dateHeureMesure = mesure_data["date"].strftime("%Y-%m-%d %H:%M:%S"),
                dataMesure = {
                    "Distance (cm)": mesure_data["distance"]
                }
            )
            print(mesure.afficherMesure())
            self.vue.afficher_distance(mesure_data["distance"])
            mesure.sauvegarderJson()
            time.sleep(2)


    def programme(self):
        
        # Boucle pour gérer l'appui sur les boutons et l'état du système.
        
        print("Système prêt. En attente de bouton...")

        try:
            while True:
                bouton = self.platine.bouton_appuye()

                if bouton == "demarrer":
                    # Changer l'état du système
                    if self.systeme_en_marche:
                        self.arreter_systeme()
                    else:
                        self.demarrer_systeme()
                    time.sleep(0.5)

                elif bouton == "mesure" and self.systeme_en_marche:
                    # Si système en marche, prendre une mesure
                    self.prendre_mesure()
                    time.sleep(0.5)

                # mesure automatique
                if self.systeme_en_marche:
                    temps_courant = time.time()
                    if temps_courant - self.dernier_temps_mesure >= 5:
                        self.prendre_mesure()
                        self.dernier_temps_mesure = temps_courant


        except KeyboardInterrupt:
            print("\nArrêt du programme")
            self.vue.effacer()
            time.sleep(1)
