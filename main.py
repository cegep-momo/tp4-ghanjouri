from model.platine import Platine
from model.mesure import Mesure
import time

def main():
    platine = Platine()
    systeme_en_marche = False

    print("En attente d'un bouton...")

    try:
        while True:
            bouton = platine.bouton_appuye()

            if bouton == "demarrer":
                if systeme_en_marche:
                    print("Le système est déjà démarré.")
                else:
                    print("Système démarré.")
                    systeme_en_marche = True
                time.sleep(0.5)

            elif bouton == "arreter":
                if not systeme_en_marche:
                    print("Le système est déjà arrêté.")
                else:
                    print("Système arrêté.")
                    systeme_en_marche = False
                time.sleep(0.5)

            if systeme_en_marche:
                mesure_data = platine.lire_mesure()
                if mesure_data:
                    mesure = Mesure(
                        dateHeureMesure = mesure_data["date"].strftime("%Y-%m-%d %H:%M:%S"),
                        dataMesure = {
                            "Distance (cm)": mesure_data["distance"]
                        }
                    )
                    print(mesure.afficherMesure())
                    mesure.sauvegarderJson()

                time.sleep(5)  # Attendre 5 secondes avant prochaine mesure

            else:
                time.sleep(0.1)

    except KeyboardInterrupt:
        print("\nArrêt du programme par l'utilisateur.")
        time.sleep(1)

if __name__ == "__main__":
    main()
