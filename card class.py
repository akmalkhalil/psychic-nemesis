import pygame
##from pygame.locals import *

class Card():
    def __init__(self, faceVal, suit):
        self.faceVal = faceVal
        self.suit = suit
        self.img = ''
    


##pygame.init()
##fpsClock = pygame.time.Clock()
##windowSurf = pygame.display.set_mode((640,480))
##
##num = 0

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
            deck[-1].img = pygame.image.load('C:\\Users\\Akmal\\Desktop\\Files\\games\\programs\\Playing Cards\\PNG-cards-1.3\\'+bob+'_of_'+blob+'.png')
            deck[-1].img = pygame.transform.scale(deck[-1].img,(int(deck[-1].img.get_width()/5),int(deck[-1].img.get_height()/5)))



##while True:
##    windowSurf.blit(deck[num].img,(100,100))
##
##    for event in pygame.event.get():
##        if event.type == QUIT:
##            pygame.quit()
##        elif event.type == KEYDOWN:
##            if event.key == K_UP:
##                if num == len(deck)-1:
##                    num = 0
##                else:
##                    num += 1
##            elif event.key == K_DOWN:
##                if num == 0:
##                    num = len(deck)-1
##                else:
##                    num -=1
##            if event.key == K_ESCAPE:
##                pygame.event.post(pygame.event.Event(QUIT))
##
##    pygame.display.update()
##    fpsClock.tick(30)
