import random
class Deck(object):
    facesDict = { 1:'A'}
    for i in range (2,11,1):
        facesDict[i] = str(i)
    facesDict [11] = 'J'
    facesDict [12] = 'Q'
    facesDict [13] = 'K'
    del(i)
    suits = ('♠', '❤', '♣', '♦')
    def __init__(self,n):
        #just checked out classes on codecademy and they say use this initialise thing
        self.cardsDict = {}
        for h in range (4*n):
            self.cardsDict[len(self.cardsDict)+1] = 'A' + self.suits[h%4]
            for i in range (len(self.cardsDict) + 1 , len(self.cardsDict)+10 , 1):
                self.cardsDict [i] = str(i%13) + self.suits[h%4]
            self.cardsDict[len(self.cardsDict) + 1] = 'J' + self.suits[h%4]
            self.cardsDict[len(self.cardsDict) + 1] = 'Q' + self.suits[h%4]
            self.cardsDict[len(self.cardsDict) + 1] = 'K' + self.suits[h%4]   

        del(h)
        del(i)

    def randCard(self):
        return self.cardsDict[random.randint(1, 52)]

    def kill(self):
        try:
            self.cardsDict.clear()
            self.facesDict.clear()
            print (self , 'has been killed')
        except:
            print("why won't you die")

    def remCard(self,card):
        #(self.cardsDict).pop(card)
        del self.cardsDict[card]
    
                       


##deck1 = Deck(1)
##deck2 = Deck(2)
##print ("the object 'deck1' has been created")
##print ("the object 'deck2' has been created")



