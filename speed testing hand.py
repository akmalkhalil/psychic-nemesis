#best name i could come up with#

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
        return ps

deck = [x for x in range(52)]
p1Hand = [deck[x] for x in range(0,int(len(deck)/2))]
p2Hand = [deck[x] for x in range(int(len(deck)/2), len(deck))]

if len(p1Hand)<15:
    print("p1 Has won")
elif len(p2Hand)<15:
    print("p2 ahs won")
else:
    p1p1 = p1Hand[0]
    p1p2 = [p1Hand[1],p1Hand[2]]
    p1p3 = [p1Hand[x] for x in range(3,6)]
    p1p4 = [p1Hand[x] for x in range(6, 10)]
    p1p5 = [p1Hand[x] for x in range(10, 16)]
    p1P  = [p1Hand[x] for x in range(16, len(p1Hand))]


ps = []
count =0
for i in range(5):
    array = []
    lim = count +i + 1
    for j in range(count, lim):
        array.append(p1Hand[j])
    ps.append(array)
    count = lim
    


        
