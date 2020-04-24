class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("This is "+self.restaurant_name.title() +
              " and we serve "+self.cuisine_type.title()+" dishes.")

    def restaurant_open(self):
        print(self.restaurant_name.title()+" is open!")

    def set_number_served(self, number):
        self.number_served += number

    def increment_number_served(self, number):
        if number >= self.number_served:
            self.number_served += number
            print("We served "+str(self.number_served)+" in a day of business")
        else:
            print("Number served can only be increased!")


# my_restaurant = Restaurant('Easy Company', 'continental')

# my_restaurant.describe_restaurant()
# my_restaurant.restaurant_open()
# my_restaurant.set_number_served(18)
# my_restaurant.increment_number_served(60)


class User():

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.login_attempts = 0

    def greet_user(self):
        print("Hi "+self.first.title()+" " +
              self.last.title()+" welcome to the party!")

    def count_login_attempts(self):
        self.login_attempts += 1
        login_counts = self.login_attempts
        print("Login attempts "+str(login_counts))

    def reset_login_attempts_count(self):
        self.login_attempts = 0
        print("Login attempts reset to "+str(self.login_attempts))


# user_1 = User('ebo', 'riley')
# user_1.greet_user()
# user_1.count_login_attempts()
# user_1.count_login_attempts()
# user_1.count_login_attempts()
# user_1.count_login_attempts()
# user_1.reset_login_attempts_count()


class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_description(self):
        long_name = self.make+' '+self.model+' '+str(self.year)
        return long_name.title()

    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" mileage on it")

    def update_odemeter(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading += mileage
        else:
            print("Odometer reading cannot be rolled back")


# my_car = Car('audi', 'a4', 2016)
# print(my_car.get_description())
# my_car.read_odometer()
# my_car.update_odemeter(77)
# my_car.read_odometer()


class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a "+str(self.battery_size)+" -kWh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately "+str(range)
        message += " miles on full charge."
        print(message)

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


# my_tesla_car = ElectricCar('aston martin', 'ac aceca', '1980')
# print(my_tesla_car.get_description())


# my_tesla_car.battery.describe_battery()
# my_tesla_car.battery.get_range()
# my_tesla_car.battery.upgrade_battery()
# my_tesla_car.battery.get_range()
