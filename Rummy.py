#i made this one in february some time or maybe before





import Deck2, time
deck = Deck2.Deck(1)
#i think it's best to only play with a single deck

players = [['playerNum', 'hand']]

def numOfPlayers():
    while True:
        print("how many players will there be")
        try:
            n = int(input())
            break
        except ValueError:
            print("you didn't enter an interger")
    for i in range(n):
        players.append(['player'+str(i+1), 'I\'ll do the hand here'])
    playerNames()
def playerNames():
    for i in range(1, len(players)):
        print('enter '+(players[i][0])+'\'s name?')
        name = input()
        players[i][0] = name
        print("welcome to the game " + name)
        print()
def initHand():
    for i in range(1,len(players)):
        hand1 = []
        for j in range(7):
            hand1.append(deal())
        players[i][1] = hand1
def deal():
    if isinstance(deck, Deck2.Deck):
        dealt, randNum = deck.randCard()
        deck.remCard(randNum)
        return dealt
    else:
        return 'death'

#hmm how to sort the hand
#could do a function where user chooses card and where to move it to
#bit user unfriendly though
#hmm

#i'l sort that out when it comes up
    


pile = [deal()]
#this is the pile next to the deck where you can see the top card
#anything better to call it?
def play():
    global players, pile
    for i in range(1, len(players)):
        print('it is ' +players[i][0]+ ' turn')
        print ("Your hand is", players[i][1])
        print("the card on the top of the pile is " + pile[-1])
        print("would you like a card from the (1) deck, or (2) the pile")
        opt = input()
        if opt == '1':
            dealt = deal()
        elif opt == '2':
            dealt = pile[-1]
            pile.remove(dealt)
        print("you recieved " + dealt + ".")
        players[i][1].append(dealt)
        #right then we've found a difficult bit
        discard(players[i][1])
        #check if won
    


def discard(cards):
    print("which card would you like to discard")
    cardsn = []
    for i in range(len(cards)):
        cardsn.append( '(' + str(i) +')' + cards[i])
    print(cardsn)
    while True:
        try:
            opt = int(input())
            if 0<= opt <=7:
                break
            else:
                print("enter a number between 0 and 7")
        except ValueError:
            print("sorry you didnt enter a number")
        
    pile.append(cards[opt])
    print("you placed " + cards[opt] + " at the top of the pile")
    cards.remove(cards[opt])
    
    
        
#just thinking that i could have used this to create a shuffled deck
#for i in range(52):
#   deck.append(Deck2.Deck(1).cardsList[random.randint(0,len(Deck2.Deck(1).cardsList))])



        
        
numOfPlayers()
initHand()
play()
