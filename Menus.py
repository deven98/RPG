class Menu(object):
    def __init__(self):
        pass

    @staticmethod
    def mainMenu():
        print("1. New Game!")
        print("2. Resume Game!")
        print("3. Exit Game")
        a = input()
        return a