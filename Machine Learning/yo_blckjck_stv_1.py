#Blackjack Card game 
import random 
import time
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11} 

class Card():

	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank 
	#This may not be needed as it is a string function	
	def __str__(self):
		return self.rank + ' of ' + self.suit

class Deck():

	def __init__(self):
		self.deck = []
		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit,rank))
	#This may not be needed as it is a string function
	def __str__(self):
		deck_comp = ''
		for card in self.deck:
			deck_comp += '\n' +card.__str__()
		return "The deck has: "+deck_comp

	def shuffle(self):
		random.shuffle(self.deck)

	def deal(self):
		return self.deck.pop()

class Hand():

	def __init__(self):
		self.cards = []
		self.value = 0
		self.aces = 0

	def add_card(self, card):
		self.cards.append(card)
		self.value += values[card.rank]
		if card.rank == 'Ace':
			self.aces += 1

	def adjust_for_ace(self):
		while self.value > 21 and self.aces:
			self.value -= 10
			self.value -= 1

class Chips():

	def __init__(self, total = 100):
		self.total = total
		self.bet = 0

	def win_bet(self):
		self.total += self.bet

	def lose_bet(self):
		self.total -= self.bet

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def yobot_busts(yobot, dealer, chips):
    chips.lose_bet()

def yobot_wins(yobot, dealer, chips):
    chips.win_bet()

def dealer_busts(yobot, dealer, chips):
    chips.win_bet()
   
def dealer_wins(yobot, dealer, chips):
    chips.lose_bet()

def take_bet(chips): 
	chips.bet = random.randint(1, chips.total) 	

def play_game():
	bank = 1000
	wins = 0
	losses = 0
	number_of_games = 1
	winning_streak = 0
	current_emotion = ' '
	
	def emotion(wins, losses, number_of_games, winning_streak, bank):
		current_emotion = ' '
		emotional_coefficient = .50 (wins / number_of_games) + .50 (winning_streak / 10)
		if emotional_coefficient <= .20:
			current_emotion = 'depressed!'
		elif emotional_coefficient > .20 and emotional_coefficient <= .50:
			current_emotion = 'sad'
		elif emotional_coefficient > .50 and emotional_coefficient <= .70:
			current_emotion = 'upset'
		elif emotional_coefficient > .70 and emotional_coefficient <= .90:
			current_emotion = 'content'
		else:
			current_emotion = 'happy!'

		print(f'Wins: {wins} \n Losses: {losses} \n Number of Games: {number_of_games} \n Winning Streak: {winning_streak} \n Bank Account: {bank} I am feeling {current_emotion}')
	
	while True:
		number_of_games += 1
		deck = Deck()
		deck.shuffle()

		yobot_hand = Hand()
		yobot_hand.add_card(deck.deal())
		yobot_hand.add_card(deck.deal())

		dealer_hand = Hand()
		dealer_hand.add_card(deck.deal())
		dealer_hand.add_card(deck.deal())

		yobot_chips = Chips()
		take_bet(yobot_chips)
		# This will withdraw 100 chips from the bank and add it to chips total count.
		if yobot_chips == 0:
			bank -= 100
			yobot_chips += 100
			take_bet(yobot_chips)

		#Always hit hard 11 or less.
		while yobot_hand.value < 21:
			if yobot_hand.value <= 11 and yobot_hand.aces == 0: 
				return hit(deck,yobot_hand)
		#Stand on hard 12 against a dealer 4-6, otherwise hit.
			elif yobot_hand.value == 12 and yobot_hand.aces == 0 and dealer_hand.value in range(4, 7): 
				break 
			elif yobot_hand.value == 12 and yobot_hand.aces == 0:
				return hit(deck,yobot_hand)
		#Stand on hard 13-16 against a dealer 2-6, otherwise hit.
			elif yobot_hand.value in range(13, 17) and dealer_hand.value in range(2, 7):
				break
			elif yobot_hand.value in range(13,17) and yobot_hand.aces == 0:
				return hit(deck, yobot_hand)
		#Always stand on hard 17 or more.
			elif yobot_hand.value >= 17 and yobot_hand.aces == 0:
				break
		#Always hit soft 17 or less.	
			elif yobot_hand.value <= 17 and yobot_hand.aces:
				return hit(deck, yobot_hand)
		#Stand on soft 18 except hit against a dealer 9, 10, or A
			elif (dealer_hand.value in range(9,11) or dealer_hand.aces) and (yobot_hand.value == 18 and yobot_hand.aces):
				return hit(deck, yobot_hand)
			elif yobot_hand.value == 18 and yobot_hand.aces and dealer_hand.value not in range(9, 11) or dealer_hand.aces:
				break
		#Always stand on soft 19 or more.
			elif yobot_hand.value >= 19 and yobot_hand.aces:
				break #I want this to stop Yobot's decisions 
			else:	
				continue 
			
		if yobot_hand.value > 21:
			yobot_busts(yobot_hand, dealer_hand, yobot_chips)
			losses -= 1
            winning_streak = 0
		if yobot_hand.value <= 21: 
			
			while dealer_hand.value < 17:
				hit(deck, dealer_hand)

			if dealer_hand.value > 21:
				dealer_busts(yobot_hand, dealer_hand, yobot_chips)
				wins += 1
				winning_streak += 1
			elif dealer_hand.value > yobot_hand.value:
				dealer_wins(yobot_hand, dealer_hand, yobot_chips)
				losses -= 1
                winning_streak = 0
			elif dealer_hand.value < yobot_hand.value:
				yobot_wins(yobot_hand, dealer_hand, yobot_chips)
				wins += 1
                winning_streak += 1
			else: 
 				continue

		print(f"Wins: {wins} \n Losses: {losses} \n Number of Games: {number_of_games} \n Winning Streak: {winning_streak} \n Bank Account: {bank} I am feeling {current_emotion}")
		time.sleep(1)