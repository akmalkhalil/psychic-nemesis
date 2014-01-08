"""
BLACKJACK GAME
Author: Akmal Khalil
"""
import time, random

class Deck:
    suits = ('♠', '❤', '♣', '♦')
    cardsDict = {}
    for h in range (4):
        cardsDict[len(cardsDict)+1] = 'A' + suits[h]
        for i in range (len(cardsDict) + 1 , len(cardsDict)+10 , 1):
            cardsDict [i] = str(i%13) + suits[h]
        cardsDict[len(cardsDict) + 1] = 'J' + suits[h]
        cardsDict[len(cardsDict) + 1] = 'Q' + suits[h]
        cardsDict[len(cardsDict) + 1] = 'K' + suits[h]

    def randCard(self):
        working = True
        while working:
            try:
                randNum = random.randint(1,52)
                if randNum in self.cardsDict:
                    working = False
                    return self.cardsDict[randNum], randNum
            except KeyError:
                pass
        
    def remCard(self,card):
        #(self.cardsDict).pop(card)
        del self.cardsDict[card]
deck1 = Deck()


def deal(deck):
    if isinstance(deck, Deck):
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
    global chips, bet
    print()
    print("Whats your name")
    player = input()
    time.sleep(0.5)
    print ("Hello " +player)
    player = 'player'
    #that't to stop them typing 'com' although i myt make that default
    time.sleep(0.2)
    hand = [deal(deck1), deal(deck1)]
    chips, bet = placeBet(chips)
    print ("Your hand is", hand)
    time.sleep(0.5)
    points = sumVals(hand, player)
    print("your score therefore is:" , points)
    time.sleep(0.5)
    stand = False
    if points == 21:
        stand = True
        print("WINNER WINNER, CHICKEN DINENR")
    while stand == False and points < 21:
        stand = hit(hand, stand)
        time.sleep(0.5)
        print ("Your hand is", hand)
        points = sumVals(hand,player)
        time.sleep(0.5)
        print("your score therefore is:" , points)
        if points > 21:
            print ("BUST")
    print()
    print()
    cHand, cPoints = comBlackjack()
    whoWins(hand, cHand, points, cPoints)
        
    
    
def hit(cards,thingy):
    #the thingy is going to be stand but i want parameter and argument to be dif
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
    

    
def whoWins(pCards, cCards, pScore, cScore):
    #p for player
    #c for computer
    global bet, chips
    print()
    print()
    print()
    print()
    time.sleep(1)
    print ('Your hand is:')
    print(pCards)
    time.sleep(0.5)
    print('The Dealers hand is:')
    print(cCards)
    time.sleep(0.6)
    if pScore > 21:
        print ("you are BUST so the Dealer wins")
        bet = 0
        print("you now have", chips, 'chips')
    elif pScore == 21 and len (pCards) == 2:
        print("YOU WIN")
        chips = chips + bet * 2.5
        bet = 0
        print("you now have", chips,'chips')
    else:
        if pScore > cScore:
            print("YOU WIN")
            chips = chips + bet * 2
            bet = 0
            print("you now have", chips, 'chips') 
        elif cScore > 21:
            print("YOU WIN")
            chips = chips + bet*2
            bet = 0
            print("you now have", chips, 'chips')
        else:
            print("YOU LOSE to the dealer")
            bet = 0
            print("you now have", chips, "chips")

    

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


    
chips, bet = 100, 0
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

while True :
    print('there are', len(deck1.cardsDict), 'cards left')
    #get rid of this line when done
    blackjack()
    if chips < 20:
        print("you no longer have any chips")
        break
    if len(deck1.cardsDict) < 10:
        print("sorry there are not enough cards left in this deck")
        time.sleep(0.3)
        print("you  have", chips, "chips remaining")
        break
    
#now how to get multiplayer?????
#i seem to get a J straight if my score is 14
    #it's just happened 3 times in a row



