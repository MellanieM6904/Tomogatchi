# class used to define a tamagatchi and it's stats
class Pet:
    # construct class with these variables
    def __init__(self, name):
        self.name = name # name, used for filename of stored Pet

    # survival stats, 'f' stats
    food = 10
    filth = 10
    fun = 10
    # tracked stats
    age = 0
    exp = 0
