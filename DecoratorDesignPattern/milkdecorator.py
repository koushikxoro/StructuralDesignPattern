from coffeedecorator import CoffeeDecorator
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self.coffee.cost()+1.5