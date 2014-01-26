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
        self.cardsList = []
        for h in range (4*n):
            self.cardsList.append('A' + self.suits[h%4])
            for i in range (len(self.cardsList) + 1 , len(self.cardsList)+10 , 1):
                self.cardsList.append(str(i%13) + self.suits[h%4])
            self.cardsList.append('J' + self.suits[h%4])
            self.cardsList.append('Q' + self.suits[h%4])
            self.cardsList.append('K' + self.suits[h%4])

        del(h)
        del(i)

    def randCard(self):
        working = True
        while working:
            try:
                randNum = random.randint(0,len(self.cardsList)-1)
                working = False
                return self.cardsList[randNum], randNum
            except KeyError:
                pass

    def kill(self):
        try:
            self.cardsList.clear()
            self.facesDict.clear()
            print (self , 'has been killed')
        except:
            print("why won't you die")

    def remCard(self,card):
        #(self.cardsDict).pop(card)
        del self.cardsList[card]

        
