import random 
from collections import Counter

# Build Deck
CardValues = ['Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King'] # List of Card Values for deck
Deck = CardValues*4 # 4 suits for each card in a deck.
random.shuffle(Deck) # By making deck a list, we can use the shuffle module 
print("Here's your Deck, Playas: ", Deck)
print('Here is your Deck counter: ')
print(Counter(Deck))

# Draw cards to players
Playerhands = random.choices(Deck, k = 14) # Make one list to count player cards.
print("Here is the Drawn cards counter: ")
print(Counter(Playerhands)) # count each card. 
# ------------------Make a limit for 4 cards
lengthPH = len(Playerhands) # We are going to split the list into each player's respective hand
middle_index = lengthPH//2 # Our midpoint for the split

# Player Hands
P1Hand = Playerhands[:middle_index] 
P2Hand = Playerhands[middle_index:]
print("Player One Hand: ")
print("\t", P1Hand)
print("Player Two Hand: ")
print("\t", P2Hand)

# Remove hand values from deck. Draw from deck
for eachcard in range(7):
    Deck.remove(P1Hand[eachcard])
    Deck.remove(P2Hand[eachcard])
print("This is the new deck without the player hands: ", Deck)


# (2) ## Flip a coin, see who goes first.
coin = ['Heads',"Tails"]
flip = random.choice(coin)
print("The coin flips ", flip , ", so ")
if flip == 'Heads':
    print("\t Player One asks first")
else:
    print("\t Player Two asks first")

#### TSKS TO DO #####
# --- Look at Cards
# --- --- If playr hand has 4 of a kind: Set into match pile. 1 Match point
# --- --- If Player hand is empty: Winner 
# --- --- Else: Next step
# --- Player asks opponent for card 
# --- Opponent responds accordingly 
# --- --- If Opp has card(s): give them over
# --- --- If Opp does not have card: Say "Go Fish Bitch"
# --- Next player turn
