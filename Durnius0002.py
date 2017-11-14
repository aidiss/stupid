"""
#http://www.mini.pw.edu.pl/~mandziuk/PRACE/ICAISC06.pdf
#add open play - with open cards.for aipurposes

#~ currentbugs: 
    #~ if player takes home Round continues. round_flow, def 
    #~ attack_switch is not working. Attack_switch, def
"""
import random
import logging
logging.basicConfig(level='DEBUG')
logger = logging.getLogger(__name__)


def shuffled_deck():
    """Initiation"""
    deck = []
    for suit in ['C', 'D', 'H', 'S']:
        for num in range(6, 15):
            deck.append([(num), suit])
    #random.shuffle(deck)
    logger.info("Deck shuffled %s cards in deck", len(deck))
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


def round_start(Round):

    return Round

  
def att_first(hands, attacker, ontable):
    """Attackers first move.

    Attacker sees his cards and has memory.
    """
    if len(hands[attacker]) > 0:
        att_choice = hands[attacker].pop(0)
    ontable.append([att_choice])
    logger.debug('Attacker chose %s', att_choice)
    return att_choice, ontable
        

def att_choice_list(): 
    """List possibilities of an attacker."""
    result = []
    onboard_numbers = [c[0] for c in plain(ontable)]
    #~ logger.info("onboard_numbers",onboard_numbers)
    #~ if len(att_possible_cards) > 0:
            #~ att_possible_cards.pop(0)
    #~ c1 = att_choice #### #need to clarify that I look for first item in the item
    for c1 in hands[attacker]:
        if c1[0] in onboard_numbers: 
            #~ logger.info("Reflect possible")
            result.append(c1)
    # logger.info("Pos atts: ", result)
    return result


def get_possible_defense_move(att_choice, hands):
    """Looking for possible defence moves.

    Defence moves are chosen based on:
      - attacking card or cards
      - trump card
      - defenders card
    """
    def_choice_list = []
    c1 = att_choice  
    for c2 in hands[defender]:
        logger.debug("These two cards will be compared:  %s and %s",c1, c2)
        if c1[1] == c2[1]:  # Suit actions
            #  logger.info("Suit actions")
            if c1[0] < c2[0]:  # Possible if higher card, suit actions.
                # logger.info("Higher same suit")
                def_choice_list.append(c2)
        elif c1[1] != trump_suit and c2[1] == trump_suit:  # Trump actions
            # logger.info("Trump card available") 
            def_choice_list.append(c2)
        elif c1[0] == c2[0]: #Reflect action
            # logger.info("Reflect possible")
            def_choice_list.append(c2)
    # logger.info("Pos defs: %s", def_choice_list)
    return def_choice_list, hands


def plain(paired_cards):
    """Plain is a pair of cards."""
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
    att_choices = att_choice_list()
    if att_choices:
        # logger.info("You have so many possible attack choices: ", len(att_choice_list()), '\n', "You have the following choices: ", att_choice_list())
        att_choice = att_choices[0]
        logger.debug('Attacker chose %s', att_choice )
        hands[attacker].remove(att_choice)
        ontable.append([att_choice, ])
        logger.debug('On table %s', ontable)
        return att_choice


def round_end(ontable, attacker, defender, hands):
    """Signals end of round.

    Round end is called when:
       - defender defended all attacks.
       - defender cannot defend

       Bita or namo should be outcom of the round.
       Game could end after round also.

       #inits end of round. Gives cards. (Reports stats of moves) 

    """
    for i in range(6 - len(hands[attacker])):
        if len(trump_deck) > 0:
            hands[attacker].append(trump_deck.pop())
            logging.debug('adding card')
    for i in range(6 - len(hands[defender])):
        if len(trump_deck) > 0:
            hands[defender].append(trump_deck.pop())
            logging.debug('adding card')
    attacker, defender = defender, attacker  # switches attacker
    ontable = []  # clears table
    return ontable, attacker, defender, hands


def namo(ontable, hands, defender):
    """Vienas zaidejas pasiima ant stalo esancias kortas i ranka"""
    assert hands[defender]
    hands[defender].extend(plain(ontable))
    logger.debug('On table: %s', ontable)
    ontable.remove(hands[defender][-1]) #?
    logger.info("Defender takes cards home: %s ", ontable)
    return ontable, hands

        
def bita(ontable, deadcards):
    """Kvieciama kai zaidejas atsigina, polantys neturi daugiau kortu"""
    logger.info("All cards in play are moved to deadcards: %s ", ontable)
    deadcards.extend(plain(ontable))
    logger.info("Len of dead cards %s", len(deadcards))
    logger.info('Dead cards %s', deadcards) 
    ontable = []
    return ontable, deadcards


def round_flow(attacker, defender, ontable, hands, deadcards):
    """This is one round

    """
    move = 0
    while True:
        move += 1
        logger.info("Move: %s", move)

        # First move
        if len(ontable) == 0 and len(hands[attacker]) > 0:
            att_choice, ontable = att_first(hands, attacker, ontable)
        else:
            att_choice = att_more(ontable)
            if not att_choice:
                ontable, deadcards = bita(ontable, deadcards)
                break
                
        possible_moves, hands = get_possible_defense_move(att_choice, hands)
        if possible_moves:  
            def_choice = possible_moves[0]
            logger.info("Defender chose: %s", def_choice)
            ontable[-1].append(def_choice)
            hands[defender].remove(def_choice)
            if len(ontable) < 4:
                for x in ontable:
                    if x[0] == x[-1]:
                        attacker, defender = defender, attacker
        else:
            if hands[defender]:
                ontable, hands = namo(ontable, hands, defender)
                    
    logger.info("Attacker %s", hands[attacker])
    logger.info("Defender %s" , hands[defender])
    logger.info("On table %s", ontable)

    ontable, attacker, defender, hands = round_end(ontable, attacker, defender, hands)

def game_flow(hands, defender, attacker, trump_deck, deadcards):
    """Whole game.

    Game consits of players 2-4.
    Game consists of cards.
    Game consists of rounds.

    Game ends when only only one or zero players have 0 cards and there are 0 cards to take from the floor
    """
    result = ''
    #for i in range(2):
    round = 0
    while hands[defender] and hands[attacker]:
        round += 1
        logger.info('Round %s', round)
        round_flow(attacker, defender, ontable, hands, deadcards)
        if round == 3:
            return 'test'
    else:
        if len(trump_deck) == 0 and len(hands[attacker]) == 0 and len(hands[defender]) == 0:
            result['result'] = 'draw'
        elif len(trump_deck) == 0 and len(hands[attacker]) > 0 and len(hands[defender]) == 0:
            result = 'defender wins'
        elif len(trump_deck) == 0 and len(hands[attacker]) == 0 and len(hands[defender]) > 0:
            result = 'attacker wins'
            logger.info("game ends: Attacker wins")
            return result



if __name__ == "__main__":
    logger.info("The game 'Stupid' is now starting...", )
    deck = shuffled_deck()
    hands = {}
    hands["P1"], hands["P2"], trump_deck, trump_show = deal_cards(deck)
    logger.info(hands)
    logger.info(trump_show)
    trump_suit = trump_show[1]
    ontable = []  # Cards that are on table
    deadcards = []  # Dead cards are ...
    attacker = "P1" 
    defender = "P2"
    Round = 0

    result = game_flow(hands, defender, attacker, trump_deck, deadcards)
    logger.debug('Result: %s', result)

'''

    Round += 1
    logger.info("Round Nr.:", Round)
    logger.info("Trump deck: %s\n" % trump_deck, 
        "Attacker hand:", hands[attacker], 
        "Defender hand:", hands[defender], 
        "Trump show:", trump_show,
        "Trump suit:", trump_suit,
    )
    '''