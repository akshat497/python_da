#oops 


#object oriented programming language

class car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year

    def start(self):
        print(f"{self.brand} {self.model} is starting.")

    def stop(self):
        print(f"{self.brand} {self.model} is stopping.")
        
        
toyota=car("Toyota","Camry",2020)
honda=car("Honda","Civic",2019)
BMW=car("BMW","X5",2021)


toyota.start()
honda.start()
BMW.start()




