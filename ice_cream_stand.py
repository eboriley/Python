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


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['bacon', 'banana',
                        'black sabbath', 'cake batter',
                        'chai', 'cherry', 'hokey pokey']

    def display_flavors(self):
        print("Ice cream flavors available: ")
        for flavor in self.flavors:
            print("- "+flavor.title())


my_icecream = IceCreamStand('Vevo', 'Snacks')
my_icecream.display_flavors()
