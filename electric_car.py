class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        print("This car has a "+str(self.battery_size)+" -kWh battery.")


my_tesla_car = ElectricCar('aston martin', 'ac aceca', '1980')
print(my_tesla_car.get_description())
my_tesla_car.describe_battery()
