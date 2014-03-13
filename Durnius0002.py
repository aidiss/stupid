#http://www.mini.pw.edu.pl/~mandziuk/PRACE/ICAISC06.pdf
#add open play - with open cards.for aipurposes
import random

#~ currentbugs: 
        #~ if player takes home Round continues. round_flow, def 
        #~ attack_switch is not working. Attack_switch, def

def shuffled_deck():
        deck = []
        for suit in ['C', 'D', 'H', 'S']:
                for num in range(6, 15):
                        deck.append(  [(num), suit]  )
        random.shuffle(deck)
        print("Deck shuffled.", len(deck),"cards in deck")
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
        ontable = [] #
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
        print("Role switch!")

def round_start():
        global Round
        Round += 1
        print ("\n############################## Round Nr.:", Round)
        print ("Trump deck: %s\n" %trump_deck, "Attacker hand:", hand[attacker], "Defender hand:", hand[defender], "Trump show:",trump_show,"Trump suit:",trump_suit)
       
def att_first(): #to change
        global att_choice
        if len(hand[attacker]) > 0:
                att_choice = hand[attacker].pop(0)
        ontable.append([att_choice])
        return att_choice
        

def att_choice_list(): #lists attack possibilities
        result = []
        onboard_numbers = [c[0] for c in plain(ontable)]
        #~ print("onboard_numbers",onboard_numbers)
        #~ if len(att_possible_cards) > 0:
                #~ att_possible_cards.pop(0)
        #~ c1 = att_choice #### #need to clarify that I look for first item in the item
        for c1 in hand[attacker]:
                if c1[0] in onboard_numbers: 
                        #~ print("Reflect possible")
                        result.append(c1)
      #  print("Pos atts: ", result)
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
      #  print("Pos defs: ", def_choice_list)
        return def_choice_list

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
                #~ print("You have so many possible attack choices: ", len(att_choice_list()), '\n', "You have the following choices: ", att_choice_list())
                att_choice = att_choice_list()[0]
                hand[attacker].remove(att_choice)
                #~ ontable.append(att_choice)
                return True

def round_end():
                for i in range(6 - len(hand[attacker])):
                        if len(trump_deck) > 0:
                                hand[attacker].append(trump_deck.pop())
                for i in range(6 - len(hand[defender])):
                        if len(trump_deck) > 0:
                                hand[defender].append(trump_deck.pop())
                attacker_switch() #switches attacker
                ontable = [] #clears table


def namo():
        global ontable
        hand[defender].extend(plain(ontable))
     #   ontable.remove(hand[defender][-1]
        print("Defender takes cards home: ", ontable)

        
def bita():
        global ontable
        print("All cards in play are moved to deadcards: ", ontable,len(deadcards))
        deadcards.extend(plain(ontable))
        ontable = []

def round_flow():
        move = 0
        round_start() #initializes round
        while True: # Round goes on
                move += 1
                print("--------------------",move ,"----------------------")
                if len(ontable) == 0 and len(hand[attacker]) > 0: #determines if its first move
                        att_first() #initializes attackers first card
                else:
                        att_more() #runs second attack
                        if not att_choice: #Attacker gives up coz no choices available
                                bita()
                                break
                print ("Att chose: ",att_choice)

                if def_is_def_pos(att_choice): #inserts attackers choice and returns possible moves
                        def_choice = def_choice_list[0]
                        print("Def chose: ",def_choice)
                        ontable[-1].append(def_choice) #
                        hand[defender].remove(def_choice)
                        if len(ontable) < 4:
                                ontable_length = len(ontable)
                                for x in ontable:
                                        if x[0] == x[-1]:
                                                attacker_switch()
                else:
                        namo()
                        
        print("A",hand[attacker],"D",hand[defender], print("Ontable",ontable))

        round_end()#inits end of round. Gives cards. (Reports stats of moves) 

def game_flow():
        while hand[defender] and hand[attacker]:
                round_flow()
        else:
                if len(trump_deck) == 0 and len(hand[attacker]) == 0 and len(hand[defender]) == 0:
                        print("game ends draw")
                elif len(trump_deck) == 0 and len(hand[attacker]) > 0 and len(hand[defender]) == 0:
                        print("game ends: Defender wins", len(deadcards))
                elif len(trump_deck) == 0 and len(hand[attacker]) == 0 and len(hand[defender]) > 0:
                        print("game ends: Attacker wins")
        


game_flow()
