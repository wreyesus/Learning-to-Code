

class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_serverd = 0

    def describe_restaurant(self):
        print(f'Welcome to {self.restaurant_name.title()}')
        print(f'Our cousine type is: {self.cuisine_type.title()}')

    def open_restaurant(self):
        print(f'The {self.restaurant_name.title()} is OPEN')

    def set_number_server(self, number):
        self.number_serverd = number

    def increment_number_served(self, number):
        self.number_serverd += number
        print(f'Customers: {self.number_serverd}')

    def show_number_serverd(self):
        print(f'{self.number_serverd}')

restaurant = Restaurant('Don Lucho', 'burguer')
restaurant.increment_number_served(100)
restaurant.increment_number_served(200)
restaurant.increment_number_served(500)
