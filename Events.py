from Enemy import Enemy
from Hero import Hero
from random import randint

#Events contain the events that happen within a storyline. EG: A small enemy encountered for a fight.

class Events(object):
    def __init__(self):
        pass

    @staticmethod
    def smallEnemy():
        print("A dwarf shows up!")
        print("Prepare to fight!")
        hero = Hero(50,50)
        enemy = Enemy(40,40)

        while hero.hp>0 and enemy.hp>0:

            print(" ")
            print("Enemy health is " + str(enemy.hp))
            print("Hero health is " + str(hero.hp))
            print(" ")
            print("What attack do you want to use?")
            print("1.Fire")
            print("2.Water")
            print("3.Ice")

            attack = int(input())

            if attack is 1:
                enemy.hp = enemy.hp - 10
            elif attack is 2:
                enemy.hp = enemy.hp - 15
            elif attack is 3:
                enemy.hp = enemy.hp - 20
            else:print("Invalid prompt")

            hero.hp = hero.hp - (randint(5,9) * 2)


        if enemy.hp <= 0:
            print("Enemy defeated!")
        elif hero.hp <= 0:
            print("Hero defeated!")