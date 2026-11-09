# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 03:42:45 2020

Expert Player: Carl

This system is an expert player for the poker game Spades.

The logic this system is supposed to accomplish is as follows:
    
    Playing the first card:
        A descending sorted list of cards to play by priority:
            -Lower Spades (10>) have highest priority (8 cards)
            -Higher Spades (10<) have second highest priority (7 cards)
            -Aces (non-spade) and cards of consecutive descending value have
            third highest priority (3 cards)
            -Low value (non-spade) (10>) cards have fourth highest priority
            (25 cards)
            -High value (non-spade) (10<) cards have fifth highest priority
            (9 cards)
    
    Playing into the book:
        If your team still needs books and you are not currently winning the
        book, win the book by playing the lowest value card that will win the
        book. If your team doesn't need books, you are currently winning the
        book or you can't win the book, play the lowest value card
    
Carl accepts the following inputs:
    -The current hand
    -The current book
    -Book cards corresponding to teammate and opposing players
    -Flag tracking first spade played
    -Team books
    -Team bids

@author: justin paul
"""

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

def Hand_Priority(hand):
    #Establish categories
    Cat_1 = [9,8,7,6,5,4,3,2]
    Cat_2 = [10,11,12,13,1,14,40]
    Cat_3 = [26,39,52]
    Cat_4 = [22,35,48,21,34,47,20,33,46,19,32,45,
             18,31,44,17,30,43,16,29,42,15,28,41]
    Cat_5 = [23,36,49,24,37,50,25,38,51]
    #Build the categorical lists into a 1D list
    Mast_Cat_List = [Cat_1,Cat_2,Cat_3,Cat_4,Cat_5]
    Mast_Cat_1D = []
    for mcl in range(len(Mast_Cat_List)):
        sub_list = Mast_Cat_List[mcl]
        for sl in range(len(sub_list)):
            Mast_Cat_1D.append(sub_list[sl])
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

def Book_Grading(book,First_Card):
    #Get the suit of the first card
    FC_suit = Obtain_Suits([First_Card])
    Hierarchy = []
    #Build the beginning of the list hierarchy
    if (FC_suit[0] == 'c'):
        for lc in range(1,14):
            Hierarchy.append(lc+(13*2))
    elif (FC_suit[0] == 'd'):
        for lc in range(2,14):
            Hierarchy.append(lc+(13*1))
    elif (FC_suit[0] == 'h'):
        for lc in range(2,14):
            Hierarchy.append(lc+(13*3))
    elif (FC_suit[0] == 's'):
        Hierarchy = []
    #Append the spades Hierarchy
    for lc in range(2,14):
        Hierarchy.append(lc)
    #Append the two of spades
    Hierarchy.append(1)
    #Append the two of diamonds as the little
    Hierarchy.append(14)
    #Append the two of hearts as the big
    Hierarchy.append(40)
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

def Lowest_Card(Hierarchy,hand):
    #Initialize the lowest card
    lowest_card = 0
    #Obtain the lowest value viable card in the Hierarchy
    for H in range(len(Hierarchy)):
        if (Hierarchy[H] in hand):
            lowest_card = Hierarchy[H]
            return(lowest_card)
    if (lowest_card == 0):
        #Capture cards off suit
        throwing_off = []
        for h in range(len(hand)):
            if (hand[h] not in Hierarchy):
                throwing_off.append(hand[h])
        #Obtain values for off suit cards
        value_list = Obtain_Vals(throwing_off)
        #Obtain index of lowest value off suit card
        low_val_ind = value_list.index(min(value_list))
        #Obtain the lowest card
        lowest_card = throwing_off[low_val_ind]
    return(lowest_card)
    
def Cards_That_Win(winning_card,Hierarchy,hand,sp_flg):
    #Initialize selected card
    selected_card = 0
    #Grab the index of the winning card in the Hierarchy
    win_index = Hierarchy.index(winning_card)
    #Determine what cards can beat the winning card
    cards_that_win = []
    for H in range(len(Hierarchy)):
        if (H > win_index):
            cards_that_win.append(Hierarchy[H])
    Spades_Cards = [40,14,1,13,12,11,10,9,8,7,6,5,4,3,2]
    #Check if spades flag is active
    if (sp_flg == 0):
        #Check if hand has cards of first suit
        first_suit = Obtain_Suits([Hierarchy[0]])
        suit_list = Obtain_Suits(hand)
        if (first_suit[0] in suit_list):
            #Remove spades from cards that win
            for SC in range(len(Spades_Cards)):
                if (Spades_Cards[SC] in cards_that_win):
                    cards_that_win.remove(Spades_Cards[SC])
    if (cards_that_win == []):
        #Return 0 if no cards can win
        return(selected_card)
    for ctw in range(len(cards_that_win)):
        if (cards_that_win[ctw] in hand):
            #Return the minimum card to win
            selected_card = cards_that_win[ctw]
            return(selected_card)

def Cards_That_Lose(winning_card,Hierarchy,hand):
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
        if (cards_that_lose[ctl] in hand):
            selected_card = cards_that_lose[ctl]
    return(selected_card)

def Highest_Card(Hierarchy,hand):
    #Initialize the lowest card
    highest_card = 0
    #Obtain the lowest value viable card in the Hierarchy
    for H in range(len(Hierarchy)):
        if (Hierarchy[H] in hand):
            highest_card = Hierarchy[H]
    if (highest_card == 0):
        #Capture cards off suit
        throwing_off = []
        for h in range(len(hand)):
            if (hand[h] not in Hierarchy):
                throwing_off.append(hand[h])
        #Obtain values for off suit cards
        value_list = Obtain_Vals(throwing_off)
        #Obtain index of lowest value off suit card
        high_val_ind = value_list.index(max(value_list))
        #Obtain the lowest card
        highest_card = throwing_off[high_val_ind]
    return(highest_card)
    
def Carl(hand,Book,players,sp_flg,Team_Books,Team_Bids):
    Spades_Cards = [40,14,1,13,12,11,10,9,8,7,6,5,4,3,2]
    #Check position in book
    if (Book == []):
        #Organize the hand by priority
        Hand_Sorted = Hand_Priority(hand)
        #Play the first 
        if (sp_flg == 1):
            Card_to_play = Hand_Sorted[0]
        else:
            for hs in range(len(Hand_Sorted)):
                if (Hand_Sorted[hs] not in Spades_Cards):
                    Card_to_play = Hand_Sorted[hs]
                    return(Card_to_play)
    else:
        #Determine which card in the book is winning
        [winning_card,winning_ply,Hierarchy] = Book_Grading(Book)
        #Determine the corresponding player
        winning_ply = players[winning_ply]
        #Determine if books need to be won
        if (Team_Books < Team_Bids):
            if (winning_ply == 'T'):
                #Play the lowest card since the teammate is winning the book
                lowest_card = Lowest_Card(Hierarchy,hand)
                Card_to_play = lowest_card
            elif (winning_ply == 'O'):
                #Determine if the book can be won
                selected_card = Cards_That_Win(winning_card,Hierarchy,hand,sp_flg)
                if (selected_card == 0):
                    #The book cannot be won so play the lowest card
                    lowest_card = Lowest_Card(Hierarchy,hand)
                    Card_to_play = lowest_card
                else:
                    #The book can be won so play the selected card
                    Card_to_play = selected_card
        else:
            #Books do not need to be won so lose as efficiently as possible
            selected_card = Cards_That_Win(winning_card,Hierarchy,hand)
            if (selected_card == 0):
                #The book cannot be lost so play the highest card
                highest_card = Highest_Card(Hierarchy,hand)
                Card_to_play = highest_card
            else:
                #The book can be lost so play the selected card
                Card_to_play = selected_card
    return(Card_to_play)