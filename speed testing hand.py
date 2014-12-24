#need a class for players in speed

class Player():
    def __init__(self, ID, name):
        self.ID = ID
        self.name = name
        img = ''#maybe

    #def newHand(cards):
        


class Hand():
    def __init__(self, p1,p2,p3,p4,p5,dealp):#p for pile
        pass


def deal(cards):
    if len(cards) < 15:
        print("you've won")
    else:
        count = 0
        ps = []#piles
        for i in range(5):
            array = []
            lim = count+i+1
            for j in range(count, lim):
                array.append(cards[j])
            ps.append(array)
            count = lim
        ps.append([cards[x] for x in range(count, len(cards))])
        return ps

deck = [x for x in range(52)]
p1Hand = [deck[x] for x in range(0,int(len(deck)/2))]
p2Hand = [deck[x] for x in range(int(len(deck)/2), len(deck))]

p1ps = deal(p1Hand)
p2ps = deal(p2Hand)
    


        
