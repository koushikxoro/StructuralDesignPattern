from coffee import Coffee
class CoffeeDecorator(Coffee):
    def __init__(self, coffee:Coffee):
        self.coffee=coffee

    def cost(self):
        return self.coffee.cost()
