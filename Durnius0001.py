#http://www.mini.pw.edu.pl/~mandziuk/PRACE/ICAISC06.pdf
#add open play - with open cards.for aipurposes
import random

def shuffled_deck():
        deck = []
        for suit in ['C', 'D', 'H', 'S']:
                for num in range(6, 15):
                        deck.append(  [(num), suit]  )
        random.shuffle(deck)
        return deck
def card_name(card):
    if card == 11:
        return 'J'
    elif card == 12:
        return 'Q'
    elif card == 13:
        return 'K'
    elif card == 14:
        return 'A'
    else:
        return str(card)
def deal_cards():
    return deck[:12:2], deck[1:13:2], deck[13:-1], deck[-1]
def init():
        print("The game 'Stupid' is now starting...", )
        global deck,hand,trump_suit,trump_deck,trump_show,ontable,deadcards,Round, attacker, defender
        deck = shuffled_deck()
        hand = {}
        hand["P1"], hand["P2"], trump_deck, trump_show = deal_cards()
        trump_suit = trump_show[1]
        ontable = []
        deadcards = [] #panaudotu kortu kruva
        attacker = "P1"
        defender = "P2"
        Round = 0
init()

def attacker_switch():
        global attacker,defender
        if attacker == "P1":
                attacker = "P2"
                defender = "P1"
        else:
                attacker = "P1"
                defender = "P2"

### in game mechanics

def round_start():
        global Round
        Round += 1
        print ("\n############################## Round Nr.:", Round)
        print ("Trump deck: %s\n" %trump_deck, "Attacker hand:", hand[attacker], "Defender hand:", hand[defender])
        print ("Trump show:",trump_show)
        print ("Trump suit:",trump_suit)
       
def att_first(): #to change
        global att_choice
        att_choice = hand[attacker].pop(0)
        ontable.append([att_choice])
        return att_choice

def att_choice_list(): #lists attack possibilities
        result = []
        
        onboard_numbers = [c[0] for c in plain(ontable)]
        print("onboard_numbers",onboard_numbers)
        #~ if len(att_possible_cards) > 0:
                #~ att_possible_cards.pop(0)
        #~ c1 = att_choice #### #need to clarify that I look for first item in the item
        for c1 in hand[attacker]:
                if c1[0] in onboard_numbers: 
                        print("Reflect possible")
                        result.append(c1)
        return result



def def_is_def_pos(c1):
        global def_choice, def_choice_list
        def_choice_list = []
        def_choice = []
        c1 = att_choice #### #need to clarify that I look for first item in the item
        for c2 in hand[defender]:
                #~ print ("These two cards will be compared: ",c1, c2)
                if c1[1] == c2[1]: #Suit actions
                        #~ print("Suit actions")
                        if c1[0] < c2[0]: #Possible if higher card, suit actions.
                               #~ print("Higher same suit")
                               def_choice_list.append(c2)
                if c1[1] != trump_suit and c2[1]==trump_suit: #Trump actions
                        #~ print("Trump card available") 
                        def_choice_list.append(c2),
                if c1[0] == c2[0]: #Reflect action
                        #~ print("Reflect possible")
                        def_choice_list.append(c2)
                #~ else:
                        #~ print("No possible moves")
        print("You have so many possible defence choices: ", len(def_choice_list), "You have the following choices: ", def_choice_list)
        return def_choice_list
#~ 
#~ if def_is_def_pos == True:
        #~ if def_number_of_choices < 2:
                #~ choice[0]
        #~ else def_choice

def plain(paired_cards):
        global boom
        boom = []
        for x in paired_cards:
                boom.append(x[0])
                if len(x) > 1:
                        boom.append(x[1])
        return boom
                        


        
def att_more():
        global att_possible_cards, att_choice
        att_choice = []
        if      att_choice_list():
                print("You have so many possible attack choices: ", len(att_choice_list()), '\n', "You have the following choices: ", att_choice_list())
                att_choice = att_choice_list()[0]
                hand[attacker].remove(att_choice)
                return True

def att_choose_card():
        passc1
def att_bita():
        attacker_switch()
        round_end()
        
def att_stop():
        if len.att_choice_list < 2:
                att_bita()
        pass
        
def def_ence():
        for x in hand[defender]:
                #compare each_item_in_hand_defender to last items first line.
                #if valid put to a list possible_cards
                #choose a card from possible cards
                if x == def_choice_list: #compare items
                        def_choice = hand[defender].pop(0)
                        print("def_choice",def_choice)
                        ontable[-1].append(def_choice)
                        return def_choice


def def_give_up():
        pass
def def_refl():
        pass
def def_after_refl():
        nm_of_cards_to_defend = 0
        nm_of_cards_to_defend = count(onboard)
        cards_to_defend = []
        for x in onboard:
                if x[2] == "":
                        cards_to_defend(x.pop)
                        nm_of_cards_to_defend += 1
        print("Cards to defend: ", cards_to_defend)
        pass

def round_end():
                for i in range(6 - len(hand[attacker])):
                        if len(trump_deck) > 0:
                                hand[attacker].append(trump_deck.pop())
                for i in range(6 - len(hand[defender])):
                        if len(trump_deck) > 0:
                                hand[defender].append(trump_deck.pop())


#~ how_attack = att_choice_list[0]
#~ print("Attack1",how_attack)
def namo():
        global ontable
        print("namo", ontable)
        hand[defender].extend(plain(ontable))
        ontable = []
        
def bita():
        global ontable
        print("bita", ontable)
        deadcards.extend(plain(ontable))
        ontable = []

def round_flow():
        move = 0
        round_start() #initializes round
        while True: # Round goes on
                move += 1
                print("---",move ,"---")
                if len(ontable) == 0:
                        att_first() #initializes attackers first card
                else:
                        att_more()
                        if not att_choice:
                                bita()
                                break
                print ("Attacker chose: ",att_choice, "\n")
                if def_is_def_pos(att_choice): #inserts attackers choice and returns possible moves
                        def_choice = def_choice_list[0]
                        print("def_choice",def_choice)
                        hand[defender].remove(def_choice)
                        ontable[-1].append(def_choice)
                else:
                        namo()
                        print("Defending player takes cards: ", ontable)
        round_end()#inits end of round. Gives cards. (Reports stats of moves) 
        

def game_flow():
        while hand[defender] and hand[attacker]:
                round_flow()
                attacker_switch()

game_flow()


#~ def attack(defender, attackers):
        #~ if attack_defence1 is empty:
        #~ attack_defence1.append(choice)
        #~ elif
        #~ attack_defence2 is empty:
        #~ attack_defence2.append(choice)
        #~ elif
        #~ attack_defence3 is empty:
        #~ attack_defence3.append(choice)
        #~ elif
        #~ attack_defence4 is empty:
        #~ attack_defence4.append(choice)
        #~ elif
        #~ attack_defence5 is empty:
        #~ attack_defence5.append(choice)
        #~ elif
        #~ attack_defence6 is empty:
        #~ attack_defence6.append(choice)

#~ def defence(defenders_choice):
	#~ with_to_defend = ""
	#~ if defenders_choice #same power as attacking card
		#~ move_defender_status
	#~ elif defenders_choice #right to one attack#
		#~ attack_defence.append
	#~ elif defenders_choice #right to many attacks#
		#~ which_to_defend = raw_input (#listattacks to defend#)
	#~ else 
		#~ defenders_choice #cannot fend of any attacks

#    print ("Round %d" % round")
#    who_attacks = #1 or 2. Kuris zaidejas puola
#    whos_turn = #1 or 2. Kuriam zaidejui reikia mesti korta
#    raw_input. Player sees all his cards and puts a card. Also, being able to put two cards.
#    raw_input. Player2 sees the cards on table and his cards. Choose to reply.
#	ontable.extend ([card1,card2])
	# players_choice
#	print "Player One plays the %s of %s." % (card_name(card1[0]), card1[1]) #to run few times
   	# players_choice
#   	print "Player Two plays the %s of %s." % (card_name(card2[0]), card2[1])
	#if one drops last card and the one that loses ..
	#if player is underattack and does not defend #add on_table to defender_stack
	#switching stacks. If player replies with #samecard[0] attacker turns into deffender, deffenders move.
    
#def print_both_hands:
#	print hand1
#	print hand2

#def print_all:
#	print deck
#	print coser_stack
#	print hand1
#	print hand2
#	print dead_cards



#~ def start_game()

#~ while Round < 2:
    #~ Round += 1
    #~ attacker_switch()
    #~ move = 0    
    #~ while True:
            #~ hand[attacker]
            #~ print("Attacker: %s\n " %attacker, hand[attacker], "\n")
            #~ att_choice = hand[attacker].pop(0)
            #~ print(att_choice)
            #~ attacker_choice = att_choice
            #~ choice = input("What card would you like to attack with? (Use acronims like AS or JD)")  # print hand1 alternatively print hand
            #~ if attacker_cRound += 1hoice in hand[attacker]: #if choice in attackers_hand ORMORESIMPLE if choice == "KS":
                #~ ontable.append(attacker_choice)
                #~ print("Attacking player chose: %s \n"%attacker_choice)
                #~ print("Ontable: %s \n"%ontable)
            #~ else:
                #~ print ("The card you chose is not in your hand" )
                #~ print ("round",Round)
            #~ move +=1
            #~ print("Move nr:",move,"\n")
#sukurti
#attackers_move(attacker):
