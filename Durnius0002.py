"""
#http://www.mini.pw.edu.pl/~mandziuk/PRACE/ICAISC06.pdf
#add open play - with open cards.for aipurposes

#~ currentbugs: 
    #~ if player takes home Round continues. round_flow, def 
    #~ attack_switch is not working. Attack_switch, def
"""
import random

def shuffled_deck():
    """Initiation"""
    deck = []
    for suit in ['C', 'D', 'H', 'S']:
        for num in range(6, 15):
            deck.append([(num), suit])
    random.shuffle(deck)
    print("Deck shuffled.", len(deck), "cards in deck")
    return deck


def card_name(card):
    """Initiation"""
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
        
def deal_cards(deck):
    """Initiation"""
    return deck[:12:2], deck[1:13:2], deck[13:-1], deck[-1]


def attacker_switch(attacker, defender):
    """Performs a role switch.

    Todo: incorporate to rule set.
    """
    if attacker == "P1":
        attacker, defender = "P2", "P1"
    else:
        attacker, defender = "P1", "P2"
    return attacker, defender
    print("Role switch!")


def round_start(Round):
    Round += 1
    print("Round Nr.:", Round)
    print("Trump deck: %s\n" % trump_deck, 
        "Attacker hand:", hands[attacker], 
        "Defender hand:", hands[defender], 
        "Trump show:", trump_show,
        "Trump suit:", trump_suit,
    )
    return Round

  
def att_first(hands, attacker, ontable):
    """Attackers first move.

    Attacker sees his cards and has memory.
    """
    if len(hands[attacker]) > 0:
        att_choice = hands[attacker].pop(0)
    ontable.append([att_choice])
    return att_choice, ontable
        

def att_choice_list(): 
    """List possibilities of an attacker."""
    result = []
    onboard_numbers = [c[0] for c in plain(ontable)]
    #~ print("onboard_numbers",onboard_numbers)
    #~ if len(att_possible_cards) > 0:
            #~ att_possible_cards.pop(0)
    #~ c1 = att_choice #### #need to clarify that I look for first item in the item
    for c1 in hands[attacker]:
        if c1[0] in onboard_numbers: 
            #~ print("Reflect possible")
            result.append(c1)
    # print("Pos atts: ", result)
    return result


def def_is_def_pos(att_choice):
    """Looking for possible defence moves.

    Defence moves are chosen based on:
      - attacking card or cards
      - trump card
      - defenders card
    """
    def_choice_list = []
    c1 = att_choice  #  Need to clarify that I look for first item in the item
    for c2 in hands[defender]:
        #  print ("These two cards will be compared: ",c1, c2)
        if c1[1] == c2[1]:  # Suit actions
            #  print("Suit actions")
            if c1[0] < c2[0]:  # Possible if higher card, suit actions.
                # print("Higher same suit")
                def_choice_list.append(c2)
        elif c1[1] != trump_suit and c2[1] == trump_suit:  # Trump actions
            # print("Trump card available") 
            def_choice_list.append(c2)
        elif c1[0] == c2[0]: #Reflect action
            # print("Reflect possible")
            def_choice_list.append(c2)
    # print("Pos defs: ", def_choice_list)
    return def_choice_list


def plain(paired_cards):
    """Plain is a pair of cards."""
    global boom
    boom = []
    for x in paired_cards:
        boom.append(x[0])
        if len(x) > 1:
            boom.append(x[1])
    return boom


def att_more(ontable):
    """Second attack move.

    Todo: make iterator for attack moves.
    """
    att_choice = []
    if att_choice_list():
        # print("You have so many possible attack choices: ", len(att_choice_list()), '\n', "You have the following choices: ", att_choice_list())
        att_choice = att_choice_list()[0]
        hands[attacker].remove(att_choice)
        # ontable.append(att_choice)
        return att_choice


def round_end(ontable, attacker, defender, hands):
    """Signals end of round. 
    Round end is called when:
       - defender defended all attacks.
       - defender cannot defend

       Bita or namo should be outcom of the round.
       Game could end after round also.
    """
    for i in range(6 - len(hands[attacker])):
        if len(trump_deck) > 0:
            hands[attacker].append(trump_deck.pop())
    for i in range(6 - len(hands[defender])):
        if len(trump_deck) > 0:
            hands[defender].append(trump_deck.pop())
    attacker, defender = attacker_switch(attacker, defender)  # switches attacker
    ontable = []  # clears table
    return ontable, attacker, defender, hands


def namo(ontable, hands, defender):
    """Vienas zaidejas pasiima ant stalo esancias kortas i ranka"""
    hands[defender].extend(plain(ontable))
    # ontable.remove(hand[defender][-1]
    print("Defender takes cards home: ", ontable)

        
def bita(ontable, deadcards):
    """Kvieciama kai zaidejas atsigina, polantys neturi daugiau kortu"""
    print("All cards in play are moved to deadcards: ", ontable, len(deadcards))
    deadcards.extend(plain(ontable))
    ontable = []
    return ontable, deadcards


def round_flow(attacker, defender, ontable, hands, deadcards):
    """This is one round"""
    move = 0
    Round = round_start(Round=move)  # initializes round
    while True:  # Round goes on
        move += 1
        print("Move: %s" % move)
        if len(ontable) == 0 and len(hands[attacker]) > 0:  # determines if its first move
            att_choice, ontable = att_first(hands, attacker, ontable)  # initializes attackers first card
        else:
            att_choice = att_more(ontable)  # runs second attack
            if not att_choice:  # Attacker gives up coz no choices available
                ontable, deadcards = bita(ontable, deadcards)
                break
        print("Att chose: ", att_choice)

        possible_moves = def_is_def_pos(att_choice)  # inserts attackers choice and returns possible moves
        if possible_moves:  
            def_choice = possible_moves[0]
            print("Def chose: ", def_choice)
            ontable[-1].append(def_choice)
            hands[defender].remove(def_choice)
            if len(ontable) < 4:
                ontable_length = len(ontable)
                for x in ontable:
                    if x[0] == x[-1]:
                        attacker_switch(attacker, defender)
        else:
            namo(ontable, hands, defender)
                    
    print(
        "A", hands[attacker], 
        "D", hands[defender], 
        "Ontable", ontable,
    )

    ontable, attacker, defender, hands = round_end(ontable, attacker, defender, hands) #inits end of round. Gives cards. (Reports stats of moves) 


def game_flow(hands, defender, attacker, trump_deck, deadcards):
    """Whole game.

    Game consits of players 2-4.
    Game consists of cards.
    Game consists of rounds.

    Game ends when only only one or zero players have 0 cards and there are 0 cards to take from the floor
    """
    while hands[defender] and hands[attacker]:
        round_flow(attacker, defender, ontable, hands, deadcards)
    else:
        if len(trump_deck) == 0 and len(hands[attacker]) == 0 and len(hands[defender]) == 0:
            print("game ends draw")
        elif len(trump_deck) == 0 and len(hands[attacker]) > 0 and len(hands[defender]) == 0:
            print("game ends: Defender wins", len(deadcards))
        elif len(trump_deck) == 0 and len(hands[attacker]) == 0 and len(hands[defender]) > 0:
            print("game ends: Attacker wins")

if __name__ == "__main__":
    print("The game 'Stupid' is now starting...", )
    deck = shuffled_deck()
    hands = {}
    hands["P1"], hands["P2"], trump_deck, trump_show = deal_cards(deck)
    trump_suit = trump_show[1]
    ontable = []  # Cards that are on table
    deadcards = []  # Dead cards are ...
    attacker = "P1" 
    defender = "P2"
    Round = 0

game_flow(hands, defender, attacker, trump_deck, deadcards)
