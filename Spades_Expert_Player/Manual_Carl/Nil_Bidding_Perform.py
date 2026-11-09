#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 10:19:26 2021

This script is for studying 56 different potential Nil hands of the forms:
    #Maximum potential for Nil bid
    0 high spade(s), 0 low spade(s), 0 ace(s), 0 king(s)
    
    #Kings block
    0 high spade(s), 0 low spade(s), 0 ace(s), 1 king(s)
    0 high spade(s), 0 low spade(s), 0 ace(s), 2 king(s)
    0 high spade(s), 0 low spade(s), 0 ace(s), 3 king(s)                       4 forms
    
    [0,0,0,0],[0,0,0,1],[0,0,0,2],[0,0,0,3]
    
    #Kings and Aces block
    0 high spade(s), 0 low spade(s), 1 ace(s), 0 king(s)
    0 high spade(s), 0 low spade(s), 2 ace(s), 0 king(s)
    0 high spade(s), 0 low spade(s), 1 ace(s), 1 king(s)
    0 high spade(s), 0 low spade(s), 1 ace(s), 2 king(s)
    0 high spade(s), 0 low spade(s), 2 ace(s), 1 king(s)
    0 high spade(s), 0 low spade(s), 2 ace(s), 2 king(s)                       10 forms
    
    [0,0,1,0],[0,0,2,0],[0,0,1,1],[0,0,1,2],[0,0,2,1],[0,0,2,2]
    
    #Low spades block
    0 high spade(s), 1 low spade(s), 0 ace(s), 0 king(s)
    0 high spade(s), 2 low spade(s), 0 ace(s), 0 king(s)
    0 high spade(s), 3 low spade(s), 0 ace(s), 0 king(s)

    [0,1,0,0],[0,2,0,0],[0,3,0,0]
    
    #Low spades and Kings block
    0 high spade(s), 1 low spade(s), 0 ace(s), 1 king(s)
    0 high spade(s), 1 low spade(s), 0 ace(s), 2 king(s)
    0 high spade(s), 1 low spade(s), 0 ace(s), 3 king(s)
    0 high spade(s), 2 low spade(s), 0 ace(s), 1 king(s)
    0 high spade(s), 2 low spade(s), 0 ace(s), 2 king(s)
    0 high spade(s), 2 low spade(s), 0 ace(s), 3 king(s)                       19 forms
    
    [0,1,0,1],[0,1,0,2],[0,1,0,3],[0,2,0,1],[0,2,0,2],[0,2,0,3]
    
    #Low spades, Aces and kings block
    0 high spade(s), 1 low spade(s), 1 ace(s), 0 king(s)
    0 high spade(s), 1 low spade(s), 2 ace(s), 0 king(s)
    0 high spade(s), 1 low spade(s), 1 ace(s), 1 king(s)
    0 high spade(s), 1 low spade(s), 1 ace(s), 2 king(s)
    0 high spade(s), 1 low spade(s), 2 ace(s), 1 king(s)
    0 high spade(s), 1 low spade(s), 2 ace(s), 2 king(s)
    0 high spade(s), 2 low spade(s), 1 ace(s), 0 king(s)
    0 high spade(s), 2 low spade(s), 2 ace(s), 0 king(s)
    0 high spade(s), 2 low spade(s), 1 ace(s), 1 king(s)
    0 high spade(s), 2 low spade(s), 1 ace(s), 2 king(s)
    0 high spade(s), 2 low spade(s), 2 ace(s), 1 king(s)
    0 high spade(s), 2 low spade(s), 2 ace(s), 2 king(s)                       31 forms
    
    [0,1,1,0],[0,1,2,0],[0,1,1,1],[0,1,1,2],[0,1,2,1],
    [0,1,2,2],[0,2,1,0],[0,2,2,0],[0,2,1,1],[0,2,1,2],
    [0,2,2,1],[0,2,2,2]
    
    #High spades block
    1 high spade(s), 0 low spade(s), 0 ace(s), 0 king(s)
    2 high spade(s), 0 low spade(s), 0 ace(s), 0 king(s)
    3 high spade(s), 0 low spade(s), 0 ace(s), 0 king(s)
    
    [1,0,0,0],[2,0,0,0],[3,0,0,0]
    
    #High spades and Kings block
    1 high spade(s), 0 low spade(s), 0 ace(s), 1 king(s)
    1 high spade(s), 0 low spade(s), 0 ace(s), 2 king(s)
    2 high spade(s), 0 low spade(s), 0 ace(s), 1 king(s)
    2 high spade(s), 0 low spade(s), 0 ace(s), 2 king(s)                       38 forms

    [1,0,0,1],[1,0,0,2],[2,0,0,1],[2,0,0,2]
    
    #High spades, aces and Kings block
    1 high spade(s), 0 low spade(s), 1 ace(s), 0 king(s)
    1 high spade(s), 0 low spade(s), 1 ace(s), 1 king(s)
    2 high spade(s), 0 low spade(s), 1 ace(s), 0 king(s)
    2 high spade(s), 0 low spade(s), 1 ace(s), 1 king(s)
    1 high spade(s), 0 low spade(s), 2 ace(s), 0 king(s)
    1 high spade(s), 0 low spade(s), 2 ace(s), 1 king(s)                       44 forms
    
    [1,0,1,0],[1,0,1,1],[2,0,1,0],[2,0,1,1],[1,0,2,0],[1,0,2,1]
    
    #High spades and Low spades block
    1 high spade(s), 1 low spade(s), 0 ace(s), 0 king(s)
    1 high spade(s), 2 low spade(s), 0 ace(s), 0 king(s)
    2 high spade(s), 1 low spade(s), 0 ace(s), 0 king(s)

    [1,1,0,0],[1,2,0,0],[2,1,0,0]
    
    #High spades, Low spades and Kings block
    1 high spade(s), 1 low spade(s), 0 ace(s), 1 king(s)
    1 high spade(s), 2 low spade(s), 0 ace(s), 1 king(s)
    2 high spade(s), 1 low spade(s), 0 ace(s), 1 king(s)                       50 forms

    [1,1,0,1],[1,2,0,1],[2,1,0,1]
    
    #High spades, Low spades and Aces block
    1 high spade(s), 1 low spade(s), 1 ace(s), 0 king(s)
    1 high spade(s), 2 low spade(s), 1 ace(s), 0 king(s)
    2 high spade(s), 1 low spade(s), 1 ace(s), 0 king(s)
    
    [1,1,1,0],[1,2,1,0],[2,1,1,0]
    
    #High spades, Low spades and Aces block
    1 high spade(s), 1 low spade(s), 1 ace(s), 1 king(s)
    1 high spade(s), 2 low spade(s), 1 ace(s), 1 king(s)
    2 high spade(s), 1 low spade(s), 1 ace(s), 1 king(s)                       56 forms
    
    [1,1,1,1],[1,2,1,1],[2,1,1,1]
    
With spade classification defined as:
    Kopp Var:
        low -  3,4,5
        high - 6,7,8,9
    
    Std Var:
        low -  2,3,4
        high - 5,6,7
        
A separate study may be dedicated to the same algorithm with forms that include
face cards and higher depending on the success of this study
    
@author: justinpaul
"""

def Pot_Nil_Hand_Gen(Limit_Vector,Variation):
    #Import the random library
    import random
    
    #Establish invariant card categories
    Kings = [25,38,51]
    Aces = [26,39,52]
    if (Variation == 'Kopp'):
        #Establish card categories for Kopp Var
        Low_Cards = [23,36,49,24,37,50,22,35,48,21,34,47,20,33,46,19,
                     32,45,18,31,44,17,30,43,16,29,42,15,28,41,27]
        Low_Spades = [4,3,2]
        High_Spades = [8,7,6,5]
        #Excluding Js - Big
    else:
        #Establish card categories for Std Var
        Low_Cards = [23,36,49,24,37,50,22,35,48,21,34,47,20,33,46,19,
                     32,45,18,31,44,17,30,43,16,29,42,15,28,41,27,40,14]
        Low_Spades = [3,2,1]
        High_Spades = [6,5,4]
        #Excluding 8s - As
        
    #Calculate quantity of low cards to randomize
    limit_sum = sum(Limit_Vector)
    n = 13 - limit_sum
    
    #Gather n unique Low cards
    low_card_hand = []
    while (len(low_card_hand) < n):
        card = Low_Cards[random.randint(0,(len(Low_Cards)-1))]
        if (card in low_card_hand):
            continue
        else:
            low_card_hand.append(card)
    #Gather High Spades limit cards
    hs_cards = []
    if (Limit_Vector[0] != 0):
        while (len(hs_cards) < Limit_Vector[0]):
            card = High_Spades[random.randint(0,len(High_Spades)-1)]
            if (card in hs_cards):
                continue
            else:
                hs_cards.append(card)
    #Gather Low Spades limit cards
    ls_cards = []
    if (Limit_Vector[1] != 0):
        while (len(ls_cards) < Limit_Vector[1]):
            card = Low_Spades[random.randint(0,len(Low_Spades)-1)]
            if (card in ls_cards):
                continue
            else:
                ls_cards.append(card)
    #Gather Aces limit cards
    ace_cards = []
    if (Limit_Vector[2] != 0):
        while (len(ace_cards) < Limit_Vector[2]):
            card = Aces[random.randint(0,len(Aces)-1)]
            if (card in ace_cards):
                continue
            else:
                ace_cards.append(card)
    #Gather Kings limit cards
    king_cards = []
    if (Limit_Vector[3] != 0):
        while (len(king_cards) < Limit_Vector[3]):
            card = Kings[random.randint(0,len(Kings)-1)]
            if (card in king_cards):
                continue
            else:
                king_cards.append(card)
    
    output_hand = low_card_hand + hs_cards + ls_cards + ace_cards + king_cards
    return(output_hand)

def Nil_Bid_Perform_Param_Est():
    import time
    import Carl_Bidding_With_MCS_Kopp_Var
    import Carl_Bidding_With_MCS_Std
    '''
    Set the investigation fidelity parameters
     -bid time: this gives you accurate numbers for a specific hand
     -number of MCS: this gives you accurate numbers for a specific form
    '''
    bid_time_permit = 10
    num_of_MCS = 500
    '''
    Set the limit vectors for testing and variation
    '''
    Limit_Vectors_4_Test = [[0,0,0,0],[0,0,0,1],[0,0,0,2],[0,0,0,3],
                            [0,0,1,0],[0,0,2,0],[0,0,1,1],[0,0,1,2],
                            [0,0,2,1],[0,0,2,2],[0,1,0,0],[0,2,0,0],
                            [0,3,0,0],[0,1,0,1],[0,1,0,2],[0,1,0,3],
                            [0,2,0,1],[0,2,0,2],[0,2,0,3],[0,1,1,0],
                            [0,1,2,0],[0,1,1,1],[0,1,1,2],[0,1,2,1],
                            [0,1,2,2],[0,2,1,0],[0,2,2,0],[0,2,1,1],
                            [0,2,1,2],[0,2,2,1],[0,2,2,2],[1,0,0,0],
                            [2,0,0,0],[3,0,0,0],[1,0,0,1],[1,0,0,2],
                            [2,0,0,1],[2,0,0,2],[1,0,1,0],[1,0,1,1],
                            [2,0,1,0],[2,0,1,1],[1,0,2,0],[1,0,2,1],
                            [1,1,0,0],[1,2,0,0],[2,1,0,0],[1,1,0,1],
                            [1,2,0,1],[2,1,0,1],[1,1,1,0],[1,2,1,0],
                            [2,1,1,0],[1,1,1,1],[1,2,1,1],[2,1,1,1]]
    Variation = 'Kopp'
    '''
    Set progress update timing parameters
    '''
    prnt_time = 30
    prnt_time_inc = 30
    start_time = time.time()
    
    '''
    Open the write file
    '''
    wrt_fl_nm = 'Nil_Bid_Perform.txt'
    wrt_fl_obj = open(wrt_fl_nm,'a')
    
    for lvt in range(len(Limit_Vectors_4_Test)):
        lim_vect = Limit_Vectors_4_Test[lvt]
        Carl_Bid_dict = {}
        num_of_games = 0
        for mcs in range(num_of_MCS):
            if ((time.time() - start_time) > prnt_time):
                #Calculate progress metrics
                lvt_prog = round(((lvt+1)/len(Limit_Vectors_4_Test))*100,3)
                mcs_prog = round(((mcs+1)/num_of_MCS)*100,3)
                prnt_time_str = round((time.time() - start_time)/60,3)
                
                prnt_stmt_1 = 'Limit Vector progress: ' + str(lvt_prog) + ' %\n'
                prnt_stmt_2 = 'MCS progress: ' + str(mcs_prog) + ' %\n'
                prnt_stmt_3 = 'at ' + str(prnt_time_str) + ' minutes\n'
                
                prnt_stmt = prnt_stmt_1 + prnt_stmt_2 + prnt_stmt_3
                print(prnt_stmt)
                prnt_time += prnt_time_inc
            #Pull a new nil hand
            new_nil_hand = Pot_Nil_Hand_Gen(lim_vect,Variation)
            #Attempt to bid nil
            if (Variation == 'Kopp'):
                [Player_1_BK_avg,hnd_games,P1_Conv_Books,All_iters,Rnd_Crd_Count_1,Rnd_Crd_Count_2,Rnd_Crd_Count_3] = Carl_Bidding_With_MCS_Kopp_Var.Placing_A_Nil_Bid(new_nil_hand,bid_time_permit)
            else:
                [Player_1_BK_avg,hnd_games,P1_Conv_Books,All_iters,Rnd_Crd_Count_1,Rnd_Crd_Count_2,Rnd_Crd_Count_3] = Carl_Bidding_With_MCS_Std.Placing_A_Nil_Bid(new_nil_hand,bid_time_permit)
            #Calculate the frequency for each book
            for pcb in range(len(P1_Conv_Books)):
                if (P1_Conv_Books[pcb] in Carl_Bid_dict):
                    Carl_Bid_dict[P1_Conv_Books[pcb]] += 1
                else:
                    Carl_Bid_dict[P1_Conv_Books[pcb]] = 1
            num_of_games += hnd_games
        sort_keys_list = sorted(Carl_Bid_dict)
        #Print the frequencies
        wrt_fl_obj.write('Limit Vector: \n')
        lim_vect_str = ''
        for lv in range(len(lim_vect)):
            lim_vect_str = lim_vect_str + str(lim_vect[lv]) + ' '
        lim_vect_str = lim_vect_str + '\n'
        wrt_fl_obj.write(lim_vect_str)
        for key in sort_keys_list:
            freq = round((Carl_Bid_dict[key]/num_of_games)*100,2)
            prnt_stmt = 'Chance of winning ' + str(key) + ' books: ' + str(freq) + '%\n'
            wrt_fl_obj.write(prnt_stmt)
        wrt_fl_obj.write('\n')
    
    #Finish print statement
    prnt_time_str = round((time.time() - start_time)/60,3)
    prnt_stmt = 'Finished at ' + str(prnt_time_str) + ' minutes'
    return(1)

Nil_Bid_Perform_Param_Est()