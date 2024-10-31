from simplecoffee import SimpleCoffee
from milkdecorator import MilkDecorator
from sugardecorator import SugarDecorator
if __name__=="__main__":
    coffee=SimpleCoffee()
    milk_coffee=MilkDecorator(coffee)
    sugar_milk_coffee=SugarDecorator(milk_coffee)
    print(sugar_milk_coffee.cost())