class Engine:
    def start(self):
        print("Engine started")

class Car: 
    def __init__(self, engine): # dependency injection
        self.engine = engine 

    def start(self):
        self.engine.start()
        print("Car started")

engine = Engine()
car = Car(engine)

car.start()