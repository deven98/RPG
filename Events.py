from Enemy import Enemy
from Hero import Hero
from random import randint

# Events contain the events that happen within a storyline. EG: A small enemy encountered for a fight.


class Events(object):
    def __init__(self):
        pass

    @staticmethod
    def smallEnemy(hero):
        print("A dwarf shows up!")
        print("Prepare to fight!")

        enemy = Enemy(40,40)

        while hero.hp > 0 and enemy.hp > 0:

            print(" ")
            print("Enemy health is " + str(enemy.hp))
            print("Hero health is " + str(hero.hp))
            print(" ")
            print("What attack do you want to use?")
            print("1.Fire")
            print("2.Water")
            print("3.Ice")
            print("4. Heal")

            attack = int(input())

            if attack is 1:
                enemy.takeDamage(10)
            elif attack is 2:
                enemy.takeDamage(15)
            elif attack is 3:
                enemy.takeDamage(12)
            elif attack is 4:
                if hero.hp < 50:
                    hero.heal(30)
                else:
                    print("Cannot heal above maximum")

                if hero.hp > 50:
                    hero.hp = 50

            else:print("Invalid prompt")

            hero.takeDamage(5*randint(1,3))

        if enemy.hp <= 0:
            print("Enemy defeated!")
        elif hero.hp <= 0:
            print("Hero defeated!")