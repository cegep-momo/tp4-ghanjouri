import json
from datetime import datetime

class Mesure:
    # un constructeur
    def __init__(self, dateHeureMesure, dataMesure):
        self.dateHeureMesure = dateHeureMesure
        self.dataMesure = dataMesure
    
    def __repr__(self):
        return f"Mesure fait le {self.dateHeureMesure}: {self.dataMesure}"

    def afficherMesure(self):
        return f"Date et Heure: {self.dateHeureMesure}\nDonnée mesurée: {self.dataMesure}"
    
    # Methode qui sauvegarde la mesure dans un fichier JSON
    def sauvegarderJson(self):
        
        # on charge les données existantes du fichier JSON, ou une liste vide si le fichier n'existe pas
        try:
            with open("mesures.json", "r", encoding='utf-8') as fichier_json:
                fichier = json.load(fichier_json)
        except (FileNotFoundError, json.JSONDecodeError):
            
            fichier = {"mesures": []}
            
        # on crée un dict avec les informations à sauvegarder
        data = {
            "dateHeureMesure": self.dateHeureMesure,
            "dataMesure": self.dataMesure
        }
        
        # on ajoute la nouvelle mesure au fichier
        fichier["mesures"].append(data)
        
        # on sauvegarde les données dans le fichier JSON
        with open("mesures.json", "w", encoding='utf-8') as fichier_json:
            json.dump(fichier, fichier_json, ensure_ascii=False, indent=4)
       
        print("Résultats sauvegardés!")



