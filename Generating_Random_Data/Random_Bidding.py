# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 07:14:26 2020

#Generates a bid based on random play

@author: Justin Paul
"""

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

def Org_Ply_Hnd(Player):
    #Obtain suit list of cards
    suit_list = Obtain_Suits(Player)
    #Progress through the player's cards and organize by suit
    new_Player = [[],[],[],[]]
    for pcs in range(len(Player)):
        if (Player[pcs] == 14):
            new_Player[3].append(14)
        elif (Player[pcs] == 40):
            new_Player[3].append(40)
        else:
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

def Rand_Play(Book,Player,First_Cut):
    if (Book == []):
        First_Card = 0
    else:
        First_Card = Book[0]
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
    return(Ply_Card,First_Cut)

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
    return(winning_card,winning_ply)

def New_Ply_Order(winning_ply):
    if (winning_ply == 1):
        ply_order = [1,2,3,4]
    elif (winning_ply == 2):
        ply_order = [2,3,4,1]
    elif (winning_ply == 3):
        ply_order = [3,4,2,1]
    elif (winning_ply == 4):
        ply_order = [4,1,2,3]
    return(ply_order)

def MCS_Spades_Round(Player_1_books,Player_1,Player_2,Player_3,Player_4):
    #Initialize the game
    First_Cut = 0
    Game_Books = 13
    ply_order = [1,2,3,4]
    while (Game_Books > 0):
        #Subtract a book for each book played
        Game_Books += -1
        #Initialize the book
        Book = []
        #Each Player plays a card
        First_Card = 0
        for plor in range(len(ply_order)):
            if (ply_order[plor] == 1):
                [ply_1_card,First_Cut] = Rand_Play(Book,Player_1,First_Cut)
                #Remove card played from Player 1
                for p1s in range(len(Player_1)):
                    if (ply_1_card in Player_1[p1s]):
                        Player_1[p1s].remove(ply_1_card)
                if (First_Card == 0):
                    First_Card = ply_1_card
                Book.append(ply_1_card)
            elif (ply_order[plor] == 2):
                [ply_2_card,First_Cut] = Rand_Play(Book,Player_2,First_Cut)
                #Remove card played from Player 2
                for p2s in range(len(Player_2)):
                    if (ply_2_card in Player_2[p2s]):
                        Player_2[p2s].remove(ply_2_card)
                if (First_Card == 0):
                    First_Card = ply_2_card
                Book.append(ply_2_card)
            elif (ply_order[plor] == 3):
                [ply_3_card,First_Cut] = Rand_Play(Book,Player_3,First_Cut)
                #Remove card played from Player 3
                for p3s in range(len(Player_3)):
                    if (ply_3_card in Player_3[p3s]):
                        Player_3[p3s].remove(ply_3_card)
                if (First_Card == 0):
                    First_Card = ply_3_card
                Book.append(ply_3_card)
            elif (ply_order[plor] == 4):
                [ply_4_card,First_Cut] = Rand_Play(Book,Player_4,First_Cut)
                #Remove card played from Player 4
                for p4s in range(len(Player_4)):
                    if (ply_4_card in Player_4[p4s]):
                        Player_4[p4s].remove(ply_4_card)
                if (First_Card == 0):
                    First_Card = ply_4_card
                Book.append(ply_4_card)
        #Evaluate the Book and decide who has the winning card
        [winning_card,winning_ply] = Book_Grading(Book,First_Card)
        #Use the index to get the actual player number
        winning_ply = ply_order[winning_ply]
        #Generate new player order based on who won the book
        ply_order = New_Ply_Order(winning_ply)
        #Track player books
        if (winning_ply == 1):
            Player_1_books += 1
    return(Player_1_books)

def Placing_A_Bid(hand):
    import time
    #Averaging across each spades game
    num_of_games = 300
    num_of_reps = 10
    player_card_num = 13
    #Start time
    start_time = time.time()
    #Initialize and organize the player hand
    Player_1_st = Org_Ply_Hnd(hand)
    Player_1_full_list = []
    for ngms in range(num_of_games):
        Player_1_sub_list = []
        for nrps in range(num_of_reps):
            Player_1_sub_list.append(list(Org_Ply_Hnd(hand)))
        Player_1_full_list.append(Player_1_sub_list)
    #Start quantity of game simulation
    Player_1_Book_Averages = []
    for ngms in range(num_of_games):
        Player_1_Books = []
        #Build the initial game state
        Player_1_sub_list = Player_1_full_list[ngms]
        rnd_player_2 = Random_Cards(player_card_num,Player_1_st)
        Player_2 = Org_Ply_Hnd(rnd_player_2)
        Player_2_full_list = []
        for nrps in range(num_of_reps):
            Player_2_full_list.append(list(Org_Ply_Hnd(rnd_player_2)))
        cards_taken = Player_1_st + Player_2
        rnd_player_3 = Random_Cards(player_card_num,cards_taken)
        Player_3 = Org_Ply_Hnd(rnd_player_3)
        Player_3_full_list = []
        for nrps in range(num_of_reps):
            Player_3_full_list.append(list(Org_Ply_Hnd(rnd_player_3)))
        cards_taken = cards_taken + Player_3
        rnd_player_4 = Random_Cards(player_card_num,cards_taken)
        Player_4 = Org_Ply_Hnd(rnd_player_4)
        Player_4_full_list = []
        for nrps in range(num_of_reps):
            Player_4_full_list.append(list(Org_Ply_Hnd(rnd_player_4)))
        #Start quantity of game simulation repetition
        for nrps in range(num_of_reps):
            Player_1 = Player_1_sub_list[nrps]
            Player_2 = Player_2_full_list[nrps]
            Player_3 = Player_3_full_list[nrps]
            Player_4 = Player_4_full_list[nrps]
            #Player books
            Player_1_books = 0
            #Play a random MCS spades game
            Player_1_books = MCS_Spades_Round(Player_1_books,
                                              Player_1,Player_2,
                                              Player_3,Player_4)
            #Append books for each repetition of the game played
            Player_1_Books.append(Player_1_books)
        #Average the books for player 1
        Player_1_book_sum = 0
        for pBKS in range(len(Player_1_Books)):
            Player_1_book_sum += Player_1_Books[pBKS]
        Player_1_BK_avg = round(Player_1_book_sum/num_of_reps,2)
        Player_1_Book_Averages.append(Player_1_BK_avg)
    #Average the books for player 1
    Player_1_book_avg_sum = 0
    for pBKS in range(len(Player_1_Book_Averages)):
        Player_1_book_avg_sum += Player_1_Book_Averages[pBKS]
    Player_1_Tot_BK_avg = round(Player_1_book_avg_sum/num_of_games,2)
    end_time = time.time()
    delta_time = round(end_time-start_time,2)
    return(Player_1_Tot_BK_avg,delta_time)