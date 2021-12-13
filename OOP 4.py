class Vehicle:
    def __init__(self, maxSpeed, mileage):
        self.maxSpeed = maxSpeed
        self.mileage = mileage

class Bus(Vehicle):
    def __init__(self, maxSpeed, mileage):
        super().__init__(maxSpeed, mileage)

bus = Bus(120, 50000)
print(f"Bus Max Speed: {bus.maxSpeed} \nBus Mileage: {bus.mileage}")