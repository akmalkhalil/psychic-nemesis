import pygame
from pygame.locals import *
import random


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

    def showButton(self,surface):#stick in an if statement so that it's not shown twice
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
#the other bit from myButtons
#i wrote this one over summer i think, now it's april so a while ago
class SwitchB():
    def __init__(self, rect, switch, text = "", Fsize = 12):
        self.rect = rect
        if isinstance(switch, bool):
            self.switch = switch
            self.onColour = pygame.color.Color(0,255,0)
            self.offColour = pygame.color.Color(255,0,0)
            self.colour = self.offColour
        elif isinstance(switch, list):
            self.switch = switch
            self.colour = pygame.color.Color(0,0,255)
            self.l = len(switch)
            self.stateN = 0
            self.colourA = []#stick in a comprehension so set the colours
        else:
            raise TypeError('switch must be a bool type or a list type or a function')
        self.text = text
        self.Fsize = Fsize

    def pressButton(self):
        if isinstance(self.switch, bool):
            self.switch = not self.switch
        else:
            self.stateN += 1
            if self.stateN == self.l:
                self.stateN = 0
                

    def getState(self):
        if isinstance(self.switch, bool):
            return self.switch
        else:
            return self.switch[self.stateN]
            
        
    def showButton(self,surface):
        if isinstance(self.switch, bool):
            if self.switch:
                colour = self.onColour
            else:
                colour = self.offColour
        else:
            if len(self.colourA) == self.l:
                colour = self.colourA[self.stateN]
            else:
                colour = self.colour
        pygame.draw.rect(surface, colour, self.rect)
        if len(self.text) > 0:
            font = pygame.font.Font('freesansbold.ttf',self.Fsize)
            msgSurfObj = font.render(self.text, False, pygame.color.Color(0,0,0))
            msgRectObj = msgSurfObj.get_rect()
            msgRectObj.center = (self.rect[0] + int(self.rect[2]/2), self.rect[1] + int(self.rect[3]/2))
            windowSurf.blit(msgSurfObj, msgRectObj)

        

    def Xstartstop(self):#the start and end of the x co-ords where button is
        return self.rect[0],self.rect[0]+self.rect[2]

    def Ystartstop(self):
        return self.rect[1],self.rect[1]+self.rect[3]

#setting up the cards and the deck
class Card():
    def __init__(self, faceVal, suit,faceN):
        self.faceVal = faceVal
        self.suit = suit
        self.img = ''
        self.faceN = faceN
        
num = 0
deck = []
suits = ('♠', '❤', '♣', '♦')
CARDWIDTH = 75
CARDHEIGHT = int(3* 145/4)#i hope
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
            deck.append(Card(face,suits[i],j))
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

def shuffleDeck(deck):
    shuffled = []
    temp = [deck[x] for x in range(len(deck))]
    for i in range(len(deck)):
        rand = random.randint(0,len(deck)-1)
        shuffled.append(deck[rand])
        deck.remove(deck[rand])
    deck = [temp[x] for x in range(len(temp))]
    return shuffled, deck

##def deal2(hand,deck):
##    cards = [deck.pop(),deck.pop()]
##    hand.append(cards[0])
##    hand.append(cards[1])
def dealN(hand, deck, n):
    cards = [deck.pop() for x in range(n)]
    for i in range(n):
        hand.append(cards[i])
        if cards[i].faceVal == 'A':
            #aceB = SwitchB((10+i*(CARDWIDTH+5),100+CARDHEIGHT+10,80,30), [1,11], text = "umm shouldnt this change?")
            #aceBs.append(aceB)
            aceBs[cards[i]] = SwitchB((0,0,0,0), [1,11], text = "umm shouldnt this change?")
            aceBs[cards[i]].colourA = [pygame.Color(255,0,0),pygame.Color(0,0,255)]
def calcScore(hand):
    score = 0
    for i in range(len(hand)):
        if 1<hand[i].faceN<11:
            score += hand[i].faceN
        elif 10<hand[i].faceN<14:
            score +=10
        elif hand[i].faceN == 1:
            score+=aceBs[hand[i]].getState()
##            oneB = Button((10+i*(CARDWIDTH+5),100+CARDHEIGHT+10,80,30),lambda:print("1"))
##            elevenB = Button((10+i*(CARDWIDTH+5),100+CARDHEIGHT+10+30+5,80,30), lambda:print("11"))
##            aceBs.append([oneB,elevenB])
##            aceB = SwitchB((10+i*(CARDWIDTH+5),100+CARDHEIGHT+10,80,30), [1,11], text = "umm shouldnt this change?")
##            aceBs.append(aceB)
    return score

def displayText(surface,text,topLeft):
    textSurf = fontObj.render(str(text), False, colour['blue'])
    textRect = textSurf.get_rect()
    textRect.topleft = topLeft
    surface.blit(textSurf, textRect)
    


    

pygame.init()
fpsClock = pygame.time.Clock()
windowSurf = pygame.display.set_mode((960,480))
pygame.display.set_caption("yeah")
windowW = windowSurf.get_width()
windowH = windowSurf.get_height()

colour = {
    'red' : pygame.Color(255,0,0),
    'green' : pygame.Color(0,255,0),
    'blue' : pygame.Color(0,0,255),
    'white' : pygame.Color(255,255,255),
    'magenta' : pygame.Color(255,0,255),
    'yellow' : pygame.Color(255,255,0),
    'cyan' : pygame.Color(0,255,255),
    'black' : pygame.Color(0,0,0),
    'silver' : pygame.Color(192,192,192)
}
colour2 = {}
file = open ('C:\\Users\\Akmal\\Desktop\\Files\\500+ colours.csv','r')
lines = file.readlines()
file.close
colName = ''
red = 0
green = 0
blue =0
for i in range(1,len(lines)):
    row = lines[i].split(',')
    colName = str(row[0])
    red,green,blue = int(row[4]),int(row[5]),int(row[6])
    colour2[colName] = pygame.color.Color(red,green,blue)
del red,green,blue
fontObj = pygame.font.Font('freesansbold.ttf',32)


mouseX,mouseY = 0,0


myHand = []
shuffledD, deck = shuffleDeck(deck)

deal2B = Button((200,windowH-125,80,40), lambda:dealN(myHand,shuffledD,2), text = "deal2")
deal1B = Button((300,windowH-125,80,40), lambda:dealN(myHand, shuffledD, 1), text = "deal1")
aceBs = {}#maybe i should have aceBs as a class
#I've had to change it three times now and i have to do it throughout the program
#if i have it as a class I'll just have to change it in the class???

totalScore = 0

#deal2(myHand,shuffledD)
running = True
while running:
    windowSurf.fill(colour['green'])
    
    handSize = len(myHand)
    for i in range(handSize):
        windowSurf.blit(myHand[i].img, (10+i*(CARDWIDTH+5), 100))
        if myHand[i] in aceBs:
            aceBs[myHand[i]].rect = (10+i*(CARDWIDTH+5),100+CARDHEIGHT+10,CARDWIDTH,20)
            aceBs[myHand[i]].showButton(windowSurf)
            #print("I feel so awesome right now")
        
    
    deal2B.showButton(windowSurf)
    deal1B.showButton(windowSurf)
##    for i in range(len(aceBs)):
##        aceBs[i][0].showButton(windowSurf)
##        aceBs[i][1].showButton(windowSurf)
##    for i in range(len(aceBs)):
##        aceBs[i].showButton(windowSurf)
    
    
    displayText(windowSurf, totalScore, (windowW-75,10))
    
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
                    totalScore = calcScore(myHand)
                    #may need to copy this elsewhere when other things are done
            deal1Bco_ords = [deal1B.get_Xs(), deal1B.get_Ys()]
            if deal1Bco_ords[0][0]<mouseX<deal1Bco_ords[0][1]:
                if deal1Bco_ords[1][0]<mouseY<deal1Bco_ords[1][1]:
                    deal1B.pressButton()
                    totalScore = calcScore(myHand)
                    #may need to copy this elsewhere when other things are done

            for key in aceBs.keys():#dont think i need the i just do it with .keys()
                co_ords = [aceBs[key].Xstartstop(), aceBs[key].Ystartstop()]
                if co_ords[0][0] < mouseX < co_ords[0][1]:
                    if co_ords[1][0] < mouseY < co_ords[1][1]:
                        aceBs[key].pressButton()
                        print(aceBs[key].getState())
                        totalScore = calcScore(myHand)
                        #may need to copy this elsewhere when other things are done
            


















print("and the programs ended")
