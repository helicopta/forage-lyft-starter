from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

class CarFactory(Car):
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage) :
        calliope = Car(self)
        calliope.engine = CapuletEngine(last_service_mileage, current_mileage)
        calliope.battery = SpindlerBattery(last_service_date, current_date)

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage) :
        calliope = Car(self)
        calliope.engine = WilloughbyEngine(last_service_mileage, current_mileage)
        calliope.battery = SpindlerBattery(last_service_date, current_date)

    def create_palindrome(self, current_date, last_service_date, warning_light_on) :
        calliope = Car(self)
        calliope.engine = SternmanEngine(warning_light_on)
        calliope.battery = SpindlerBattery(last_service_date, current_date)
    
    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage) :
        calliope = Car(self)
        calliope.engine = WilloughbyEngine(last_service_mileage, current_mileage)
        calliope.battery = NubbinBattery(last_service_date, current_date)

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage) :
        calliope = Car(self)
        calliope.engine = CapuletEngine(last_service_mileage, current_mileage)
        calliope.battery = NubbinBattery(last_service_date, current_date)