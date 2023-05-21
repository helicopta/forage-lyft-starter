from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage) :
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        calliope = Car(engine, battery)
        return calliope

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage) :
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        glissade = Car(engine, battery)
        return glissade

    @staticmethod
    def create_palindrome(self, current_date, last_service_date, warning_light_on) :
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        palindrome = Car(engine, battery)
        return palindrome
    
    @staticmethod
    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage) :
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        rorschach = Car(engine, battery)
        return rorschach

    @staticmethod
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage) :
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        thovex = Car(engine, battery)
        return thovex