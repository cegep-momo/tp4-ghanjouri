import unittest
from gpiozero import Device
from gpiozero.pins.mock import MockFactory
from model.platine import Platine


Device.pin_factory = MockFactory()

class TestPlatine(unittest.TestCase):
    def setUp(self):
       
        self.platine = Platine()

    def test_bouton_demarrer_appuier(self):
        # Test lors d'un appui sur le bouton demarrer
        self.platine.boutons["demarrer"].pin.drive_low()
        bouton_presse = self.platine.bouton_appuye()
        self.assertEqual(bouton_presse, "demarrer")

        # Test lors d'un appui sur le bouton mesurer
    def test_bouton_mesure_appuier(self):
        self.platine.boutons["mesure"].pin.drive_low()
        bouton_presse = self.platine.bouton_appuye()
        self.assertEqual(bouton_presse, "mesure")
        

    # Test pour verifier que aucun bouton appuyé
    def test_bouton_non_appuier(self):
       
        bouton_presse = self.platine.bouton_appuye()
        self.assertIsNone(bouton_presse)

if __name__ == "__main__":
    unittest.main()
