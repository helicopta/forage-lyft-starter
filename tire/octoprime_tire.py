from tire.tire import Tire
 
class OctoprimeTire(Tire) :
    def __init__(self, worn_array):
        self.worn_array = worn_array
    
    def needs_service(self):
        count = 0
        for worn_tire in self.worn_array:    
            count += worn_tire
        if count >= 3:
            return True
        else:
            return False