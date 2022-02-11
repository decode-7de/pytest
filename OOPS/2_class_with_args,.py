class Car:
    no_of_tires = 4

    def __init__(self,model,year) -> None:
        self.model = model
        self.make = year
        self.engine = 'not starting'

    def start_the_engine(self):
        self.engine = 'start'




new_car = Car('merc',2009)
print(new_car.model)
print(new_car.make)
print(new_car.engine)
print(new_car.no_of_tires)

new_car.no_of_tires = 10
print(new_car.no_of_tires)
old_car = Car('ambi',2010)
print(old_car.no_of_tires)
print(old_car.model)
old_car.start_the_engine()
print(old_car.engine)
print(new_car.engine)