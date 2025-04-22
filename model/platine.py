import time
import RPi.GPIO as GPIO
from Freenove_DHT_GPIO import DHT
from gpiozero import Button
import datetime

class Platine:
    def __init__(self):
        self.boutons = {
            "demarrer": Button(19),
            "arreter": Button(26)
        }
        
        self.DHT_GPIO = 4
        GPIO.setwarnings(False)
        self.dht = DHT(self.DHT_GPIO)

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
        for i in range(15):
            valeur = self.dht.readDHT11()
            if valeur == self.dht.DHTLIB_OK:
                temperature = self.dht.temperature
                humidite = self.dht.humidity
                moment = datetime.datetime.now()
                return {
                    "date": moment,
                    "temperature": temperature,
                    "humidite": humidite
                }
            time.sleep(0.1)
        return None
