from model.platine import Platine
from model.mesure import Mesure
from view.view import Vue
import time

def main():
    platine = Platine()
    vue = Vue()
    systeme_en_marche = False

    print("En attente d'un bouton...")

    try:
        while True:
            bouton = platine.bouton_appuye()

            if bouton == "demarrer":
                systeme_en_marche = not systeme_en_marche  
                if systeme_en_marche:
                    print("Système démarré.")
                    vue.afficher_message("SYSTEME", "DEMARRÉ")
                else:
                    print("Système arrêté.")
                    vue.afficher_message("SYSTEME", "ARRÊTÉ")
                time.sleep(0.5)

            elif bouton == "mesure" and systeme_en_marche:
                print("Prise de mesure...")
                vue.afficher_message("PRISE", "MESURE...")
                mesure_data = platine.lire_mesure()
                if mesure_data:
                    mesure = Mesure(
                        dateHeureMesure = mesure_data["date"].strftime("%Y-%m-%d %H:%M:%S"),
                        dataMesure = {
                            "Distance (cm)": mesure_data["distance"]
                        }
                    )
                    print(mesure.afficherMesure())
                    vue.afficher_distance(mesure_data["distance"])
                    mesure.sauvegarderJson()

                time.sleep(0.5)  # Petite pause anti-rebond

            else:
                time.sleep(0.1)

    except KeyboardInterrupt:
        print("\nArrêt du programme par l'utilisateur.")
        vue.effacer()
        time.sleep(1)

if __name__ == "__main__":
    main()
