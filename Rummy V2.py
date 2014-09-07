#lets try rummy from scratch
import pygame,random,time
from pygame.locals import *

class Card():
    def __init__(self, f, s):
        self.face = f
        self.suit = s
        self.img = ''
        
class Player():
    def __init__(self,n):
        self.name = n
        self.chips = 100
        self.img = 'hmm'
        self.hand = []
#maybe i could make a chips object aswell

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


#put in the whole archittecture/the stuff i need to build the game frst
#then start pygame

numPlayers = 3
players = []
for i in range(numPlayers):
    players.append(Player('bob'+str(i)))


def shuffleDeck():
    global deck
    shuffled = []
    for i in range(len(deck)):
        rand = random.randint(0,len(deck)-1)
        shuffled.append(deck[rand])
        deck.remove(deck[rand])
    deck = shuffled

def deal():
    randCard = deck[0]
    deck.remove(deck[0])
    return randCard

def startHand():
    for i in range(numPlayers):
        for j in range(7):
            players[i].hand.append(deal())


shuffleDeck()
startHand()

##for i in range(len(players)):
##    print(players[i].name)
##    for j in range(len(players[i].hand)):
##        print(players[i].hand[j].face,players[i].hand[j].suit)
    
discardPile = [deal()]

def choosePile(person):
    print('take card from (1)discard pile or from (2)deck')
    choice =0
    while choice not in [1,2]:
        try:
            choice = int(input('enter 1 or 2:  '))#need to change this later
            #so that you can click on the pile
        except ValueError:
            print('enter a number')
    if choice == 1:
        card = discardPile[0]
        discardPile.remove[card]
    if choice == 2:
        card = deal()
    person.hand.append(card)

def discardCard(cards):
    global discardPile
    #cards = person[x].hand

    #again need to change this later so that they click on the card to discard
    

    print('choose which card to discard')
    for i in range(len(cards)):
        print('('+str(i)+')',cards[i].face,cards[i].suit)
    choice = int(input())
    going = cards[choice]
    cards.remove(going)
    discardPile.insert(0,going)
    


        
        
