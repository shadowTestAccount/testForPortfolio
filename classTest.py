

# test main Class Animal

class Animal(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.kind = 'animal'
        self._num_of_legs = 0

    def show_info(self):
        print "This is a {0} and it's name is {1} and age {2}".format(self.kind.upper(),self.name,str(self.age))
        
    def show_params(self):
        if self._num_of_legs == 0:
            print "I can fly ({})".format(self._num_of_legs)
        else:
            print "I have {} legs".format(self._num_of_legs)

    
# class Dog is extension of the Animal class
class Dog(Animal):
    def __init__(self,name,age,bark_phrase):
        super(Dog,self).__init__(name,age)
        self.bark_phrase = bark_phrase
        self.kind = 'dog'
        #self.num_of_legs = 4
        

    def bark(self):
        print 'Wof wof {}'.format(self.bark_phrase)
        


animal1 = Animal('Rex',3)
animal1.show_params()
animal1._num_of_legs = 2
animal1.show_params()

dog1 = Dog('Rex',3,'cokies!!')
dog1.show_params()
