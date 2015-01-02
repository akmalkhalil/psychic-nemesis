import pygame
from pygame.locals import *
import random#go through and replace andom.randint with randint
from random import randint

#copied from 'card class.py'
class Card():
    def __init__(self, faceVal, suit):
        self.faceVal = faceVal
        self.suit = suit
        self.img = ''
        self.facing = "DOWN"#can also be set to UP
deck = []
suits = ('♠', '❤', '♣', '♦')
for i in range(4):
    if i == 0:#this'd be a great place for a case/switch
        blob = 'spades'
    elif i == 1:
        blob = 'hearts'
    elif i == 2:
        blob = 'clubs'
    elif i == 3:
        blob = 'diamonds'
    for j in range(1,14):
            if j == 1:
                face = 'A'
                bob = 'ace'
            elif j == 11:
                face = 'J'
                bob = 'jack'
            elif j == 12:
                face = 'Q'
                bob = 'queen'
            elif j == 13:
                face = 'K'
                bob = 'king'
            else:
                face = str(j)
                bob = face
            deck.append(Card(face,suits[i]))
            deck[-1].img = pygame.image.load('Playing Cards\\PNG-cards-1.3\\'+bob+'_of_'+blob+'.png')
            deck[-1].img = pygame.transform.scale(deck[-1].img,(int(deck[-1].img.get_width()/5),int(deck[-1].img.get_height()/5)))
#copied from 'card class.py'

class Pile():
    #if i'm making pile a class should deck also be a class
    #technically isn't deck a pile -> so use inheritance???
    def __init__(self, size, cardsA):
        self.n = int(size)#make sure it's an interger
        self.topCard = cardsA[-1]#when i 'deal' i'll be appending it
        #so the top card in real life will be the last one appended
        cardsA.remove(self.topCard)
        self.faceUpCards = [cardsA[x] for x in range(0,len(cards),1) if cardsA[x].facing == "UP"]
        #this time don't go backwards because we'll go backwards when we go through faceUpCards
        self.faceDownCards = [cardsA[x] for x in range(0,len(cards),1) if cardsA[x].facing == "DOWN"]
        if len(self.faceDownCards)+len(self.faceUpCards) != len(cardsA):
            print("we may have a problem")
        

def OHshuffle(cards):#over hand
    percentRange = (0.5,0.75)#26-32 although i got 35,34 mostly
    L = len(cards)
    packet = [cards[x] for x in range(0,random.randint(int(len(cards)*percentRange[0]),int(len(cards)*percentRange[1])))]
    for i in range(len(packet)):
        cards.remove(packet[i])
    numShuffles = random.randint(2,5)
    if (numShuffles == 2 or numShuffles == 5) and random.randint(0,2) != 2:
        numShuffles = 4
    #when i was shuffling i got 4s mostly and some 3s and vary rare 2s or 5s
    #i just made up the probs
    print(numShuffles)
    print(len(cards))
    count = 0
    #for i in range(numShuffles):
    while len(cards) != L:
        count+=1
        print(len(cards))
        drop = []
        if count == numShuffles -1:
            drop = packet
            drop.append("test")
            print("bob")
        else:
            drop = [packet[x] for x in range(0,random.randint(int(len(packet)*percentRange[0]),int(len(packet)*percentRange[1])))]
            #i couldnt be bothered to figur out % so i'll use same as earlier
        cards += drop
        for j in range(len(drop)):
            packet.remove(drop[j])
        
        
                
    return cards
def UHshuffle(cards):#underhand
    percentRanges((1/13,0.25),(0.65,0.85))
    #midPacket = [cards[x] for x in range(int(len(cards)*percentRange[0][0])
        
def comShuffle(cards):
    shuffled = []
    for i in range(len(cards)):
        n = randint(0,len(cards)-1)
        shuffled.append(cards[n])
        cards.remove(cards[n])
    return shuffled
    

deck = comShuffle(deck)







##
##pygame.init()
##fpsClock = pygame.time.Clock()
##windowSurf = pygame.display.set_mode((960,680))
##pygame.display.set_caption("Speed!!!")
##windowW = windowSurf.get_width()
##windowH = windowSurf.get_height()
##
##
##
##pygame.quit()
