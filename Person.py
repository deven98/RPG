# Documentation : Hero and enemy classes inherit from Person class

class Person(object):
    def __init__(self,hp,mp):
        self.hp = hp
        self.mp = mp

    def takeDamage(self,damage):
        self.hp = self.hp - damage
