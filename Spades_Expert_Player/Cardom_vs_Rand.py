# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 15:40:22 2020

This script is a spades game of

Team 1: carl 1 and carl 2 
against 
Team 2: carl 3 and carl 4

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

def Hand_Translator(hand):
    #Initialize card lists
    disp_hand = []
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
        value = str(value)
        if (hand[i] == 14):
            card = 'Little'
        elif (hand[i] == 40):
            card = 'Big'
        else:
            if (suit == 1):
                suit = "d"
            elif (suit == 2):
                suit = "c"
            elif (suit == 3):
                suit = "h"
            if (value == "11"):
                value = "J"
            elif (value == "12"):
                value = "Q"
            elif (value == "13"):
                value = "K"
            elif (value == "14"):
                value = "A"
            #Create the card
            card = value + suit
        #Append the card
        disp_hand.append(card)
    #Give disp_hand back to main driver
    return(disp_hand)

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
        #Special consideration given to the Little
        if (hand[i] == 14):
            suit = "s"
        #Special consideration given to the Big
        elif (hand[i] == 40):
            suit = "s"
        #Append suits to suit list
        suit_list.append(suit)
    return(suit_list)

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

def Org_Ply_Rnd_Hnd(Player):
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

def Org_Ply_Hnd(Player):
    #Build the ultimate organization list
    ult_org_list = []
    for c in range(27,(39+1)):
        ult_org_list.append(c)
    for h in range(41,(52+1)):
        ult_org_list.append(h)
    for d in range(15,(26+1)):
        ult_org_list.append(d)
    for s in range(2,(13+1)):
        ult_org_list.append(s)
    #Append the 2s, Little, Big
    ult_org_list.append(1)
    ult_org_list.append(14)
    ult_org_list.append(40)
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

def Spades_Against_Carl():
    #Import libraries
    import Carl_Bidding_With_MCS
    import Random_Bidding
    import math
    #Start the game
    Team_1_Points = 0
    Team_1_Bags = 0
    Team_2_Points = 0
    Team_2_Bags = 0
    #Play the game
    game_set = 500
    bag_limit = 10
    Total_Bid_Time = 0
    while ((Team_1_Points < game_set) and (Team_2_Points < game_set)):
        #Shuffle the deck
        rnd_deck = Random_Cards(52,[])
        #Initialize the players
        Player_1 = rnd_deck[0:13]
        Player_2 = rnd_deck[13:26]
        Player_3 = rnd_deck[26:39]
        Player_4 = rnd_deck[39:52]
        #Place and calculate the bids
#        print('Player 1:')
#        print(Hand_Translator(Org_Ply_Hnd(Player_1)))
        [Player_1_Bid,bid_time_1] = Random_Bidding.Placing_A_Bid(Player_1)
#        print('Player 1 Bid:')
#        print(Player_1_Bid)
#        print('Player 3:')
#        print(Hand_Translator(Org_Ply_Hnd(Player_3)))
        [Player_3_Bid,bid_time_3] = Carl_Bidding_With_MCS.Placing_A_Bid(Player_3)
#        print('Player 3 Bid:')
#        print(Player_3_Bid)
        Team_1_Bids = int(math.floor(Player_1_Bid) + math.floor(Player_3_Bid))
#        print('Team 1 Bid:')
#        print(Team_1_Bids)
#        print()
        #Place and calculate the bids
#        print('Player 2:')
#        print(Hand_Translator(Org_Ply_Hnd(Player_2)))
        [Player_2_Bid,bid_time_2] = Random_Bidding.Placing_A_Bid(Player_2)
#        print('Player 2 Bid:')
#        print(Player_2_Bid)
#        print('Player 4:')
#        print(Hand_Translator(Org_Ply_Hnd(Player_4)))
        [Player_4_Bid,bid_time_4] = Random_Bidding.Placing_A_Bid(Player_4)
#        print('Player 4 Bid:')
#        print(Player_4_Bid)
        Team_2_Bids = int(math.floor(Player_2_Bid) + math.floor(Player_4_Bid))
#        print('Team 2 Bid:')
#        print(Team_2_Bids)
#        print()
        sub_total_bid_time = round((bid_time_1+bid_time_2+bid_time_3+bid_time_4)/60,3)
        Total_Bid_Time += sub_total_bid_time
        #Initialize the round
        First_Cut = 0
        All_Player_Books = [0]*4
        Team_1_Books = []
        Team_2_Books = []
        Round_Books = 13
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
                    [ply_1_card,First_Cut] = Random_Bidding.Rand_Play(Book,Org_Ply_Rnd_Hnd(Player_1),First_Cut)
                    #Remove card played from Player 1
                    Player_1.remove(ply_1_card)
                    if (First_Card == 0):
                        First_Card = ply_1_card
                    Book.append(ply_1_card)
                elif (ply_order[plor] == 2):
                    [ply_2_card,First_Cut] = Random_Bidding.Rand_Play(Book,Org_Ply_Rnd_Hnd(Player_2),First_Cut)
                    #Remove card played from Player 2
                    Player_2.remove(ply_2_card)
                    if (First_Card == 0):
                        First_Card = ply_2_card
                    Book.append(ply_2_card)
                elif (ply_order[plor] == 3):
                    [ply_3_card,First_Cut] = Carl_Bidding_With_MCS.Carl(Book,Player_3,First_Cut,
                                                                        Team_1_players,len(Team_1_Books),
                                                                        Team_1_Bids)
                    #Remove card played from Player 3
                    Player_3.remove(ply_3_card)
                    if (First_Card == 0):
                        First_Card = ply_3_card
                    Book.append(ply_3_card)
                elif (ply_order[plor] == 4):
                    [ply_4_card,First_Cut] = Random_Bidding.Rand_Play(Book,Org_Ply_Rnd_Hnd(Player_4),First_Cut)
                    #Remove card played from Player 4
                    Player_4.remove(ply_4_card)
                    if (First_Card == 0):
                        First_Card = ply_4_card
                    Book.append(ply_4_card)
            #Evaluate the Book and decide who has the winning card
            [winning_card,winning_ply,Hierarchy] = Carl_Bidding_With_MCS.Book_Grading(Book,First_Card)
            #Use the index to get the actual player number
            winning_ply = ply_order[winning_ply]
            #Generate new player order based on who won the book
            [ply_order,Team_1_players,Team_2_players] = Carl_Bidding_With_MCS.New_Ply_Order(winning_ply,
                                                                                            Team_1_players,
                                                                                            Team_2_players)            
            '''
            #Print the round
            disp_Book = Hand_Translator(Book)
            print(disp_Book)
            disp_Card = Hand_Translator([winning_card])
            print('P',str(winning_ply),':',disp_Card[0])
            '''
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
#        print()
#        print(Hand_Translator(Team_1_Books))
#        print(Hand_Translator(Team_2_Books))
#        print()
        #Score the round for Team 1
        T1_Change = 0
        if (Team_1_Bids <= len(Team_1_Books)):
            T1_Change += (10*Team_1_Bids)
            Team_1_Bags += (len(Team_1_Books) - Team_1_Bids)
        elif (Team_1_Bids > len(Team_1_Books)):
            T1_Change += -(10*Team_1_Bids)
        if (Team_1_Bags >= 10):
            Team_1_Bags += -10
            T1_Change += -100
        Team_1_Points += T1_Change
        print()
        print('TEAM CARDOM SCORE:',str(Team_1_Points-T1_Change),'+',str(T1_Change),'=',str(Team_1_Points))
        print('TEAM CARDOM BAGS:',str(Team_1_Bags))
        #Score the round for Team 1
        T2_Change = 0
        if (Team_2_Bids <= len(Team_2_Books)):
            T2_Change += (10*Team_2_Bids)
            Team_2_Bags += (len(Team_2_Books) - Team_2_Bids)
        elif (Team_2_Bids > len(Team_2_Books)):
            T2_Change += -(10*Team_2_Bids)
        if (Team_2_Bags >= bag_limit):
            Team_2_Bags += -bag_limit
            T2_Change += -10*bag_limit
        Team_2_Points += T2_Change
        print('TEAM RAND SCORE:',str(Team_2_Points-T2_Change),'+',str(T2_Change),'=',str(Team_2_Points))
        print('TEAM RAND BAGS:',str(Team_2_Bags))
        print()
    #Declare the winner
    if (Team_1_Points > Team_2_Points):
        winner = 'TEAM CARDOM'
    elif (Team_2_Points > Team_1_Points):
        winner = 'TEAM RAND'
    else:
        winner = 'TIE'
    print(winner)
    return(winner,Total_Bid_Time)

def Win_Rate():
    #Run the full game against two carl teams to get the win rate
    num_of_games = 100
    Team_1_Wins = 0
    Team_2_Wins = 0
    Ties = 0
    for nog in range(num_of_games):
        [winner,Total_Bid_Time] = Spades_Against_Carl()
        if (winner == 'TEAM CARDOM'):
            Team_1_Wins += 1
        elif (winner == 'TEAM RAND'):
            Team_2_Wins += 1
        else:
            Ties += 1
        print('GAME:',str(nog+1))
        print('Total_Bid_Time:',str(Total_Bid_Time),'Minutes')
    #Calculate win rates
    Team_1_Win_Rate = round((Team_1_Wins/num_of_games)*100,4)
    Team_2_Win_Rate = round((Team_2_Wins/num_of_games)*100,4)
    Tie_Rate = round((Ties/num_of_games)*100,4)
    #Print the win rates
    print('Win rate for CARDOM:',str(Team_1_Win_Rate),'%')
    print('Win rate for RAND:',str(Team_2_Win_Rate),'%')
    print('Tie rate:',str(Tie_Rate),'%')
    return(num_of_games)

Win_Rate()