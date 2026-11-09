# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 15:04:20 2020

A bidding program based on Carl

***solving reneging issue***

Added "Carl playing for     Nil" program
      "Carl playing with    Nil" program
      "Carl playing against Nil" program
      
And modified script to leverage the added programs 

@author: justin paul
"""

'''Limbic System'''

def Random_Cards(n,input_hand):
    #Import the random library
    import random
    #Gather n unique cards
    output_hand = []
    while (len(output_hand) < n):
        #Call random integer for next card
        card = random.randint(1,52)
        if (card in input_hand) or (card in output_hand):
            #Skip duplicate card
            continue
        else:
            #Append unique card
            output_hand.append(card)
    #Give the hand back to main driver
    return(output_hand)

def partition(arr,low,high): 
	i = ( low-1 )		 # index of smaller element 
	pivot = arr[high]	 # pivot 
	for j in range(low , high): 
		# If current element is smaller than or 
		# equal to pivot 
		if arr[j] <= pivot: 
			# increment index of smaller element 
			i = i+1
			arr[i],arr[j] = arr[j],arr[i] 
	arr[i+1],arr[high] = arr[high],arr[i+1] 
	return ( i+1 )

def quickSort(arr,low,high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr,low,high)
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
    return(arr)

def Obtain_Suits(hand):
    #Initialize suit list
    suit_list = []
    #Iterate through each card to find the identity
    for i in range(len(hand)):
        #Identify the value
        if (hand[i] < 14):
            #Modulo not required for first suit
            value = int(hand[i]) + 1
            #First suit is spades
            suit = "s"
        else:
            if ((hand[i] % 13) == 0):
                #Check if the card is an Ace
                value = 14
                #Identify the suit
                suit = (int(hand[i]) - (value - 1))/13
            else:
                #Modulo required for all suits above the first
                value = (int(hand[i]) % 13) + 1
                #Identify the suit
                suit = (int(hand[i]) - (value - 1))/13
        #Convert to conventional card identification
        if (suit == 1):
            suit = "d"
        elif (suit == 2):
            suit = "c"
        elif (suit == 3):
            suit = "h"
        #Append suits to suit list
        suit_list.append(suit)
    return(suit_list)

def Obtain_Vals(hand):
    #Cycle through each card to obtain values
    value_list = []
    for i in range(len(hand)):
        #Identify the value
        if (hand[i] < 14):
            #Modulo not required for first suit
            value = int(hand[i]) + 1
        else:
            if ((hand[i] % 13) == 0):
                #Check if the card is an Ace
                value = 14
            else:
                #Modulo required for all suits above the first
                value = (int(hand[i]) % 13) + 1
        #Append the value to value list
        value_list.append(value)
    return(value_list)

def Org_Ply_Rnd_Hnd(Player):
    #Obtain suit list of cards
    suit_list = Obtain_Suits(Player)
    #Progress through the player's cards and organize by suit
    new_Player = [[],[],[],[]]
    for pcs in range(len(Player)):
        if (suit_list[pcs] == 'c'):
            new_Player[0].append(Player[pcs])
        elif (suit_list[pcs] == 'h'):
            new_Player[1].append(Player[pcs])
        elif (suit_list[pcs] == 'd'):
            new_Player[2].append(Player[pcs])
        elif (suit_list[pcs] == 's'):
            new_Player[3].append(Player[pcs])
    return(new_Player)

def Rand_Sub_Ply_Card(sub_Player):
    #Import random library
    import random
    #Ensure the selected suitlist has cards
    rand_suit_list = []
    while (rand_suit_list == []):
        #Call a random index for first three suits
        rand_suit = random.randint(1,len(sub_Player))
        #Grab the random suit list
        rand_suit_list = sub_Player[rand_suit-1]
    #Grab a random index for the random suit list
    rand_card_index = random.randint(0,len(rand_suit_list)-1)
    #Grab the random card
    rand_card = rand_suit_list[rand_card_index]
    return(rand_card)

def Rand_Play(First_Card,Player,First_Cut):
    #Determine if player has cards other than spades
    other_card_count = []
    for occ in range(len(Player)-1):
        #Grab each suit list length
        other_card_count.append(len(Player[occ]))
    if (sum(other_card_count) > 0):
        Only_Spades = 0
    else:
        Only_Spades = 1
    #Get the suit of the first card
    if (First_Card == 0):
        FC_suit = [0]
    else:
        FC_suit = Obtain_Suits([First_Card])
    if (FC_suit[0] == 'c'):
        FC_suit_num = 0
    elif (FC_suit[0] == 'h'):
        FC_suit_num = 1
    elif (FC_suit[0] == 'd'):
        FC_suit_num = 2
    elif (FC_suit[0] == 's'):
        FC_suit_num = 3
    #Check if the first card has already been played
    if (First_Card == 0):
        #Determine if a spade has already been played
        if (First_Cut == 0):
            #Check if player only has spades
            if (Only_Spades == 0):
                #Play a card from all suits excluding spades
                Ply_Card = Rand_Sub_Ply_Card(Player[0:len(Player)-1])
            elif (Only_Spades == 1):
                #Play a spades card
                Ply_Card = Rand_Sub_Ply_Card([Player[3]])
                First_Cut = 1
        elif (First_Cut == 1):
            if (Only_Spades == 0):
                #Play a card of any suit
                Ply_Card = Rand_Sub_Ply_Card(Player)
            elif (Only_Spades == 1):
                #Play a spades card
                Ply_Card = Rand_Sub_Ply_Card([Player[3]])
    elif(First_Card > 0):
        #Check if the player only has spades
        if (Only_Spades == 0):
            #Check if the player has any cards for the same suit
            if (Player[FC_suit_num] == []):
                #Play a card of any suit
                Ply_Card = Rand_Sub_Ply_Card(Player)
                Card_Suit = Obtain_Suits([Ply_Card])
                if (Card_Suit[0] == 's'):
                    First_Cut = 1
            elif (len(Player[FC_suit_num]) > 0):
                #Play a card from the same suit list
                Ply_Card = Rand_Sub_Ply_Card([Player[FC_suit_num]])
        elif (Only_Spades == 1):
            #Play a spades card
            Ply_Card = Rand_Sub_Ply_Card([Player[3]])
    return(Ply_Card)

def Org_Ply_Hnd(Player):
    #Build the ultimate organization list
    ult_org_list = []
    for c in range(27,(39+1)):
        ult_org_list.append(c)
    for h in range(40,(52+1)):
        ult_org_list.append(h)
    for d in range(14,(26+1)):
        ult_org_list.append(d)
    for s in range(1,(13+1)):
        ult_org_list.append(s)
    #Progress through the player's cards and organize by suit
    Player_Indicies = []
    for PI in range(len(Player)):
        Player_Indicies.append(ult_org_list.index(Player[PI]))
    #Sort player indicies
    sorted_Player_Indicies = quickSort(Player_Indicies,0,len(Player_Indicies)-1)
    #Build sorted player
    new_Player = []
    for sPI in range(len(sorted_Player_Indicies)):
        new_Player.append(ult_org_list[sorted_Player_Indicies[sPI]])
    return(new_Player)

def Book_Grading(book,First_Card):
    #Get the suit of the first card
    FC_suit = Obtain_Suits([First_Card])
    Hierarchy = []
    #Build the beginning of the list hierarchy
    if (FC_suit[0] == 'c'):
        for lc in range(1,14):
            Hierarchy.append(lc+(13*2))
    elif (FC_suit[0] == 'd'):
        for lc in range(1,14):
            Hierarchy.append(lc+(13*1))
    elif (FC_suit[0] == 'h'):
        for lc in range(1,14):
            Hierarchy.append(lc+(13*3))
    elif (FC_suit[0] == 's'):
        Hierarchy = []
    #Append the spades Hierarchy
    for lc in range(1,14):
        Hierarchy.append(lc)
    #Get the ranks of each card
    card_ranks = []
    for bk in range(len(book)):
        if (book[bk] in Hierarchy):
            card_ranks.append(Hierarchy.index(book[bk]))
        else:
            card_ranks.append(-1)
    #Get the maximum rank card
    mx_crd_rnk_index = card_ranks.index(max(card_ranks))
    #Get the winning player
    winning_ply = mx_crd_rnk_index
    #Get the winning card
    winning_card = book[mx_crd_rnk_index]
    return(winning_card,winning_ply,Hierarchy)

'''Frontal Cortex'''

def Hand_Priority(hand):
    #Establish categories
    Cat_1 = [9,8,7,6,5,4,3,2,1]
    Cat_2 = [10,11,12,13]
    Cat_3 = [26,39,52]
    Cat_4 = [22,35,48,21,34,47,20,33,46,19,32,45,18,
             31,44,17,30,43,16,29,42,15,28,41,14,40,27]
    Cat_5 = [23,36,49,24,37,50,25,38,51]
    #Build the categorical lists into a 1D list
    Mast_Cat_1D = Cat_1 + Cat_2 + Cat_3 + Cat_4 + Cat_5
    #Organize the hand by sorted indicies of established categories
    Carl_cat_list = []
    for h in range(len(hand)):
        Carl_cat_list.append(Mast_Cat_1D.index(hand[h]))
    if (len(Carl_cat_list) > 1):
        Carl_cat_sorted = quickSort(Carl_cat_list,0,len(Carl_cat_list)-1)
    else:
        Carl_cat_sorted = Carl_cat_list
    #Build the sorted list of card values
    Hand_sorted = []
    for ccs in range(len(Carl_cat_sorted)):
        Hand_sorted.append(Mast_Cat_1D[Carl_cat_sorted[ccs]])
    return(Hand_sorted)

def Nil_Priority(hand):
    #Establish categories
    Cat_4 = [22,35,48,21,34,47,20,33,46,19,32,45,18,
             31,44,17,30,43,16,29,42,15,28,41,14,40,27]
    #Prioritize 2c - 10d
    Cat_4.reverse()
    #Prioritize Jd - Kh
    Cat_5 = [23,36,49,24,37,50,25,38,51]
    #Prioritize Aces
    Cat_3 = [26,39,52]
    Cat_1 = [9,8,7,6,5,4,3,2,1]
    #Prioritize low spades
    Cat_1.reverse()
    #Prioritize high spades
    Cat_2 = [10,11,12,13]
    #Build the categorical lists into a 1D list
    Mast_Cat_1D = Cat_4 + Cat_5 + Cat_3 + Cat_1 + Cat_2
    #Organize the hand by sorted indicies of established categories
    Carl_cat_list = []
    for h in range(len(hand)):
        Carl_cat_list.append(Mast_Cat_1D.index(hand[h]))
    if (len(Carl_cat_list) > 1):
        Carl_cat_sorted = quickSort(Carl_cat_list,0,len(Carl_cat_list)-1)
    else:
        Carl_cat_sorted = Carl_cat_list
    #Build the sorted list of card values
    Hand_sorted = []
    for ccs in range(len(Carl_cat_sorted)):
        Hand_sorted.append(Mast_Cat_1D[Carl_cat_sorted[ccs]])
    return(Hand_sorted)

def Opp_Nil_Priority(hand):
    #Establish categories
    Cat_2 = [10,11,12,13]
    #Prioritize high spades
    Cat_2.reverse()
    #Prioritize low spades
    Cat_1 = [9,8,7,6,5,4,3,2,1]
    #Prioritize Aces
    Cat_3 = [26,39,52]
    Cat_5 = [23,36,49,24,37,50,25,38,51]
    #Prioritize Kh - Jd
    Cat_5.reverse()
    #Prioritize 10d - 2c
    Cat_4 = [22,35,48,21,34,47,20,33,46,19,32,45,18,
             31,44,17,30,43,16,29,42,15,28,41,14,40,27]
    #Build the categorical lists into a 1D list
    Mast_Cat_1D = Cat_2 + Cat_1 + Cat_3 + Cat_5 + Cat_4
    #Organize the hand by sorted indicies of established categories
    Carl_cat_list = []
    for h in range(len(hand)):
        Carl_cat_list.append(Mast_Cat_1D.index(hand[h]))
    if (len(Carl_cat_list) > 1):
        Carl_cat_sorted = quickSort(Carl_cat_list,0,len(Carl_cat_list)-1)
    else:
        Carl_cat_sorted = Carl_cat_list
    #Build the sorted list of card values
    Hand_sorted = []
    for ccs in range(len(Carl_cat_sorted)):
        Hand_sorted.append(Mast_Cat_1D[Carl_cat_sorted[ccs]])
    return(Hand_sorted)

def Sub_Nil_Priority(hand):
    #Establish categories
    Cat_1 = [9,8,7,6,5,4,3,2,1]
    Cat_2 = [10,11,12,13]
    Cat_3 = [26,39,52]
    Cat_4 = [22,35,48,21,34,47,20,33,46,19,32,45,18,
             31,44,17,30,43,16,29,42,15,28,41,14,40,27]
    #Prioritize 2c - 10d
    Cat_4.reverse()
    Cat_5 = [23,36,49,24,37,50,25,38,51]
    #Build the categorical lists into a 1D list
    Mast_Cat_1D = Cat_1 + Cat_2 + Cat_3 + Cat_4 + Cat_5
    #Organize the hand by sorted indicies of established categories
    Carl_cat_list = []
    for h in range(len(hand)):
        Carl_cat_list.append(Mast_Cat_1D.index(hand[h]))
    if (len(Carl_cat_list) > 1):
        Carl_cat_sorted = quickSort(Carl_cat_list,0,len(Carl_cat_list)-1)
    else:
        Carl_cat_sorted = Carl_cat_list
    #Build the sorted list of card values
    Hand_sorted = []
    for ccs in range(len(Carl_cat_sorted)):
        Hand_sorted.append(Mast_Cat_1D[Carl_cat_sorted[ccs]])
    return(Hand_sorted)
    
def Reneg_Filter(hand,Hierarchy):
    #Obtain the suit for the first card
    first_suit = Obtain_Suits([Hierarchy[0]])
    suit_list = Obtain_Suits(hand)
    #Check if the hand has the Little or the Big
    for h in range(len(hand)):
        if ((hand[h] == 14) or (hand[h] == 40)):
            suit_list[h] = 's'
    #Filter the hand to yield a hand of only viable cards
    viable_cards = []
    for sl in range(len(suit_list)):
        if (suit_list[sl] == first_suit[0]):
            viable_cards.append(hand[sl])
    if (viable_cards == []):
        viable_cards = hand
    return(viable_cards)

def Lowest_Card(Hierarchy,viable_cards):
    #Initialize the lowest card
    lowest_card = 0
    #Obtain the lowest value viable card in the Hierarchy
    for H in range(len(Hierarchy)):
        if (Hierarchy[H] in viable_cards):
            lowest_card = Hierarchy[H]
            return(lowest_card)
    if (lowest_card == 0):
        #Obtain the values for all cards off suit
        value_list = Obtain_Vals(viable_cards)
        #Obtain index of lowest value off suit card
        low_val_ind = value_list.index(min(value_list))
        #Obtain the lowest card
        lowest_card = viable_cards[low_val_ind]
    return(lowest_card)
    
def Cards_That_Win(winning_card,Hierarchy,viable_cards,sp_flg):
    #Initialize selected card
    selected_card = 0
    #Grab the index of the winning card in the Hierarchy
    win_index = Hierarchy.index(winning_card)
    #Determine what cards can beat the winning card
    cards_that_win = []
    for H in range(len(Hierarchy)):
        if (H > win_index):
            cards_that_win.append(Hierarchy[H])
    Spades_Cards = [13,12,11,10,9,8,7,6,5,4,3,2,1]
    #Check if spades flag is active
    if (sp_flg == 0):
        #Check if hand has cards of first suit
        first_suit = Obtain_Suits([Hierarchy[0]])
        suit_list = Obtain_Suits(viable_cards)
        if (first_suit[0] in suit_list):
            #Remove spades from cards that win
            for SC in range(len(Spades_Cards)):
                if (Spades_Cards[SC] in cards_that_win):
                    cards_that_win.remove(Spades_Cards[SC])
    if (cards_that_win == []):
        #Return 0 if no cards can win
        return(selected_card)
    for ctw in range(len(cards_that_win)):
        if (cards_that_win[ctw] in viable_cards):
            #Return the minimum card to win
            selected_card = cards_that_win[ctw]
            return(selected_card)
    return(selected_card)

def Cards_That_Lose(winning_card,Hierarchy,viable_cards):
    #Grab the index of the winning card in the Hierarchy
    win_index = Hierarchy.index(winning_card)
    #Determine what cards can lose to the winning card
    cards_that_lose = []
    for H in range(len(Hierarchy)):
        if (H < win_index):
            cards_that_lose.append(Hierarchy[H])
    #Initialize selected card
    selected_card = 0
    if (cards_that_lose == []):
        return(selected_card)
    for ctl in range(len(cards_that_lose)):
        if (cards_that_lose[ctl] in viable_cards):
            selected_card = cards_that_lose[ctl]
    return(selected_card)

def Highest_Card(Hierarchy,viable_cards):
    #Initialize the highest card
    highest_card = 0
    #Obtain the highest value viable card in the Hierarchy
    for H in range(len(Hierarchy)):
        if (Hierarchy[H] in viable_cards):
            highest_card = Hierarchy[H]
    if (highest_card == 0):
        #Obtain the values for all cards off suit
        value_list = Obtain_Vals(viable_cards)
        #Obtain index of highest value off suit card
        high_val_ind = value_list.index(max(value_list))
        #Obtain the highest card
        highest_card = viable_cards[high_val_ind]
    return(highest_card)

def Best_Cards_That_Lose(winning_card,Hierarchy,viable_cards):
    #Grab the index of the winning card in the Hierarchy
    win_index = Hierarchy.index(winning_card)
    #Determine what cards can lose to the winning card
    cards_that_lose = []
    for H in range(len(Hierarchy)):
        if (H < win_index):
            cards_that_lose.append(Hierarchy[H])
    #Determine if any viable cards can lose
    best_cards = []
    for vc in range(len(viable_cards)):
        if (viable_cards[vc] in cards_that_lose):
            best_cards.append(viable_cards[vc])
    #Initialize selected card
    selected_card = 0
    if (best_cards == []):
        return(selected_card)
    else:
        #Determine the best card that loses
        selected_card = Highest_Card(Hierarchy,best_cards)
    return(selected_card)

def Determine_Opp_Nil_Bids(Book,players,nil_bid_flgs):
    '''
    Determine one of three situations
    1. You are playing before nil
    2. You are playing after nil
    3. Neither opponent bid nil (or the nil bid is no longer important)
    '''
    #Find position in book
    book_pos = len(Book)+1
    #Find the opponent indicies
    opp_index = []
    for p in range(len(players)):
        if (players[p] == 'O'):
            opp_index.append(p)
    #Find the opponent that bid nil
    if ((nil_bid_flgs[opp_index[0]] == 1) and (book_pos < opp_index[0])):
        #This would be if you were starting the book
        bid_situ_flg = 1
        nil_bid_index = opp_index[0]
    elif ((nil_bid_flgs[opp_index[1]] == 1) and (book_pos < opp_index[1])):
        #This would be if you were third in the book
        bid_situ_flg = 1
        nil_bid_index = opp_index[1]
    elif ((nil_bid_flgs[opp_index[0]] == 1) and (book_pos > opp_index[0])):
        #This would be if you were second in the book
        bid_situ_flg = 2
        nil_bid_index = opp_index[0]
    elif ((nil_bid_flgs[opp_index[1]] == 1) and (book_pos > opp_index[1])):
        #This would be if you were fourth in the book
        bid_situ_flg = 2
        nil_bid_index = opp_index[1]
    else:
        bid_situ_flg = 3
        nil_bid_index = 'N/A'
    return(bid_situ_flg,nil_bid_index)

'''Neocortex'''

def Carl(Book,hand,sp_flg,players,Team_Books,Team_Bids,Rnd_Crd_Count):
    Spades_Cards = [13,12,11,10,9,8,7,6,5,4,3,2,1]
    Card_to_play = None
    #Check position in book
    if (Book == []):
        Hand_Sorted = Hand_Priority(hand)
        #Play the first card in hand priority
        if (sp_flg == 1):
            Card_to_play = Hand_Sorted[0]
        else:
            #If no spades played, play a card that isn't a spade
            for hs in range(len(Hand_Sorted)):
                if (Hand_Sorted[hs] not in Spades_Cards):
                    Card_to_play = Hand_Sorted[hs]
        #If spades are the only cards left, play that card
        if (Card_to_play == None):
            Card_to_play = Hand_Sorted[0]
        #Check if first cut has been made
        if (Card_to_play in Spades_Cards):
            sp_flg = 1
        return(Card_to_play,sp_flg,Rnd_Crd_Count)
    else:
        #Determine which card in the book is winning
        [winning_card,winning_ply,Hierarchy] = Book_Grading(Book,Book[0])
        #Filter the hand
        viable_cards = Reneg_Filter(hand,Hierarchy)
        #Determine the corresponding player
        winning_ply = players[winning_ply]
        #Determine if books need to be won
        if (Team_Books < Team_Bids):
            if (winning_ply == 'T'):
                #Play the lowest card since the teammate is winning the book
                lowest_card = Lowest_Card(Hierarchy,viable_cards)
                Card_to_play = lowest_card
            elif (winning_ply == 'O'):
                #Determine if the book can be won
                selected_card = Cards_That_Win(winning_card,Hierarchy,viable_cards,sp_flg)
                if (selected_card == 0):
                    #The book cannot be won so play the lowest card
                    lowest_card = Lowest_Card(Hierarchy,viable_cards)
                    Card_to_play = lowest_card
                else:
                    #The book can be won so play the selected card
                    Card_to_play = selected_card
        else:
            #Books do not need to be won so lose as efficiently as possible
            selected_card = Cards_That_Lose(winning_card,Hierarchy,viable_cards)
            if (selected_card == 0):
                #The book cannot be lost so play the highest card
                highest_card = Highest_Card(Hierarchy,viable_cards)
                Card_to_play = highest_card
            else:
                #The book can be lost so play the selected card
                Card_to_play = selected_card
        #If Card_to_play not designated play a random card
        if (Card_to_play == None):
            Rnd_Crd_Count += 1
            rnd_hnd_sorted = Org_Ply_Rnd_Hnd(viable_cards)
            if (Book == []):
                Card_to_play = Rand_Play(0,rnd_hnd_sorted,sp_flg)
            else:
                Card_to_play = Rand_Play(Book[0],rnd_hnd_sorted,sp_flg)
    #Check if first cut has been made
    if (Card_to_play in Spades_Cards):
        sp_flg = 1
    return(Card_to_play,sp_flg,Rnd_Crd_Count)

def Carl_Against_Nil(Book,hand,sp_flg,players,Team_Books,Team_Bids,nil_bid_flgs,Nil_Player_Books,Rnd_Crd_Count):
    Spades_Cards = [13,12,11,10,9,8,7,6,5,4,3,2,1]
    Card_to_play = None
    #Check position in book
    if ((Book == []) and (Nil_Player_Books == 0)):
        [bid_situ_flg,nil_bid_index] = Determine_Opp_Nil_Bids(Book,players,nil_bid_flgs)
        if ((bid_situ_flg == 1) or (bid_situ_flg == 2)):
            Hand_Sorted = Sub_Nil_Priority(hand)
            #Play the first card in hand priority
            if (sp_flg == 1):
                Card_to_play = Hand_Sorted[0]
            else:
                #If no spades played, play a card that isn't a spade
                for hs in range(len(Hand_Sorted)):
                    if (Hand_Sorted[hs] not in Spades_Cards):
                        Card_to_play = Hand_Sorted[hs]
            #If spades are the only cards left, play that card
            if (Card_to_play == None):
                Card_to_play = Hand_Sorted[0]
            #Check if first cut has been made
            if (Card_to_play in Spades_Cards):
                sp_flg = 1
            
            #If Card_to_play not designated play a random card
            if (Card_to_play == None):
                Rnd_Crd_Count += 1
                rnd_hnd_sorted = Org_Ply_Rnd_Hnd(hand)
                if (Book == []):
                    Card_to_play = Rand_Play(0,rnd_hnd_sorted,sp_flg)
                else:
                    Card_to_play = Rand_Play(Book[0],rnd_hnd_sorted,sp_flg)
        else:
            [Card_to_play,sp_flg,Rnd_Crd_Count] = Carl(Book,hand,sp_flg,players,Team_Books,Team_Bids,nil_bid_flgs,Nil_Player_Books)
        return(Card_to_play,sp_flg,Rnd_Crd_Count)
    elif ((len(Book) > 0) and (Nil_Player_Books == 0)):
        #Determine which card in the book is winning
        [winning_card,winning_ply,Hierarchy] = Book_Grading(Book,Book[0])
        #Filter the hand
        viable_cards = Reneg_Filter(hand,Hierarchy)
        #Examine the nil opponent situation
        [bid_situ_flg,nil_bid_index] = Determine_Opp_Nil_Bids(Book,players,nil_bid_flgs)
        if (bid_situ_flg == 1):
            #Try to subvert the nil player who hasn't played yet with nil priority
            Hand_Sorted = Sub_Nil_Priority(viable_cards)
            #Play the first card in hand priority
            if (sp_flg == 1):
                Card_to_play = Hand_Sorted[0]
            else:
                #If no spades played, play a card that isn't a spade
                for hs in range(len(Hand_Sorted)):
                    if (Hand_Sorted[hs] not in Spades_Cards):
                        Card_to_play = Hand_Sorted[hs]
            #If spades are the only cards left, play that card
            if (Card_to_play == None):
                Card_to_play = Hand_Sorted[0]
        elif (bid_situ_flg == 2):
            #Check if the nil player is winning
            if (winning_ply == nil_bid_index):
                selected_card = Cards_That_Lose(winning_card,Hierarchy,viable_cards)
                if (selected_card == 0):
                    #The book cannot be lost so efficiently win the book
                    selected_card = Cards_That_Win(winning_card,Hierarchy,viable_cards,sp_flg)
                    Card_to_play = selected_card
                else:
                    #The book can be lost
                    selected_card = Best_Cards_That_Lose(winning_card,Hierarchy,viable_cards)
                    Card_to_play = selected_card
            #If Card_to_play not designated play a random card
            if (Card_to_play == None):
                Rnd_Crd_Count += 1
                rnd_hnd_sorted = Org_Ply_Rnd_Hnd(viable_cards)
                if (Book == []):
                    Card_to_play = Rand_Play(0,rnd_hnd_sorted,sp_flg)
                else:
                    Card_to_play = Rand_Play(Book[0],rnd_hnd_sorted,sp_flg)
        else:
            [Card_to_play,sp_flg,Rnd_Crd_Count] = Carl(Book,hand,sp_flg,players,Team_Books,Team_Bids,nil_bid_flgs,Nil_Player_Books)
    else:
        [Card_to_play,sp_flg,Rnd_Crd_Count] = Carl(Book,hand,sp_flg,players,Team_Books,Team_Bids,nil_bid_flgs,Nil_Player_Books)
    #Check if first cut has been made
    if (Card_to_play in Spades_Cards):
            sp_flg = 1
    return(Card_to_play,sp_flg,Rnd_Crd_Count)

def Carl_Ply4_Nil(Book,hand,sp_flg,players,Rnd_Crd_Count):
    Spades_Cards = [13,12,11,10,9,8,7,6,5,4,3,2,1]
    Card_to_play = None
    #Check position in book
    if (Book == []):
        #Organize the hand by Nil priority
        Hand_Sorted = Nil_Priority(hand)
        #Play the first card in hand priority
        if (sp_flg == 1):
            Card_to_play = Hand_Sorted[0]
        else:
            #If no spades played, play a card that isn't a spade
            for hs in range(len(Hand_Sorted)):
                if (Hand_Sorted[hs] not in Spades_Cards):
                    Card_to_play = Hand_Sorted[hs]
        #If spades are the only cards left, play that card
        if (Card_to_play == None):
            Card_to_play = Hand_Sorted[0]
        return(Card_to_play,sp_flg,Rnd_Crd_Count)
    else:
        #Determine which card in the book is winning
        [winning_card,winning_ply,Hierarchy] = Book_Grading(Book,Book[0])
        #Filter the hand
        viable_cards = Reneg_Filter(hand,Hierarchy)
        #Play the best card that can lose
        Card_to_play = Best_Cards_That_Lose(winning_card,Hierarchy,viable_cards)
        
        #If no card can be played that garuntees losing the book, play the lowest card
        if (Card_to_play == 0):
            Card_to_play = Lowest_Card(Hierarchy,viable_cards)
        
        #If Card_to_play not designated play a random card
        if ((Card_to_play == None) or (Card_to_play not in viable_cards)):
            Rnd_Crd_Count += 1
            rnd_hnd_sorted = Org_Ply_Rnd_Hnd(viable_cards)
            if (Book == []):
                Card_to_play = Rand_Play(0,rnd_hnd_sorted,sp_flg)
            else:
                Card_to_play = Rand_Play(Book[0],rnd_hnd_sorted,sp_flg)
    #Check if first cut has been made
    if (Card_to_play in Spades_Cards):
        sp_flg = 1
    return(Card_to_play,sp_flg,Rnd_Crd_Count)

def Carl_Ply_W_Nil(Book,hand,sp_flg,players,Rnd_Crd_Count):
    Spades_Cards = [13,12,11,10,9,8,7,6,5,4,3,2,1]
    Card_to_play = None
    #Check position in book
    if (Book == []):
        #Organize the hand by Nil priority
        Hand_Sorted = Opp_Nil_Priority(hand)
        #Play the first card in hand priority
        if (sp_flg == 1):
            Card_to_play = Hand_Sorted[0]
        else:
            #If no spades played, play a card that isn't a spade
            for hs in range(len(Hand_Sorted)):
                if (Hand_Sorted[hs] not in Spades_Cards):
                    Card_to_play = Hand_Sorted[hs]
        #If spades are the only cards left, play that card
        if (Card_to_play == None):
            Card_to_play = Hand_Sorted[0]
    else:
        #Determine which card in the book is winning
        [winning_card,winning_ply,Hierarchy] = Book_Grading(Book,Book[0])
        #Determine the corresponding player
        winning_ply = players[winning_ply]
        #Filter the hand
        viable_cards = Reneg_Filter(hand,Hierarchy)
        #Check if your teammate is already losing
        if ((winning_ply == 'O') and (len(Book) > 1)):
            #Lose as efficiently as possible
            selected_card = Cards_That_Lose(winning_card,Hierarchy,viable_cards)
            if (selected_card == 0):
                #The book cannot be lost so play the lowest card
                lowest_card = Lowest_Card(Hierarchy,viable_cards)
                Card_to_play = lowest_card
            else:
                #The book can be lost so play the selected card
                Card_to_play = selected_card
        else:
            #Facilitate temmate losing the book by winning it
            selected_card = Cards_That_Win(winning_card,Hierarchy,viable_cards,sp_flg)
            if (selected_card == 0):
                #The book cannot be won so play the lowest card
                lowest_card = Lowest_Card(Hierarchy,viable_cards)
                Card_to_play = lowest_card
            else:
                #The book can be lost so play the selected card
                Card_to_play = selected_card
        #If Card_to_play not designated play a random card
        if ((Card_to_play == None) or (Card_to_play not in viable_cards)):
            Rnd_Crd_Count += 1
            rnd_hnd_sorted = Org_Ply_Rnd_Hnd(viable_cards)
            if (Book == []):
                Card_to_play = Rand_Play(0,rnd_hnd_sorted,sp_flg)
            else:
                Card_to_play = Rand_Play(Book[0],rnd_hnd_sorted,sp_flg)
    return(Card_to_play,sp_flg,Rnd_Crd_Count)

def New_Ply_Order(winning_ply,Team_1_players,Team_2_players):
    if (winning_ply == 1):
        ply_order = [1,2,3,4]
        Team_1_players = ['T','O','T','O']
        Team_2_players = ['O','T','O','T']
    elif (winning_ply == 2):
        ply_order = [2,3,4,1]
        Team_1_players = ['O','T','O','T']
        Team_2_players = ['T','O','T','O']
    elif (winning_ply == 3):
        ply_order = [3,4,1,2]
        Team_1_players = ['T','O','T','O']
        Team_2_players = ['O','T','O','T']
    elif (winning_ply == 4):
        ply_order = [4,1,2,3]
        Team_1_players = ['O','T','O','T']
        Team_2_players = ['T','O','T','O']
    return(ply_order,Team_1_players,Team_2_players)

def MCS_Spades_Round(Team_1_Bids,Team_2_Bids,All_Player_Books,
                     Player_1,Player_2,Player_3,Player_4,Rnd_Crd_Count):
    #Initialize the round
    First_Cut = 0
    Team_1_Books = []
    Team_2_Books = []
    Round_Books = len(Player_1)
    ply_order = [1,2,3,4]
    Team_1_players = ['T','O','T','O']
    Team_2_players = ['O','T','O','T']
    while (Round_Books > 0):
        #Subtract a book for each book played
        Round_Books += -1
        #Initialize the book
        Book = []
        #Each Player plays a card
        First_Card = 0
        for plor in range(len(ply_order)):
            if (ply_order[plor] == 1):
                [ply_1_card,First_Cut,Rnd_Crd_Count] = Carl(Book,Player_1,First_Cut,
                                                            Team_1_players,len(Team_1_Books),
                                                            Team_1_Bids,Rnd_Crd_Count)
                #Remove card played from Player 1
                Player_1.remove(ply_1_card)
                if (First_Card == 0):
                    First_Card = ply_1_card
                Book.append(ply_1_card)
            elif (ply_order[plor] == 2):
                [ply_2_card,First_Cut,Rnd_Crd_Count] = Carl(Book,Player_2,First_Cut,
                                                            Team_2_players,len(Team_2_Books),
                                                            Team_2_Bids,Rnd_Crd_Count)
                #Remove card played from Player 2
                Player_2.remove(ply_2_card)
                if (First_Card == 0):
                    First_Card = ply_2_card
                Book.append(ply_2_card)
            elif (ply_order[plor] == 3):
                [ply_3_card,First_Cut,Rnd_Crd_Count] = Carl(Book,Player_3,First_Cut,
                                                            Team_1_players,len(Team_1_Books),
                                                            Team_1_Bids,Rnd_Crd_Count)
                #Remove card played from Player 3
                Player_3.remove(ply_3_card)
                if (First_Card == 0):
                    First_Card = ply_3_card
                Book.append(ply_3_card)
            elif (ply_order[plor] == 4):
                [ply_4_card,First_Cut,Rnd_Crd_Count] = Carl(Book,Player_4,First_Cut,
                                                            Team_2_players,len(Team_2_Books),
                                                            Team_2_Bids,Rnd_Crd_Count)
                #Remove card played from Player 4
                Player_4.remove(ply_4_card)
                if (First_Card == 0):
                    First_Card = ply_4_card
                Book.append(ply_4_card)
        #Evaluate the Book and decide who has the winning card
        [winning_card,winning_ply,Hierarchy] = Book_Grading(Book,First_Card)
        #Use the index to get the actual player number
        winning_ply = ply_order[winning_ply]
        #Generate new player order based on who won the book
        [ply_order,Team_1_players,Team_2_players] = New_Ply_Order(winning_ply,
                                                                  Team_1_players,
                                                                  Team_2_players)
        #Track team books
        if ((winning_ply == 1) or (winning_ply == 3)):
            Team_1_Books.append(winning_card)
        elif ((winning_ply == 2) or (winning_ply == 4)):
            Team_2_Books.append(winning_card)
        #Track player books
        if (winning_ply == 1):
            All_Player_Books[0] += 1
        elif (winning_ply == 2):
            All_Player_Books[1] += 1
        elif (winning_ply == 3):
            All_Player_Books[2] += 1
        elif (winning_ply == 4):
            All_Player_Books[3] += 1
    return(All_Player_Books,Rnd_Crd_Count)

def MCS_Nil_Spades_Round(Team_1_Bids,Team_2_Bids,All_Player_Books,
                         Player_1,Player_2,Player_3,Player_4,
                         nil_bid_flgs,Rnd_Crd_Count_1,
                         Rnd_Crd_Count_2,Rnd_Crd_Count_3):
    #Initialize the round
    First_Cut = 0
    Team_1_Books = []
    Team_2_Books = []
    Round_Books = len(Player_1)
    ply_order = [1,2,3,4]
    Team_1_players = ['T','O','T','O']
    Team_2_players = ['O','T','O','T']
    while (Round_Books > 0):
        #Subtract a book for each book played
        Round_Books += -1
        #Initialize the book
        Book = []
        #Each Player plays a card
        First_Card = 0
        for plor in range(len(ply_order)):
            if (ply_order[plor] == 1):
                [ply_1_card,First_Cut,Rnd_Crd_Count_1] = Carl_Ply4_Nil(Book,Player_1,First_Cut,
                                                                       Team_1_players,Rnd_Crd_Count_1)
                #Remove card played from Player 1
                Player_1.remove(ply_1_card)
                if (First_Card == 0):
                    First_Card = ply_1_card
                Book.append(ply_1_card)
            elif (ply_order[plor] == 2):
                [ply_2_card,First_Cut,Rnd_Crd_Count_3] = Carl(Book,Player_2,First_Cut,
                                                              Team_2_players,len(Team_2_Books),
                                                              Team_2_Bids,Rnd_Crd_Count_3)
                #Remove card played from Player 2
                Player_2.remove(ply_2_card)
                if (First_Card == 0):
                    First_Card = ply_2_card
                Book.append(ply_2_card)
            elif (ply_order[plor] == 3):
                [ply_3_card,First_Cut,Rnd_Crd_Count_2] = Carl_Ply_W_Nil(Book,Player_3,First_Cut,
                                                                        Team_1_players,Rnd_Crd_Count_2)
                #Remove card played from Player 3
                Player_3.remove(ply_3_card)
                if (First_Card == 0):
                    First_Card = ply_3_card
                Book.append(ply_3_card)
            elif (ply_order[plor] == 4):
                [ply_4_card,First_Cut,Rnd_Crd_Count_3] = Carl(Book,Player_4,First_Cut,
                                                              Team_2_players,len(Team_2_Books),
                                                              Team_2_Bids,Rnd_Crd_Count_3)
                #Remove card played from Player 4
                Player_4.remove(ply_4_card)
                if (First_Card == 0):
                    First_Card = ply_4_card
                Book.append(ply_4_card)
        #Evaluate the Book and decide who has the winning card
        [winning_card,winning_ply,Hierarchy] = Book_Grading(Book,First_Card)
        #Use the index to get the actual player number
        winning_ply = ply_order[winning_ply]
        #Generate new player order based on who won the book
        [ply_order,Team_1_players,Team_2_players] = New_Ply_Order(winning_ply,
                                                                  Team_1_players,
                                                                  Team_2_players)
        #Track team books
        if ((winning_ply == 1) or (winning_ply == 3)):
            Team_1_Books.append(winning_card)
        elif ((winning_ply == 2) or (winning_ply == 4)):
            Team_2_Books.append(winning_card)
        #Track player books
        if (winning_ply == 1):
            All_Player_Books[0] += 1
        elif (winning_ply == 2):
            All_Player_Books[1] += 1
        elif (winning_ply == 3):
            All_Player_Books[2] += 1
        elif (winning_ply == 4):
            All_Player_Books[3] += 1
    return(All_Player_Books,Rnd_Crd_Count_1,Rnd_Crd_Count_2,Rnd_Crd_Count_3)

'''Script'''

def Placing_A_Bid(Player_Hand,bid_time_permit):
    import time
    #Start time
    start_time = time.time()
    #Organize the player hand
    Player_1_st = Org_Ply_Hnd(Player_Hand)
    #Set the number of games
    num_of_games = 0
    #Deal a random player hand
    player_card_num = 13
    #Start quantity of game simulation
    Player_1_Book_Averages = []
    Conv_P1_Books = []
    All_iters = []
    Rnd_Crd_Count = 0
    while (bid_time_permit > (time.time()-start_time)):
        num_of_games += 1
        #Build the initial game state
        Player_1_int = list(Player_1_st)
        rnd_player_2 = Random_Cards(player_card_num,Player_1_int)
        Player_2_int = Org_Ply_Hnd(rnd_player_2)
        cards_taken = Player_1_int + Player_2_int
        rnd_player_3 = Random_Cards(player_card_num,cards_taken)
        Player_3_int = Org_Ply_Hnd(rnd_player_3)
        cards_taken = cards_taken + Player_3_int
        rnd_player_4 = Random_Cards(player_card_num,cards_taken)
        Player_4_int = Org_Ply_Hnd(rnd_player_4)
        #Initialize team bids
        Team_1_Bids = 6
        Team_2_Bids = 6
        #Initialize data structures for calculating convergence
        conv_crit = 0
        P1_Books = [3]
        P2_Books = [3]
        P3_Books = [3]
        P4_Books = [3]
        conv_num = 5
        max_iters = 100
        iters = 0
        #Start quantity of game simulation repetition
        while ((conv_crit == 0) and (iters < max_iters)):
            iters += 1
            Player_1 = list(Player_1_int)
            Player_2 = list(Player_2_int)
            Player_3 = list(Player_3_int)
            Player_4 = list(Player_4_int)
            #Player books
            All_Player_Books = [0]*4
            #Play a random MCS spades game
            [All_Player_Books,Rnd_Crd_Count] = MCS_Spades_Round(Team_1_Bids,Team_2_Bids,All_Player_Books,
                                                                Player_1,Player_2,Player_3,Player_4,Rnd_Crd_Count)
            #Calculate new team bids
            Team_1_Bids = All_Player_Books[0] + All_Player_Books[2]
            Team_2_Bids = All_Player_Books[1] + All_Player_Books[3]
            #Calculate convergence criterion
            P1_Books.append(All_Player_Books[0])
            P2_Books.append(All_Player_Books[1])
            P3_Books.append(All_Player_Books[2])
            P4_Books.append(All_Player_Books[3])
            if (len(P1_Books) < conv_num):
                conv_crit = 0
            elif ((P1_Books[-1] == (sum(P1_Books[-(conv_num+1):-1])/conv_num)) and 
                  (P2_Books[-1] == (sum(P2_Books[-(conv_num+1):-1])/conv_num)) and
                  (P3_Books[-1] == (sum(P3_Books[-(conv_num+1):-1])/conv_num)) and
                  (P4_Books[-1] == (sum(P4_Books[-(conv_num+1):-1])/conv_num))):
                conv_crit = 1
        All_iters.append(iters)
        #Append books for each repetition of the game played
        Conv_P1_Books.append(All_Player_Books[0])
    #Average the books for player 1
    Player_1_book_sum = 0
    for cp1b in range(len(Conv_P1_Books)):
        Player_1_book_sum += Conv_P1_Books[cp1b]
    Player_1_BK_avg = round((Player_1_book_sum/num_of_games),2)
    Player_1_Book_Averages.append(Player_1_BK_avg)
    return(Player_1_BK_avg,num_of_games,Conv_P1_Books,All_iters,Rnd_Crd_Count)

def Placing_A_Nil_Bid(Player_Hand,bid_time_permit):
    import time
    #Start time
    start_time = time.time()
    #Organize the player hand
    Player_1_st = Org_Ply_Hnd(Player_Hand)
    #Set the number of games
    num_of_games = 0
    #Deal a random player hand
    player_card_num = 13
    #Start quantity of game simulation
    Player_1_Book_Averages = []
    P1_Conv_Books = []
    All_iters = []
    nil_bid_flgs = [1,0,0,0]
    Rnd_Crd_Count_1 = 0
    Rnd_Crd_Count_2 = 0
    Rnd_Crd_Count_3 = 0
    while (bid_time_permit > (time.time()-start_time)):
        num_of_games += 1
        #Build the initial game state
        Player_1_int = list(Player_1_st)
        rnd_player_2 = Random_Cards(player_card_num,Player_1_int)
        Player_2_int = Org_Ply_Hnd(rnd_player_2)
        cards_taken = Player_1_int + Player_2_int
        rnd_player_3 = Random_Cards(player_card_num,cards_taken)
        Player_3_int = Org_Ply_Hnd(rnd_player_3)
        cards_taken = cards_taken + Player_3_int
        rnd_player_4 = Random_Cards(player_card_num,cards_taken)
        Player_4_int = Org_Ply_Hnd(rnd_player_4)
        #Initialize team bids
        Team_1_Bids = 6
        Team_2_Bids = 6
        #Initialize data structures for calculating convergence
        conv_crit = 0
        P1_Books = [3]
        P2_Books = [3]
        P3_Books = [3]
        P4_Books = [3]
        conv_num = 5
        max_iters = 100
        iters = 0
        #Start quantity of game simulation repetition
        while ((conv_crit == 0) and (iters < max_iters)):
            iters += 1
            Player_1 = list(Player_1_int)
            Player_2 = list(Player_2_int)
            Player_3 = list(Player_3_int)
            Player_4 = list(Player_4_int)
            #Player books
            All_Player_Books = [0]*4
            #Play a random MCS spades game
            [All_Player_Books,Rnd_Crd_Count_1,Rnd_Crd_Count_2,Rnd_Crd_Count_3] = MCS_Nil_Spades_Round(Team_1_Bids,Team_2_Bids,
                                                                                                      All_Player_Books,
                                                                                                      Player_1,Player_2,
                                                                                                      Player_3,Player_4,
                                                                                                      nil_bid_flgs,Rnd_Crd_Count_1,
                                                                                                      Rnd_Crd_Count_2,Rnd_Crd_Count_3)
            #Calculate new team bids
            Team_1_Bids = All_Player_Books[0] + All_Player_Books[2]
            Team_2_Bids = All_Player_Books[1] + All_Player_Books[3]
            #Calculate convergence criterion
            P1_Books.append(All_Player_Books[0])
            P2_Books.append(All_Player_Books[1])
            P3_Books.append(All_Player_Books[2])
            P4_Books.append(All_Player_Books[3])
            if (len(P1_Books) < conv_num):
                conv_crit = 0
            elif ((P1_Books[-1] == (sum(P1_Books[-(conv_num+1):-1])/conv_num)) and 
                  (P2_Books[-1] == (sum(P2_Books[-(conv_num+1):-1])/conv_num)) and
                  (P3_Books[-1] == (sum(P3_Books[-(conv_num+1):-1])/conv_num)) and
                  (P4_Books[-1] == (sum(P4_Books[-(conv_num+1):-1])/conv_num))):
                conv_crit = 1
        All_iters.append(iters)
        #Append books for each repetition of the game played
        P1_Conv_Books.append(All_Player_Books[0])
    #Average the books for player 1
    Player_1_book_sum = 0
    for cp1b in range(len(P1_Conv_Books)):
        Player_1_book_sum += P1_Conv_Books[cp1b]
    Player_1_BK_avg = round((Player_1_book_sum/num_of_games),2)
    Player_1_Book_Averages.append(Player_1_BK_avg)
    return(Player_1_BK_avg,num_of_games,P1_Conv_Books,All_iters,Rnd_Crd_Count_1,Rnd_Crd_Count_2,Rnd_Crd_Count_3)