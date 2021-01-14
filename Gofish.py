# 2 player simple
### GO - FISH Game Simulation ###  
# Set up Go-fish for two players. Real Player codes player strategy. 
# Game runs significant amount of times. Winner is Declared 
# Order:
# (1) ## (2 player) Each player dealth 7 cards
# (2) ## Flip a coin, see who goes first.
# (3) ## Players look at hands 
##### (A) ## If one player has no cards. Game over. 
##### (B) ## If deck is empty, count matches. Score. Game Over.
##### (C) ## If handset has 4 of a kind,
#           show cards and move them to match pile.
#
# (4) ## Player asks opponent if they have a specific card. 
#      Card must be from asking player's hand set.

##### (A) ## If opponent does not have the card, opponent says "Go fish!"
#           Player draws card from deck to their handset.
##### -- ### (a) ## If card drawn is the same as the asking card, 
#                   Player gets another turn -----> # (4) ##         
##### -- ### (ELSE) Next player's turn -----------> # (4) ##

##### (B) ## Else If opponent has the card, 
#           the opponent hands all of that type over to the Player 
#           Player gets another turn -------------> # (4) ##

################################################################################
import random
from collections import Counter

# Make simple deck since only values matter
CardValues = [ 'Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King']    
Deck = CardValues*4
random.shuffle(Deck)
print("Here's your Deck, Playas", Deck)


# (1) ## (2 player) Each player dealt 7 cards

P1hand = random.choices(Deck, k = 7)
P2hand = random.choices(Deck, k = 7)
both_hands = [P1hand] + [P2hand]
# Check all hands don't allow for more than 4 of the same element
CardCounterZero = {i : 0 for i in CardValues}
def counthands(both_hands):
    for j in range(len(both_hands)):
        return both_hands.count(j)
    print(j)
counthands(both_hands)    

print("These are your cards, Player One: ", P1hand) 
print("These are your cards, Player Two: ", P2hand) 
# Players cannot know opposing player cards.



# print("Here are both hands: ", both_hands)


for eachcard in range(7):
    Deck.remove(P1hand[eachcard])
    Deck.remove(P2hand[eachcard])
print("This is the new deck without the player hands: ", Deck)


# (2) ## Flip a coin, see who goes first.
coin = ['Heads',"Tails"]
flip = random.choice(coin)
print("The coin flips ", flip , ", so ")
if flip == 'Heads':
    print("\t Player One asks first")
else:
    print("\t Player Two asks first")

# Function for Asking and the apporpriate response from Opponent
def AskforCard(Asker_hand,Opp_hand):
    global Deck
    ask = random.choice(Asker_hand)
    print("Do you have any ", ask , "'s?")
    if ask in Opp_hand:
        def count_cards(Opp_hand,ask):
            return Opp_hand.count(ask)
        numOFcards = count_cards(Opp_hand,ask)
        print("Opponent has ", numOFcards, ask , "'s to give you.")

        # def count_cards(Opp_hand,ask):
        #     Opp_hand.count(ask)
        #     if (count_cards(Opp_hand,ask)) > 1:
        #         print("Opponent has {} {}'s to give you".format(count_cards(Opp_hand,ask),ask))
        #         Opp_hand.remove(ask*(count_cards(Opp_hand,ask)))
        #         Asker_hand.append(ask*(count_cards(Opp_hand,ask)))
        #         print("Asker now has, ", Asker_hand)
        #         print("Opponent is left with, ", Opp_hand)
        #     else:
        #         print("Opponent has only one {} to give you, go again.".format(ask))
                
        #         Opp_hand.remove(ask*(count_cards(Opp_hand,ask)))
        #         Asker_hand.append(ask*(count_cards(Opp_hand,ask)))
        #         print("Asker now has, ", Asker_hand)
        #         print("Opponent is left with, ", Opp_hand)
        # count_cards(Opp_hand,ask)




    else: # If ask is not in opponent hands
        print("\t Go fish, bitch")
        # Draw a card
        Asker_hand.append(Deck[0]) 
        Deck.remove(Deck[0])
        print("Asker's hand after turn: ", Asker_hand ) 
        print("New Deck ", Deck)   
        #print('There are ', newdeck , 'cards left in the deck. ')  


AskforCard(P1hand,P2hand)




