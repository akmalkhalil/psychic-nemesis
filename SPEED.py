import pygame
from pygame.locals import *
import random

#copied from 'card class.py'
class Card():
    def __init__(self, faceVal, suit):
        self.faceVal = faceVal
        self.suit = suit
        self.img = ''
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
def OHshuffle(cards):#over hand
    percentRange = (0.5,0.75)#26-32 although i got 35,34 mostly
    packet = [cards[x] for x in range(0,random.randint(int(len(cards)*percentRange[0]),int(len(cards)*percentRange[1])))]
    for i in range(len(packet)):
        cards.remove(packet[i])
    numShuffles = random.randint(2,5)
    if (numShuffles == 2 or numShuffles == 5) and random.randint(0,2) != 2:
        numShuffles = 4
    #when i was shuffling i got 4s mostly and some 3s and vary rare 2s or 5s
    #i just made up the probs
    for i in range(numShuffles):
        if i == numShuffles -1:
            drop = packet
        else:
            drop = [packet[x] for x in range(0,random.randint(int(len(packet)*percentRange[0]),int(len(packet)*percentRange[1])))]
            #i couldnt be bothered to figur out % so i'll use same as earlier
        cards+=drop
    return cards
def UHshuffle(cards):#underhand
    percentRanges((1/13,0.25),(0.65,0.85))
    #midPacket = [cards[x] for x in range(int(len(cards)*percentRange[0][0])
        
    
    

cleanDeck = deck
shuffledDeck = OHshuffle(cleanDeck)




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
