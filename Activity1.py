class Vehicle:
    vehiclename = 'mercedes s350d'
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage
c1 = Vehicle('150 mph', '28000 miles')
print("The name of the car is ", c1.vehiclename)
print("The maximum speed of the car is ", c1.max_speed)
print("The mileage of the car is ", c1.mileage)