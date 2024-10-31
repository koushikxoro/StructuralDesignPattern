from coffeedecorator import CoffeeDecorator
class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self.coffee.cost()+1.2