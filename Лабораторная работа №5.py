class Rocket():
    def __init__(self, total_weight, fuel_quantity, engine_status):
        self.total_weight = total_weight
        self.fuel_quantity = fuel_quantity
        self.engine_status = engine_status
    def spend_fuel(self, count):               
        self.fuel_quantity -= count           
        self.total_weight -= count             
        if self.fuel_quantity <= 0:
            self.fuel_quantity = 0
            self.engine_status = False
            return False
        elif self.fuel_quantity > 0:
            self.engine_status = True
            return True
    def get_fuel_level(self):                                      
        return f'Fuel: {self.fuel_quantity}'
    def get_total_weight(self):                                     
        return f'Mass: {self.total_weight}'
    def get_is_engine_running(self):                                
        return f'Engine status: {self.engine_status}'

def main():
    Apollon = Rocket(1500, 500, True)
    while Apollon.fuel_quantity > 0:
        Apollon.spend_fuel(100)
        print(Apollon.get_fuel_level(), end='; ')
        print(Apollon.get_total_weight(), end='; ')
        print(Apollon.get_is_engine_running())
main()