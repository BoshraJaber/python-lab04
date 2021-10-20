from abc import ABC, abstractmethod, abstractstaticmethod, abstractclassmethod

class Musician(ABC):
    members=[]
    def __init__(self, name, members=[]):
        self.name = name
        Musician.members.append(self)

    @abstractstaticmethod # It gave me an error so I put static and it is solved
    def get_instrument(cls):
        pass

    # @abstractmethod
    # def play_solo():
    #     pass

class Band(Musician):
    def play_solos():
        return "Play solo"
    
    def to_list():
        return Musician.members
    @staticmethod
    def get_instrument():
        return "band"

    

 



# Start with Guitarist,Bassist, and Drummer.
# A Band instance should have a play_solos method that asks each member musician to play a solo, in the order they were added to band.
# A Band should have a class method to_list which returns a list of previously created Band instances

class Guitarist(Band):
   
    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"
        
    def __str__(self):
        return f"My name is {self.name} and I play guitar"
    @staticmethod
    def get_instrument():
        return "guitar"


class Drummer(Band):
   
    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"
        
    def __str__(self):
        return f"My name is {self.name} and I play drums"

    @staticmethod
    def get_instrument():
        return "drums"

        

class Bassist(Band):
   
    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"
        
    def __str__(self):
        return f"My name is {self.name} and I play bass"
    @staticmethod
    def get_instrument():
        return "bass"