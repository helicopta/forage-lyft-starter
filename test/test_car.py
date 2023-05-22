import unittest
from datetime import datetime

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire

class TestCapuletEngine(unittest.TestCase) :
    def test_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0

        capulet = CapuletEngine(last_service_mileage, current_mileage)
        self.assertTrue(capulet.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0

        capulet = CapuletEngine(last_service_mileage, current_mileage)
        self.assertFalse(capulet.needs_service())

class TestWilloughbyEngine(unittest.TestCase) :
    def test_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0

        willoughby = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertTrue(willoughby.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0

        willoughby = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertFalse(willoughby.needs_service())

class TestSternmanEngine(unittest.TestCase) :
    def test_engine_should_be_serviced(self):
        warning_light_is_on = True

        sternman = SternmanEngine(warning_light_is_on)
        self.assertTrue(sternman.needs_service())

    def test_engine_should_not_be_serviced(self):
        warning_light_is_on = False

        sternman = SternmanEngine(warning_light_is_on)
        self.assertFalse(sternman.needs_service())

class TestNubbinBattery(unittest.TestCase) :
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)

        nubbin = NubbinBattery(last_service_date, current_date)
        self.assertTrue(nubbin.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)

        nubbin = NubbinBattery(last_service_date, current_date)
        self.assertFalse(nubbin.needs_service())

class TestSpindlerBattery(unittest.TestCase) :
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 4)

        spindler = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(spindler.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)

        spindler = SpindlerBattery(last_service_date, current_date)
        self.assertFalse(spindler.needs_service())

class TestCarriganTire(unittest.TestCase) :
    def test_tire_should_be_serviced(self):
        array = [0.5, 0.5, 0.9, 0.8]

        carrigan = CarriganTire(array)
        self.assertTrue(carrigan.needs_service())

    def test_tire_should_not_be_serviced(self):
        array = [0.5, 0.5, 0.8, 0.8]

        carrigan = CarriganTire(array)
        self.assertFalse(carrigan.needs_service())

class TestOctoprimeTire(unittest.TestCase) :
    def test_tire_should_be_serviced(self):
        array = [0.5, 0.9, 0.9, 0.9]

        octoprime = OctoprimeTire(array)
        self.assertTrue(octoprime.needs_service())

    def test_tire_should_not_be_serviced(self):
        array = [0.5, 0.5, 0.5, 0.5]

        octoprime = OctoprimeTire(array)
        self.assertFalse(octoprime.needs_service())

if __name__ == '__main__':
    unittest.main()
