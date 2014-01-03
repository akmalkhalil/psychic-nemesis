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
        return self.cardsDict[random.randint(1, 52)]
deck1 = Deck()


def deal(deck):
    if isinstance(deck, Deck):
        dealt = deck.randCard()
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
    print("Whats your name")
    player = input()
    time.sleep(0.5)
    print ("Hello " +player)
    time.sleep(0.2)
    hand = [deal(deck1), deal(deck1)]
    print ("Your hand is", hand)
    time.sleep(0.5)
    points = sumVals(hand, player)
    print("your score therefore is:" , points)
    time.sleep(0.5)
    stand = False
    if points == 21:
        stand = True
        print("BLACKJACK")
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
    array = comBlackjack()
    cPoints = array[1]
    cHand = array [0]
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
    print("the score therefore is:" , points)
    stand = False
    while stand == False:
        points = sumVals(hand, 'com')
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
                print("the score = ", points)
        
              
        time.sleep(1)
    return [hand, points]
    

    
def whoWins(pCards, cCards, pScore, cScore):
    #p for player
    #c for computer
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
    elif pScore == 21 and len (pCards) == 2:
        print("YOU WIN")
    else:
        if pScore > cScore:
            print("YOU WIN")
        elif cScore > 21:
            print("YOU WIN")
        else:
            print("YOU LOSE to the dealer")

    


print()
blackjack()
