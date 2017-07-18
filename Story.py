#Documentation : Story contains a combination of events creating a storyline. It refers to events ...(contd)
# for creating events inside the story

from Events import Events
from Hero import Hero

#Add stories that happen and storylines to play

class Story(object):
    def __init__(self):
        pass

    #temporary story
    @staticmethod
    def shortStory():

        hero = Hero(50,50)
        Events.smallEnemy(hero)