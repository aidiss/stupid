# This is Durnius AI software.
# counts the maximum known situation.


#main init
def durnius_ai_start(ai_type,number_of_players):
    if ai_type == 1:
        ai_perfect_knowledge(number_of_players)
    elif ai_type == 2:
        ai_partial_knowledge(number_of_players)
    elif ai_type == 3:
        ai_no_memory(number_of_players)
#three types
def ai_perfect_knowledge(number_of_players):
    pass

def ai_partial_knowledge(number_of_players):
    pass

def ai_no_memory(number_of_players):
    pass



####### Simple stats
def get_len_trump_deck(trump_deck):
    return len(trump_deck)

def get_len_my_hand():
    pass

def get_len_op_hand():
    pass

def get_len_ontable():
    pass

def get_len_dead_deck():
    pass

def get_len_stats(get_len_trump_deck,get_len_my_hand,get_len_op_hand,get_len_ontable,get_len_dead_deck):
    x = 0
    x = get_len_my_hand - get_len_op_hand

########### basic knowledge - collects information about known cards

def get_my_hand():
    pass
def get_op_hand():
    pass
def get_dead_deck():
    pass


def get_basic_info(get_my_hand, get_op_hand, get_dead_deck, ontable):

######### Possibility checks
def get_pos_trump_cards_in_deck(get_basic_info):
    pass
def get_pos_trump_cards_in_op_hand(get_basic_info):
    pass
def get_pos_high_cards_in_op_hand(get_basic_info):
    pass
def get_pos_high_cards_in_deck(get_basic_info):
    pass
def get_pot_value_of_deck(get_known_op_hand):
    pass
def get_pot_value_of_everything(get_pos_high_cards_in_deck,get_pos_high_cards_in_op_hand,get_pos_trump_cards_in_deck,get_pos_trump_cards_in_op_hand):
    pass
def get_guess_of_op_hand(get_op_hand,get_my_hand,get_trump):
    pass

def get_estimated_knowledge(get_basic_info(), get_pot_value_of_everything(), get_guess_of_op_hand())



######### assess values
def get_bita_val(get_simple_knowledge, get_assess_next_round, 
def get_home_val(hand_size, pos_of_good_card, get_strength_of_ontable)
    pass

#########decision checks



######## Forced moves. Checks for wining situations


####Does this move lead to victory?
