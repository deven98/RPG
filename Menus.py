#Menu class has all the menus to use within the game. Declare everything as static
#to use instead of instantiating every class

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

    #include a menu to choose which story the user chooses. Maybe add completely random story lines instead of
    #using difficulty levels. Use some sort of counter to determine the progress in the game.
    #