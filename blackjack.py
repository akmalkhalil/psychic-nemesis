"""
BLACKJACK GAME
Author: Akmal Khalil
"""
import time, random, Deck2
players = [['playerNum', 'hand', 'chips', 'bet', 'score']]
##class Deck:
##    suits = ('♠', '❤', '♣', '♦')
##    numOfDecks = 2
##    #this will be a parameter of __init__
##    cardsDict = {}
##    for h in range (4*numOfDecks):
##        cardsDict[len(cardsDict)+1] = 'A' + suits[h%4]
##        for i in range (len(cardsDict) + 1 , len(cardsDict)+10 , 1):
##            cardsDict [i] = str(i%13) + suits[h%4]
##        cardsDict[len(cardsDict) + 1] = 'J' + suits[h%4]
##        cardsDict[len(cardsDict) + 1] = 'Q' + suits[h%4]
##        cardsDict[len(cardsDict) + 1] = 'K' + suits[h%4]
##    def randCard(self):
##        working = True
##        while working:
##            try:
##                randNum = random.randint(1,len(self.cardsDict))
##                if randNum in self.cardsDict:
##                    working = False
##                    return self.cardsDict[randNum], randNum
##            except KeyError:
##                pass
##    def remCard(self,card):
##        #(self.cardsDict).pop(card)
##        del self.cardsDict[card]
deck1 = DeckV2.Deck(2)

def numOfPlayers():
    while True:
        print("how many players will there be")
        try:
            n = int(input())
            break
        except ValueError:
            print("you didn't enter an interger")
    for i in range(n):
        players.append(['player'+str(i+1), 'I\'ll do the hand here', 100, 0, 0])
        #print(players[i+1], 'has been created')
    playerNames()
def initHand(deck):
    for i in range(1,len(players)):
        players[i][1] = [deal(deck),deal(deck)]

def deal(deck):
    if isinstance(deck, DeckV2.Deck):
        dealt, randNum = deck.randCard()
        deck.remCard(randNum)
        return dealt
    else:
        return 'death'

def getValue(card):
    x = 0
    if isinstance(card, str ):
        try:
            if len(card) == 2:
                x = int(card[0])
            else:
                x = 10
        except ValueError:
            y = {'A' : 1 , 'K' : 13 , 'Q' : 12 , 'J' : 11}
            x = y[card[0]]
        return x
    else:
        return 'death'

def aceVal():
    print (" do you want the ace to be 11 or 1")
    done = False
    while done == False:
        opt = input()
        if (opt == '11') or (opt == '1') :
            done = True
            return opt
        else:
            print("you didn't enter a 11 or 1")
            done = False
def sumVals(cards, user):
    score = 0
    if isinstance(cards, list):
        for i in range(len(cards)):
            value = getValue(cards[i])
            if 1<value<11:
                score += value
            elif value > 10 :
                score += 10
            elif value == 1:
                if user == 'com':
                    if len(cards) == 2:
                        score += 11
                    else:
                        score += 1
                else:
                    score += int(aceVal())
        return score
    else:
        return 'death'

def blackjack():
    global players
    print()
    print("NEW HAND")
    time.sleep(0.3)
    for i in range(1, len(players)):
        print(players[i][0], ':')
        players[i][2],players[i][3] = placeBet(players[i][2])
        initHand(deck1)
        print ("Your hand is", players[i][1])
        time.sleep(0.5)
        players[i][4] = sumVals(players[i][1], '')
        print("your score therefore is:" , players[i][4])
        time.sleep(0.5)
        stand = False
        if players[i][4] == 21:
            stand = True
            print("WINNER WINNER, CHICKEN DINENR")
        while stand == False and players[i][4] < 21:
            stand = hit(players[i][1], stand)
            time.sleep(0.5)
            print ("Your hand is", players[i][1])
            players[i][4] = sumVals(players[i][1],'')
            time.sleep(0.5)
            print("your score therefore is:" , players[i][4])
            if players[i][4] > 21:
                print ("BUST")
            if players[i][4] == 21:
                print("you must stick with 21")
        print()
        print()
    cHand, cPoints = comBlackjack()
    whoWins(cHand,cPoints)    
    
def hit(cards,thingy):
    #the thingy is going to be stand but i want parameter and argument to be different
    print ("""would you like to:
          (1)hit
          (2)stand""")
    try:
        opt = int(input())
        if 0<opt<3:
            if opt == 1:
                dealt = deal(deck1)
                cards.append(dealt)
                print ("you recieved: ",dealt)
                return False
            if opt == 2:
                return True
        else:
            print("I dont think you entered a 1 or a 2")
            return False
    except ValueError:
        print("i dont think you typed in a number")
        return False
    
def comBlackjack():
    print("now it's the computers  turn")
    time.sleep(1.5)
    hand = [deal(deck1), deal(deck1)]
    print ("computers hand is: ", hand)
    points = sumVals(hand,'com')
    time.sleep(0.5)
    stand = False
    while stand == False:
        points = sumVals(hand, 'com')
        print("the score therefore is:" , points)
        if len(hand) == 2 and int(points) == 21:
            stand = True
            print ('WINNER WINNER, CHICKEN DINNER')
        else:
            if int(points) > 16:
                print("the computer stands with the hand", hand)
                print ('with a score of', points)
                stand = True
            else:
                dealt = deal(deck1)
                hand.append(dealt)
                print("the hand now is", hand)
        time.sleep(1)
    return hand, points
    
def whoWins(cCards, cScore):
    global players
    print()
    print()
    print()
    print()
    time.sleep(1)
    for i in range (1, len(players)):
        print (players[i][0], ' hand is:')
        print(players[i][1])
        time.sleep(0.5)
    print('The Dealers hand is:')
    print(cCards)
    time.sleep(0.6)
    for i in range(1, len(players)):
        print()
        print(players[i][0], ':')
        if players[i][4] > 21:
            print ("you are BUST so the Dealer wins")
            players[i][3] = 0
            print("you now have", players[i][2], 'chips')
        elif players[i][4] == 21 and len (players[i][1]) == 2:
            print("YOU WIN")
            players[i][2] = players[i][2] + players[i][3] * 2.5
            players[i][3] = 0
            print("you now have", players[i][2],'chips')
        else:
            if players[i][4] > cScore:
                print("YOU WIN")
                players[i][2] = players[i][2] + players[i][3] * 2
                players[i][3] = 0
                print("you now have", players[i][2], 'chips') 
            elif cScore > 21:
                print("YOU WIN")
                players[i][2] = players[i][2] + players[i][3]*2
                players[i][3] = 0
                print("you now have", players[i][2], 'chips')
            else:
                print("YOU LOSE to the dealer")
                players[i][3] = 0
                print("you now have", players[i][2], "chips")

def placeBet(money):
    #calling chips money just so i have summat different in function
    print("you have", money, "chips")
    time.sleep(0.4)
    done = False
    while done == False:
        print("how much would you like to bet?")
        try:
            stake = int(input())
            if stake >= 20 and stake <= money:
                done = True
            elif stake < 20:
                done = False
                print("that's below the minimum bet")
            elif stake > money:
                print(" you don't have than many chips")
        except ValueError:
            print("you didn't enter an integer")
            done = False
    print ("you have placed a bet of", stake)
    money = money - stake
    return money, stake
    


def playerNames():
    for i in range(1, len(players)):
        print('enter '+(players[i][0])+'\'s name?')
        name = input()
        players[i][0] = name
        print("welcome to the game " + name)
        print()
#need to define function before main progeam thing

def newDeck():
    print ("I'm now creating a new deck")
    #if i do summat here then i'll have to change it every where
    #need to think what i'm gonna do here first


print("this crappy game was created by Akmal Khalil")
print("NOTE: IF TIE, DEALER WINS BY DEFAULT")
print("MINIMUM BET IS 20")
print("This deck begins with", len(deck1.cardsDict), 'cards')
for i in range(5):
    time.sleep(1)
    print(deck1.suits)
time.sleep(0.8)
print("WELCOME TO BLACKJACK")
time.sleep(0.4)
numOfPlayers()
while True :
    blackjack()
    time.sleep(0.5)
##    if chips < 20:
##        print("you no longer have enough chips to place a bet")
##        break
    #great now i've got a problem here
    #apart from this it's working
    if len(deck1.cardsDict) < (len(players)*5):
        print("sorry there are not enough cards left in this deck")
        time.sleep(0.3)
        print("you  have", chips, "chips remaining")
        break



    
#purple dinosaur has sent me a thing for multiplayer on multiple omputers
#he wanted to play each screen, back to back
# like battleships
#i should make a battleships game

 

#bug
#if player runs out of chips they can still place bets
#need to figure out where to correct this


#bug:
#AceVal('com')
#if dealer recieves 2 aces
#if dealer recieves 6 to 13 & A

