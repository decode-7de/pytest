class Car:
    
    def __init__(self) -> None:
        self.make = 'Ford'
        self.model = "mustang"
        self.year = 2010
        self.engine = 'not_running'
    
    def start_the_engine(self):
        print("calling the engine start function...!")
        self.engine ='running'


new_car = Car()
print(new_car.engine)

new_car.start_the_engine()
print(new_car.engine)