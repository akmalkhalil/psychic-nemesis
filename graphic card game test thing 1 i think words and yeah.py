import pygame
from pygame.locals import *

#from myButtons import Button
class Button():#based on the code from my previous attempt at a button
    def __init__(self, rect, command, text = "", Fsize = 12):
        self.rect = rect
        self.command = command
        self.text = text
        self.Fsize = Fsize
        self.colour = (255,255,255)

    def pressButton(self):
        self.command()

    def showButton(self,surface):
        pygame.draw.rect(surface, self.colour, self.rect)
        font = pygame.font.Font('freesansbold.ttf',self.Fsize)
        msgSurfObj = font.render(self.text, False, pygame.color.Color(0,0,0))
        msgRectObj = msgSurfObj.get_rect()
        msgRectObj.center = (self.rect[0] + int(self.rect[2]/2), self.rect[1] + int(self.rect[3]/2))
        surface.blit(msgSurfObj, msgRectObj)

    def get_Xs(self):#the start and end of the x co-ords where button is
        return self.rect[0],self.rect[0]+self.rect[2]
    def get_Ys(self):
        return self.rect[1],self.rect[1]+self.rect[3]

#setting up the cards and the deck
class Card():
    def __init__(self, faceVal, suit):
        self.faceVal = faceVal
        self.suit = suit
        self.img = ''
num = 0
deck = []
suits = ('♠', '❤', '♣', '♦')
CARDWIDTH = 100
CARDHEIGHT = 145#i hope
#picAddr = 'Playing Cards\\PNG-cards-1.3\\'##if the file is saved in the same file
picAddr = "C:/Users/Akmal/Desktop/Files/games/programs/Playing Cards/PNG-cards-1.3/"#just for now
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
            try:
                deck[-1].img = pygame.image.load(picAddr+bob+'_of_'+blob+'.png')
            except pygame.error:
                print("you you haven't saved the pics in a folder called Playing Cards and a folder called PNG-cards-1.3")
                print("copy the exact address of where the pics are saved")
                picAddr = input()
                try:
                    deck[-1].img = pygame.image.load(picAddr+bob+'_of_'+blob+'.png')
                except pygame.error:
                    print("well i tried...")
                    quit()
            #deck[-1].img = pygame.transform.scale(deck[-1].img,(int(deck[-1].img.get_width()/5),int(deck[-1].img.get_height()/5)))
            deck[-1].img = pygame.transform.scale(deck[-1].img, (CARDWIDTH, CARDHEIGHT),)
del bob,blob,face,j,i,picAddr,num


def deal2(hand,deck,shuffled = True):
    #assume it's been shuffled for now
    cards = [deck.pop(),deck.pop()]
    hand.append(cards[0])
    hand.append(cards[1])

pygame.init()
fpsClock = pygame.time.Clock()
windowSurf = pygame.display.set_mode((640,480))
pygame.display.set_caption("yeah")
windowW = windowSurf.get_width()
windowH = windowSurf.get_height()

mouseX,mouseY = 0,0


myHand = []


#deal2(myHand,deck)
running = True
while running:
    windowSurf.fill((0,0,0))

##    windowSurf.blit(deck[0].img,(10,10))
##    windowSurf.blit(myHand[0].img, (10,100))
##
##    pygame.draw.line(windowSurf, (0,255,0),(10,100),(110,100))
    
    handSize = len(myHand)
    for i in range(handSize):
        windowSurf.blit(myHand[i].img, (10+i*(CARDWIDTH+5), 100))
        
    deal2B = Button((200,windowH-125,80,40), lambda:deal2(myHand,deck), text = "deal2")
    deal2B.showButton(windowSurf)

    pygame.display.update()
    fpsClock.tick(30)
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE or event.key == K_q:
                pygame.event.post(pygame.event.Event(QUIT))
        elif event.type == QUIT:
            pygame.quit()
            running = False
        elif event.type == MOUSEMOTION:
            mouseX,mouseY = event.pos
        elif event.type == MOUSEBUTTONUP:
            deal2Bco_ords = [deal2B.get_Xs(), deal2B.get_Ys()]
            if deal2Bco_ords[0][0] < mouseX < deal2Bco_ords[0][1]:
                if deal2Bco_ords[1][0] < mouseY < deal2Bco_ords[1][1]:
                    deal2B.pressButton()




















print("and the programs ended")
