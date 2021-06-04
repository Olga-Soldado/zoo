class Animal(object):
    def __init__(self, nombre, edad, salud, felicidad,clase,especial):
        self.nombre = nombre
        self.edad = edad
        self.salud =salud
        self.felicidad = felicidad
        self.Clase_animal=clase
        self.especial=especial

    def display_info(self):
        print('Tipo:',self.Clase_animal)
        print ('Nombre:',self.nombre)
        print('Edad:',self.edad)
        print('Caracteristica especial',self.especial)
        print('Salud:',self.salud)
        print('Felicidad:',self.salud)

        return self

    def feed(self,comer:int):
        if self.salud< 50:
            self.salud += comer/10
            self.felicidad += comer/10
        else :
            self.salud +=comer/5
            self.felicidad +=comer/5
        return self

class Lion(Animal):
    def __init__(self, nombre, edad, salud, felicidad,Clase_animal,especial):
        super().__init__(nombre, edad, salud, felicidad,Clase_animal,especial)
    
class Bear(Animal):
    def __init__(self, nombre, edad, salud , felicidad,Clase_animal,especial):
        super().__init__(nombre, edad, salud, felicidad,Clase_animal,especial)

class Tiger(Animal):
    def __init__(self, nombre, edad, salud , felicidad,Clase_animal,especial):
        super().__init__(nombre, edad, salud, felicidad,Clase_animal,especial)

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_lion(self, nombre,edad, salud, felicidad, Clase_animal,especial):
        self.animals.append(Lion(nombre,edad, salud, felicidad,Clase_animal, especial))
        return self
    def add_bear(self, nombre, edad, salud , felicidad,Clase_animal,especial):
        self.animals.append(Bear(nombre,edad, salud , felicidad,Clase_animal,especial))
        return self

    def add_tiger(self, nombre, edad, salud , felicidad,Clase_animal,especial):
        self.animals.append(Tiger( nombre, edad, salud , felicidad,Clase_animal,especial))
        return self

    def print_all_info(self):
        print("-" * 30, self.name, "-" * 30)
        print("Informacion general:")
        for animal in self.animals:
            animal.display_info()
        return self


zoo1 = Zoo("La ley de la selva XD")
zoo1.add_lion("Linda",3,43,43,"Leon","Carnivoro").add_lion("Simba",5,3,43,"Leon","Fuerte").add_tiger("Tigger",8,100,4,"Tigre","Enorme").add_tiger("Princessa",8,100,4,"Tigre","Peligroso").add_bear("Princessa",8,100,4,"Oso","pelaje cafe").print_all_info()
print("")
Lion.feed(Lion("Nala",3,43,43,"Leon","Carnivoro"),23).display_info()