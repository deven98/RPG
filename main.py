from Story import Story
from Menus import Menu

#Write main code here
#Maybe a sequence and a menu class too?

print("Welcome to <placeHolder>!")

mainInput = Menu.mainMenu()

if int(mainInput) is 1:
    Story.shortStory()