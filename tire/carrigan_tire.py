from tire.tire import Tire

class CarriganTire(Tire) :
    def __init__(self, worn_array):
        self.worn_array = worn_array
    
    def needs_service(self):
        count = 0
        for worn_tire in self.worn_array:
            if worn_tire >= 0.9:
                count += 1
        if count >= 1:
            return True
        else:
            return False