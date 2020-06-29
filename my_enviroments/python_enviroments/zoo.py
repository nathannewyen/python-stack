class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_lion(self, name):
        self.animals.append('Lion')

    def add_tiger(self, name):
        self.animals.append('Tiger')

    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            print(animal)


zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala")
zoo1.add_lion("Simba")
zoo1.add_tiger("Rajah")
zoo1.add_tiger("Shere Khan")
zoo1.print_all_info()
