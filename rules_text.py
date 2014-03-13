###Durak (Russian for Stupid). This rules rendition by Alejandro Tkaczevski.

#Object. Not to lose. There is no single winner, but there is a single loser.
##AI.IL.

#The last player with cards in hand is the loser. The game involves some luck but mostly strategy. Like in chess, each player may develop his or her own style of playing.
Losing_rule =

#Players. Three to five or six players, usually four.
Number of players =
#Preparing the Deck. There are several variations of this game depending on how many players, and the general level of expertise. For large groups (5 or 6 players) and/or beginners usually the whole deck is used. For a smaller group and/or a faster game a smaller deck is used.
##IL. Deck dependence on number of players.

##Large Deck Use one deck of 52 cards. Remove the Jokers.
def deck_size(large_deck or small_deck)
def Large_deck = #Card values in ascending order: 2 3 4 5 6 7 8 9 10 J Q K A trump.

##Small Deck (preferable). Use one deck of 52 cards. Remove the Jokers, as well as all the cards of a face value of five or less (except the Aces).
def Small_deck = #Card values in ascending order: 6 7 8 9 10 J Q K A trump.

#Preparation. Except for the first game of the evening, the loser of the previous game is the dealer. #NI(Not important). whos dealer. Impacts only whos given first card. 
#    Shuffle the cards. #DONE
#    The dealer asks the person to his left to cut the deck. Optional: If this is not the first game of the evening, the player may opt not to cut the deck by saying "Nye snimayu shapkee Doo-rah-kam" ("I do not tip my hat to idiots"). The dealer must go around the table asking for people to cut the deck. If all refuse, the dealer cuts the deck.
#    If the small deck is used, deal six cards to each player. If the large deck is used deal seven (usually) or six (rarely) cards to each player depending on general agreement.
#    After the players have received all their cards, reveal the top card of the deck. Place it on the middle of the table, place the deck on top of the revealed card, covering it half way. This card represents the trump suit and is now at the bottom of the deck. Cards in this suit hold a higher value then the Aces of the other suits. Within the trump suit card hierarchy is maintained. Optional: Before game play begins the player who holds a two (large deck) or six (small deck) of the trump suit in their hand may opt to exchange their card for the revealed trump card. This may only be done before the game begins.

#Game Play
#    The game consists of a series of attacks (where players get a chance to get rid of cards) and defenses (where players are threatened with having to add cards to their hand unless of course they are succesful in defending themselves).
#    Each player gets a turn to defend himself. As players are eliminated from the game, the order of defenders must be maintained (see notes below).
#    The first attacker is the player on the left of the dealer (dealer attacks last). The defender is the player to the left of the attacker. Game play procedes clockwise.

#    There are three common variations in Durak:
#        Pros-toy (simple)
#       Pod-kid-noy (underhand)
#        Pe-re-vod-noy (pass the buck). 
#    Podkidnoy is the most popular. This variation will be described in the main body of the rules. The rules for the other two variations will descibed in the Variations section.

def Attacking_phase ###can it be describe as phase?

#    Attacker reveals a card from his hand by placing it on the table so all can see. Hint A*.
def atackers_choice =

#    After the first card has been defended all players become attackers and may add cards to the table as long as they are of the same face value as other cards in play. Hint B*. 
def defenders_choice = 
	first_move #if yes = any card can be played. If no = only same number or coser (on non_trump), or higher trump (on trump)
	second_attackers_move_what_are_the_possible_cards =

#    Maximum cards to be defended must be as many as have been originally dealt to each player (6 or 7) or until the defender runs out of cards, whichever is less. max_cards_to_be_defended = #number of dealt cards or the number of cards that defender has

#Defending ###can it be describe as phase?
#    Defender must respond to the revealed card by beating it with a card of the same suit of higher value or a card of the trump suit. Hint C*. Hint D*. ###defenders_choices
#    If the defender has no appropriate card he must pick up the card and add it to his hand, thereby losing his turn to attack. If the defender picks up the first attacking card, the turn is over. ###no_choices ###losing_attacking_turn
#    If the defender beats the first card, all other players may join in as attackers. #IL. More players
#    Defender must beat all revealed cards. Otherwise he must pick all cards in play including ones that have been beaten. Hint E*. 
#    Maximum cards to be defended must be as many as have been originally dealt to each player (6 or 7) or until the defender runs out of cards, whichever is less.
#    A successful turn ends when the defender beats all attacking cards. All cards that have been revealed during this turn are removed from the game. #no_more_attack_attackers_choice

End_of_Turn = 0 or 1 #should be switched by defender or attacked. 
	Attacker_chooses_not_to_attack
		move_cards_to_dead #how to move cards from table to removed_cards_stack
	defender_chooses_not_to_defend
		takes on_table #how to transfer from stack to hand
#    When a defender has successfully beaten all the attacking cards, all the cards that have been in play are removed from the game. #

    ###Every player must take his turn to refresh his hand by taking as many cards from deck as needed to bring his hand to a total of as many as have been originally dealt to each player (6 or 7). The original attacker refreshes his hand first. All other attackers follow in clockwise order. Defender refreshes his hand last. Hint F*.
def refreshing_cards
	check_number_of_cards_in_hand:
		if attacker_hand_size < initial_hand_size
			fill(attacker)
				add_cards till attackers_hand_size = initial_hand_size
			fill(defender)
				add_cards till defenders_hand_size = initial_hand_size
		if deck_size = 0 # If the deck has been exhausted, players who are left empty handed withdraw from the game. They are lucky, for they will not have a chance to lose.

			continue to play

turn_switch   #The player who completed a successful defence becomes the next attacker against the player to his left. If the defender was not successful, the player to his left becomes the attacker. Hint G*.

#Endgame. The endgame begins as soon as the deck is exhausted and there are no more cards to refresh one's hand. As cards and players are eliminated, strategy becomes much more important than luck. The last two players battle out their fates, until one player remains with cards in hand. This player is the Durak and the dealer of the next game. (There have been games where there was no loser when two players remain each holding one card. The attacker reveals his card. The defender happens to be able to beat it. The game is over without a loser. But this happens very rarely.)
draw #last two players attack and defend succesfully. How to define?


#Variations
#Prostoy (simple)
#The rules are the same as above, except that each turn consists of one attacker, and one defender. Other players do not get a chance to attack once the first card has been beaten. They only watch until it is their turn to be attacker or defender. This variation is usually played only for didactic reasons.

#Prevodnoy (pass the buck)
#The rules are the same as Prostoy with one addition. If a defender finds that he has a card of the same value as the attacker has placed on the table, he places that card down and passes off both cards to the player on his left to defend. This variation is rarely played.

#Podkidnoy-Perevodnoy (underhand and pass the buck)
#This variation is popular with children and is much sillier than plain Podkidnoy. The rules are the same as Podkidnoy (described in the main body of the rules) with the same addition as in (c.). If a defender (Misha) finds that he has a card of the same value as the attacker (Tanya) has placed on the table, he places that card down and passes off both cards to the player on his left (Boris) to defend. Each new defender (Boris) must attempt to beat all cards on the table. However new attacking cards may be placed on the table only after all the passed cards have been beaten. The possibility exists that the third player may pass the buck as well... and even the fourth player...

#Notes Regarding Order of Defenders
#Perhaps the most difficult aspect of the game to get used to is that turns are based on order of defenders. This becomes important in the end game when players are eliminated.

#Players are eliminated in two ways:

    #An attacker used his last card,
    #A defender has successfully beaten all cards on the table and is left empty handed. 

#In the first case, game play procedes in an obvious manner. In the second case, game play is not necessarily as obvious.

#When the defender is left empty handed (Misha), successfully completing his turn, it would normally be his turn to attack. However the deck has been exhausted. The player on his left (Boris) does not get a free ride, however. The player to the new defender(Boris)'s right who is still in play is the attacker (Tanya). This often means that a player (Tanya) gets to attack twice in a row: first against the player who has just been eliminated (Misha), and second against the new defender (Boris).

#Hints
#A
#Preferably this is an unwanted card, usually one of low value, but not necessarily.

#B
#You may want to collect cards of the same value to increase the punch of an attack.

#C
#Defender may want to keep trump cards to the end of the game, but not necessarily.

#D
#By defending with a trump of the same face value, the defender minimizes the risk of further attacks.

#E
#Picking up the first card can sometimes be a wise move.

#F
#If a player has enough cards there is no need to refresh the hand.

#G
#As a player your goal is to keep the person to your immediate right from defending successfully, and to help the person two spaces for your right from losing a turn.

#Rules rendition by Alejandro Tkaczevski of ?, USA
#tka@crl.com
#August 3, 1993

#The Game Cabinet - editor@gamecabinet.com - Ken Tidwell
