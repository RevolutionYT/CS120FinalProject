 # -*- coding: utf-8 -*-
"""
    Created on Mon Nov 27 18:38:27 2023

    @author: nfost
"""
import pygame, simpleGE
class Node(object):
        def __init__(self, title, desc, aText, aIndex, bText, bIndex, dText, dIndex):
            self.title = title
            self.description = desc
            self.aText = aText
            self.aIndex = aIndex
            self.bText = bText
            self.bIndex = bIndex
            self.dText = dText
            self.dIndex = dIndex
class GameScreen(simpleGE.Scene):
        def __init__(self):
            simpleGE.Scene.__init__(self)
            self.lblTitle = simpleGE.Label()
            self.lblTitle.font = pygame.font.Font("goodfoot.ttf", 50)
            self.lblTitle.bgColor =("dark green")
            self.lblTitle.center = (320, 35)
            self.lblTitle.size = (350, 60)
            self.lblDescription = simpleGE.MultiLabel()
            self.lblDescription.font = pygame.font.Font("goodfoot.ttf", 30)
            self.lblDescription.bgColor = ("dark gray")
            self.lblDescription.center = (320,240)
            self.lblDescription.size = (640, 300)
            self.btnA = simpleGE.Button()
            self.btnA.bgColor = ("red")
            self.btnA.font = pygame.font.Font("goodfoot.ttf", 30)
            self.btnA.center = (110, 420)
            self.btnA.size = (100, 40)
            self.btnB = simpleGE.Button()
            self.btnB.bgColor = ("red")
            self.btnB.font = pygame.font.Font("goodfoot.ttf", 30)
            self.btnB.center = (530, 420)
            self.btnB.size = (100, 40)
            self.btnD = simpleGE.Button()
            self.btnD.bgColor = ("green")
            self.btnD.font = pygame.font.Font("goodfoot.ttf", 30)
            self.btnD.center = (310, 420)
            self.btnD.size = (100, 40)
            self.sprites = [self.lblTitle, self.lblDescription, 
                            self.btnA, self.btnB, self.btnD]
            self.background.fill(("dark red"))
        def loadNode(self, node):
              self.lblTitle.text = node.title
              self.lblDescription.textLines = node.description
              self.btnA.text = node.aText
              self.btnB.text = node.bText
              self.btnD.text = node.dText
              self.aIndex = node.aIndex
              self.bIndex = node.bIndex
              self.dIndex = node.dIndex
        def update(self):
            if self.btnA.clicked:
                if self.aIndex == -1:
                    self.keepGoing = False
                else:
                    self.loadNode(self.nodeList[self.aIndex])
            if self.btnB.clicked:
                if self.bIndex == -1:
                    self.keepGoing = False
                else:
                    self.loadNode(self.nodeList[self.bIndex])
            if self.btnD.clicked:
               if self.dIndex == -1:
                   self.keepGoing = False
               else:
                   self.loadNode(self.nodeList[self.dIndex])
def main():
        nodeList = []
        #0
        nodeList.append( Node(
            "Horror House" ,
            ["You were out on a casual midnight joyride" ,
             "and your car suddenly breaks down" ,
             "you look around for some help" ,
             "until you find a big, abandoned house"],
            "Go In", 2,
            "Stay Outside", 1,
            "quit", -1,
            ))
        #1
        nodeList.append( Node(
            "Smart" ,
            ["Before going in you have an amazing revalation" ,
             "Wait a minute this is the 21st century," ,
             "I got a cellphone(and unknowingly you saved yourself" ,
             "from a night of terror"],
            "Start over", 0,
            "quit", -1,
            "Reset", -1,
            ))
        #2
        nodeList.append( Node(
            "Inside" ,
            ["You have decided to go in," ,
             "and you come upon the living room of the house," ,
             "and ther is also 2 doors:" ,
             "one to the left and one to the right"],
            "Search", 3,
            "Right", 4,
            "Left", 5,
            ))
        #3
        nodeList.append( Node(
            "Iten #1" ,
            ["You search the lving room and find a submarine" ,
             "Description reads: It looks like the doors are welded shut"],
            "Living Room", 2,
            "Left", 5,
            "Right", 4,
            ))
        #4
        nodeList.append( Node(
            "Spikes" ,
            ["Welp, it turns out right isn't always" ,
             "right and you fall into a spike pit"],
            "Start over", 0,
            "quit", -1,
            "reset", 0,
            ))
        #5
        nodeList.append( Node(
            "Hallway" ,
            ["You decided to take the door on the left," ,
             "and you come into a hallway, which has 3 rooms," ,
             "a bedroom, the kitchen, and the closet"] ,
            "Bedroom", 6,
            "Kitchen", 9,
            "Closet", 11,
            ))
        #6
        nodeList.append( Node(
            "Bedroom" ,
            ["You go to the bedroom, and it's smaller" ,
             "than you expected but rather cozy"] ,
            "Search", 7,
            "Hallway", 5,
            "nap", 8,
            ))
        #7
        nodeList.append( Node(
            "Item #2" ,
            ["Teddy Bear" ,
             "Descrption: Even creepy places can feel eerily normal"] ,
            "Bedroom", 6,
            "Hallway", 5,
            "nap", 8,
            ))
        #8
        nodeList.append( Node(
            "Paralysis Demon" ,
            ["Somehow you manage to fall asleep, but" ,
             "a few minutes later you wake up parylzed" ,
             "after a few hours you relize this is life now"] ,
            "Start over", 0,
            "quit", -1,
            "reset", 0,
            ))
        #9
        nodeList.append( Node(
            "Kitchen" ,
            ["You go into the kitchen, and it" ,
             "dosen't look like anything at first," ,
             "but you look at the celing and notice some blood"] ,
            "Search", 10,
            "Hallway", 5,
            "quit", -1,
            ))
        #10
        nodeList.append( Node(
            "Item #3" ,
            ["Cornbread Descrption: You notice a cute" ,
             "little face with a smile on it"] ,
            "Hallway", 5,
            "Kitchen", 9,
            "quit", -1,
            ))
        #11
        nodeList.append( Node(
            "Closet" ,
            ["You go into the closet expeting something" ,
             "horrible, but it's uncomfortably normal compared" ,
             "to the rest of the house, but it goes in rather deep"] ,
            "Search", 12,
            "Deeper", 13,
            "Hallway", 5,
            ))
        #12
        nodeList.append( Node(
            "Iten #4" ,
            ["Bag Descrption: It has a very odd shape to it"] ,
            "Closet", 11,
            "Hallway", 5,
            "Deeper", 13,
            ))
        #13
        nodeList.append( Node(
            "Double Hallway" ,
            ["You have decided to go in deeper" ,
             "and you see it leads to another" ,
             "set of 3 rooms, the attic, the bathroom, " ,
             "and the master bedroom"] ,
            "Attic", 14,
            "MBedroom", 17,
            "Bathroom", 20,
            ))
        #14
        nodeList.append( Node(
            "Attic" ,
            ["The attic is mostly normal," ,
             "except you notice a shadowy figure" ,
             "in the corner"] ,
            "Search", 15,
            "Jump", 16,
            "Hallway", 13
            ))
        #15
        nodeList.append( Node(
            "Item #5" ,
            ["Notebook" ,
             "Descption:Attic Schmatics"] ,
            "Attic", 14,
            "Hallway", 13,
            "Jump", 16,
            ))
        #16
        nodeList.append( Node(
            "Fall" ,
            ["Who would've thought jumping out of" ,
             "the highest point of the house was a bad idea" ,
             "and you plummet to your death"] ,
            "Start over", 0,
            "quit", -1,
            "reset", 0,
            ))
        #17
        nodeList.append( Node(
            "Master Bedroom" ,
            ["You have decided to go to the master bedroom," ,
             "and the room is huge, but the entire bed," ,
             "including the matress, is made of wood"] ,
            "Search", 18,
            "Sleep", 19,
            "Hallway", 13,
            ))
        #18
        nodeList.append( Node(
            "Item #6" ,
            ["Hole Descrption: Somehow you can pick" ,
             "up a completly empty area"] ,
            "Bedroom", 17,
            "Sleep", 19,
            "Hallway", 13,
            ))
        #19
        nodeList.append( Node(
            "Restless" ,
            ["You are not well rested"] ,
            "Search", 18,
            "Bedroom", 17,
            "Hallway", 13,
            ))
        #20
        nodeList.append( Node(
            "Bathroom" ,
            ["You decide to go to the bathroom," ,
             "and it's very clean, with a strong smell" ,
             "of bleach, and there is also another door"] ,
            "Search", 21,
            "Hallway", 13,
            "Door", 22,
            ))
        #21
        nodeList.append( Node(
            "Item #7" ,
            ["Plunger" ,
             "Descrption: This reminds you of your" ,
             "first career"] ,
            "Hallway", 13,
            "Bathroom", 20,
            "door", 22,
            ))
        #22
        nodeList.append( Node(
            "End" ,
            ["You have decided to go to the mysterious door"] ,
            "Open", 23,
            "Bathroom", 20,
            "Hallway", 13,
            ))
        #23
        nodeList.append( Node(
            "Freedom" ,
            ["You open the door and your eyes are blinded" ,
             "by how much light there is outside" ,
             "You have finnaly escaped"] ,
            "Start over", 0,
            "quit", -1,
            "reset", 0,
            ))
        game = GameScreen()
        game.nodeList = nodeList
        game.loadNode(nodeList[0])
        game.setCaption("HorreryXmas House")
        game.start()  
if __name__ == "__main__":
        main()
