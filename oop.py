
# class definition
class Animal(object):
    #weight
    #color

    # inicializator atributu
    def __init__(self,weight=None,color=None):
        print("Initializing...")
        self.weight = weight
        self.color = color

    # aby nam to vypisovalo neco hezkyho
    
    def __str__(self):
        return "Animal(weight: {}. color {})".format(self.weight,self.color)

class Mammal(Animal):
    def __init__(self,weight=None,color=None, furry =None):
        super(). __init__(weight,color)
        self.furry=furry

    def __str__(self):
        return "Mammal({},{})".format(self.weight,self.furry)


# create new object and define value of attributes
print("Creating animal")

a=Animal(30,"red")
print(a)
print(a.weight)

b=Animal(40)
print(b)

c=Mammal(30,"red","full")
print(c)