class Animal:

    def func1(self):
        print ('Animals can make voice')

class Dog(Animal):

    def func2(self):
        print ('Dog say bow bow... ')

class Animal2:

    def func3(self):
        print ('Animals can make voice')

class Puppy(Dog,Animal2):

    def func4(self):
        print ('Puppy can say bow bow...')



object = Puppy()
object.func1()
object.func2()
