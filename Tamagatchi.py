# class used to define a tamagatchi and it's stats
class Pet:
    # construct class with these variables
    def __init__(self, name, age, exp, food, filth, fun):
        self.name = name # name, used for filename of stored Pet
        self.age = age # how old in minutes the tamagatchi is since creation
        self.exp = exp # arbitrary points for something
        
        self.food = food # stat for non-hungeriness
        self.filth = filth # stat for cleansliness
        self.fun = fun # stat for not boredem-ness


        # defaults for survival stats, or the 'f' stats
        # these stats should always start at max
        # decrease over time
        # something dying related when ANDOR these 0 is true
        food = 10
        filth = 10
        fun = 10


        # defaults for tracked stats
        # always start at 0
        # change over time, should only increase
        age = 0
        exp = 0
