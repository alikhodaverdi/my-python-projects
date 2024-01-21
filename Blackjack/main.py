import random
import sys

HEARTS = chr(9829)  # Character 9829 is '♥'.
DIAMONDS = chr(9830)  # Character 9830 is '♦'.
SPADES = chr(9824)  # Character 9824 is '♠'.
CLUBS = chr(9827)  # Character 9827 is '♣'.

BACKSIDE = 'backside'


def main():
    print('''
            
            Rules:
            Try to get as close to 21 without going over. Kings, Queens, and Jacks are worth 10 points. Aces 
            are worth 1 or 11 points.
            Cards 2 through 10 are worth their face value. (H)it to take another card.
            (S)tand to stop taking cards.
            On your first play, you can (D)ouble down to increase your bet but must hit exactly one more time 
            before standing.
            In case of a tie, the bet is returned to the player. The dealer stops hitting at 17.    

            ''')

    money = 5000

    while True:

        if money <= 0:
            print("Your're brke")
            print("Good thing you weren't playing with real money.")
            print('Thanks for playing!')
            sys.exit()

        print('Money:', money)

        bet = getBet(money)
        # Give the dealer and player two cards from the deck each:
        deck = getDeck()

        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]
        # Handle player actions:
        print("Bet :", bet)

        while True:  # Keep looping until player stands or busts.
            diplayHands(playerHand, dealerHand, False)
            print()

            # Check if the player has bust
            if getHandValue(playerHand) > 21:
                break
            # Get the player's move, either H, S, or D:
            move = getMove(playerHand, money - bet)

            # Handle the player actions
            if move == "D":
                # Player is doubling down, they can increase their bet
                additionalBet = getBet(min(bet, (money-bet)))
                bet += additionalBet
                print("Bet increased to {}.".format(bet))
                print("Bet:", bet)

            if move in ('H', 'D'):
                # Hit / doubling down takes another card.
                newCard = deck.pop()
                rank, suit = newCard
                print('You drew a {} of {}.'.format(rank, suit))
                playerHand.append(newCard)

                if getHandValue(playerHand) > 21:
                    # The player has busted
                    continue

            if move in ('S', 'D'):
                # Stand / doubling down stops the players's trun.
                break

        # Handle the dealer's actions:
        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                # The dealer hits:
                print('Dealer hits...')
                dealerHand.append(deck.pop())
                diplayHands(playerHand, dealerHand, False)

                if getHandValue(dealerHand) > 21:
                    break  # The dealer has busted.

                input("Press Enter to continue...")

                print('\n\n')

        # Show the final hands:
        if dealerHand > 21:
            print("Dealer busts ! You win ${}!".format(bet))

        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)
        # Handle whether the player won,lost,or tied:
        if dealerValue > 21:
            print("Dealer busts ! You win ${}".format(bet))
            money += bet
        elif (playerValue > 21) or (playerValue < dealerValue):
            print('You lost!')
            money -= bet
        elif playerValue > dealerValue:
            print('You won ${}!'.format(bet))
            money += bet
        elif playerValue == dealerValue:
            print('It\'s a tie, the bet is returned to you.')
            input('Press Enter to continue...')
            print('\n\n')


def getBet(maxBet):
    """Ask the player how much they want to bet for this round."""
    while True:  # Keep asking until they enter a valid amount.
        print("How much do you bet ?(1-{},or QUIT)".format(maxBet))
        bet = input(' > ').upper().strip()
        if bet == 'QUIT':
            print('Thanks for playing!')
            sys.exit()e

        if not bet.isdecimal():
            continue  # If the player didn't enter a number, ask again.

        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet  # Player entered a valid bet.


def getDeck():
    """Return a list of (rank, suit) tuples for all 52 cards."""
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))  # Add the numbered cards.
        for rank in ('J', 'Q', 'K', 'A'):
            # Add the face and ace cards. random.shuffle(deck)
            deck.append((rank, suit))
        return deck

    pass


def diplayHands(playerHand, dealerHand, showDealerHand):
    """Show the player's and dealer's cards. Hide the dealer's first card if showDealerHand is False."""


def getHandValue():
    pass


def getMove():
    pass
