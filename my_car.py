from car import Car, ElectricCar

my_new_car = Car('ford', 'raptor', '2018')
print(my_new_car.get_description())
my_tesla = ElectricCar('tesla', 'model s', '2016')
print(my_tesla.get_description())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
