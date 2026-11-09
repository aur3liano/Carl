# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 15:40:22 2020

This script generates a console interface 

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
    #Initialize card list
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
                suit = int((int(hand[i]) - (value - 1))/13)
            else:
                #Modulo required for all suits above the first
                value = (int(hand[i]) % 13) + 1
                #Identify the suit
                suit = int((int(hand[i]) - (value - 1))/13)
        #Convert to conventional card identification
        value = str(value)
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

def Reverse_Hand_Translator(hand):
    #Initialize value and suit lists
    numerical_hand = []
    #Separate value and suit
    for h in range(len(hand)):
        if(len(hand[h]) > 2):
            value = int(hand[h][0:2])
            suit = hand[h][2]
        else:
            if (hand[h][0] == 'J'):
                value = 11
            elif (hand[h][0] == 'Q'):
                value = 12
            elif (hand[h][0] == 'K'):
                value = 13
            elif (hand[h][0] == 'A'):
                value = 14
            else:
                value = int(hand[h][0])
            suit = hand[h][1]
        if (suit == 's'):
            suit = 0
        elif (suit == 'd'):
            suit = 1
        elif (suit == 'c'):
            suit = 2
        elif (suit == 'h'):
            suit = 3
        numerical_value = (value-1) + (suit*13)
        numerical_hand.append(numerical_value)
    return(numerical_hand)

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

def Proc_Master_Game_File(master_file_nm):
    import os
    import datetime as dt
    
    #Detect if there is a master game file
    if (os.path.isfile(master_file_nm) == True):
        #Read the master game file
        master_file_obj = open(master_file_nm,'r')
        raw_data = master_file_obj.readlines()
        master_file_obj.close()
        #Process the data
        proc_data = []
        for rd in range(len(raw_data)):
            row_info = raw_data[rd].strip('\n').split('\t')
            proc_data.append(row_info)
        
        #Team 1 name information
        ply1_nm = proc_data[1][1]
        ply3_nm = proc_data[1][2]
        #Team 2 name information
        ply2_nm = proc_data[2][1]
        ply4_nm = proc_data[2][2]
        #Game Limit information
        game_set = int(proc_data[3][1])
        bag_limit = int(proc_data[4][1])
        #Bonus information
        wheel_bonus = int(proc_data[5][1])
        nil_bonus = int(proc_data[6][1])
        #Team 1 point information
        Team_1_Points = int(proc_data[7][1])
        Team_1_Bags = int(proc_data[7][3])
        #Team 1 bonus information
        Team_1_Blinds = int(proc_data[7][5])
        Team_1_Wheels = int(proc_data[7][7])
        Team_1_Nils = int(proc_data[7][9])
        #Team 2 point information
        Team_2_Points = int(proc_data[8][1])
        Team_2_Bags = int(proc_data[8][3])
        #Team 2 bonus information
        Team_2_Blinds = int(proc_data[8][5])
        Team_2_Wheels = int(proc_data[8][7])
        Team_2_Nils = int(proc_data[8][9])
        #Round
        current_round = int(proc_data[9][1])
        #Dealer
        dealer = proc_data[10][1]
        #Winner
        winner_nm = proc_data[11][1]
        
        ply_nms = [ply1_nm,ply2_nm,ply3_nm,ply4_nm]
        game_params = [game_set,bag_limit]
        game_bonuses = [wheel_bonus,nil_bonus]
        Team_1_status = [Team_1_Points,Team_1_Bags,Team_1_Blinds,Team_1_Wheels,Team_1_Nils]
        Team_2_status = [Team_2_Points,Team_2_Bags,Team_2_Blinds,Team_2_Wheels,Team_2_Nils]
        
        if (winner_nm != 'Undecided'):
            winner_prnt_stmt = 'Winner of the game:\t' + winner_nm + '\n'
            print(winner_prnt_stmt)
            return(ply_nms,game_params,game_bonuses,Team_1_status,Team_2_status,current_round,dealer)
        
    else:
        #Pull the present day
        present_day = dt.date.today()
        present_day_string = dt.datetime.strftime(present_day,'%Y-%m-%d')
        present_day_prnt_stmt = 'Game start date:\t' + present_day_string + '\n'   
        prnt_stmt_for_write = str(present_day_prnt_stmt)
        
        #Read in player names
        ply1_nm = input('Player 1 name (playing with player 3): ')
        ply2_nm = input('Player 2 name (playing with Carl): ')
        ply3_nm = input('Player 3 name (playing with player 3): ')
        ply4_nm = 'Carl'
        #Establish teams
        team_1_prnt_stmt = 'Team 1:\t' + ply1_nm + '\t' + ply3_nm + '\n'
        team_2_prnt_stmt = 'Team 2:\t' + ply2_nm + '\t' + ply4_nm + '\n'
        teams_prnt_stmt = team_1_prnt_stmt + team_2_prnt_stmt
        prnt_stmt_for_write = prnt_stmt_for_write + teams_prnt_stmt
        
        #Set the game parameters
        game_set = 500
        bag_limit = 10
        game_score_prnt_stmt = 'Game score limit:\t' + str(game_set) + '\n'
        game_bag_prnt_stmt = 'Game bag limit:\t' + str(bag_limit) + '\n'
        prnt_stmt_for_write = prnt_stmt_for_write + game_score_prnt_stmt
        prnt_stmt_for_write = prnt_stmt_for_write + game_bag_prnt_stmt
        
        #Wheels bonus
        wheel_bonus = input('Wheels bonus (0-200): ')
        #Make sure wheel bonus value is between 0 and 200
        while (float(wheel_bonus) <= 0) and (float(wheel_bonus) >= 200):
            wheel_bonus = input('Please enter a valid Wheels bonus (0-200): ')
        wheel_bonus_prnt_stmt = 'Wheel bonus:\t' + wheel_bonus + '\n'
        prnt_stmt_for_write = prnt_stmt_for_write + wheel_bonus_prnt_stmt
        
        #Nil bonus
        nil_bonus = input('Nil bonus (0-200): ')
        #Make sure nil bonus value is between 0 and 200
        while (float(nil_bonus) <= 0) and (float(nil_bonus) >= 200):
            nil_bonus = input('Please enter a valid Wheels bonus (0-200): ')
        nil_bonus_prnt_stmt = 'Nil bonus:\t' + nil_bonus + '\n'
        prnt_stmt_for_write = prnt_stmt_for_write + nil_bonus_prnt_stmt
    
        #Initialize the game
        Team_1_Points = 0
        Team_1_Bags = 0
        Team_1_Blinds = 0
        Team_1_Wheels = 0
        Team_1_Nils = 0
        Team_2_Points = 0
        Team_2_Bags = 0
        Team_2_Blinds = 0
        Team_2_Wheels = 0
        Team_2_Nils = 0
        team_1_status = 'Team 1 has:\t' + str(Team_1_Points) + '\tPoints and\t' + str(Team_1_Bags) +'\tBags and\t'
        team_1_bonus_stat = str(Team_1_Blinds) + '\tBlinds and\t' + str(Team_1_Wheels) + '\tWheels and\t' + str(Team_1_Nils) + '\tNils\n'
        team_2_status = 'Team 2 has:\t' + str(Team_2_Points) + '\tPoints and\t' + str(Team_2_Bags) +'\tBags and\t'
        team_2_bonus_stat = str(Team_2_Blinds) + '\tBlinds and\t' + str(Team_2_Wheels) + '\tWheels and\t' + str(Team_2_Nils) + '\tNils\n'
        prnt_stmt_for_write = prnt_stmt_for_write + team_1_status + team_1_bonus_stat
        prnt_stmt_for_write = prnt_stmt_for_write + team_2_status + team_2_bonus_stat
        Team_1_status = [Team_1_Points,Team_1_Bags,Team_1_Blinds,Team_1_Wheels,Team_1_Nils]
        Team_2_status = [Team_2_Points,Team_2_Bags,Team_2_Blinds,Team_2_Wheels,Team_2_Nils]
        
        current_round = 0
        round_prnt_stmt = 'Current round:\t' + str(current_round) + '\n'
        prnt_stmt_for_write = prnt_stmt_for_write + round_prnt_stmt
        
        dealer = str(ply1_nm)
        dealer_prnt_stmt = 'Current dealer:\t' + dealer + '\n'
        prnt_stmt_for_write = prnt_stmt_for_write + dealer_prnt_stmt
        
        winner_nm = 'Undecided'
        winner_prnt_stmt = 'Winner of the game:\t' + winner_nm + '\n'
        prnt_stmt_for_write = prnt_stmt_for_write + winner_prnt_stmt
        
        ply_nms = [ply1_nm,ply2_nm,ply3_nm,ply4_nm]
        game_params = [game_set,bag_limit]
        game_bonuses = [wheel_bonus,nil_bonus]
        team_1_status = [Team_1_Points,Team_1_Bags]
        team_2_status = [Team_2_Points,Team_2_Bags]
        
        #Write the master game file
        master_file_obj = open(master_file_nm,'w')
        master_file_obj.write(prnt_stmt_for_write)
        master_file_obj.close()
    
    return(ply_nms,game_params,game_bonuses,Team_1_status,Team_2_status,current_round,dealer)

def chk_repeated_cards(hand):
    max_count = 1
    for h in range(len(hand)):
        curr_count = hand.count(hand[h])
        max_count = max(curr_count,max_count)
    return(max_count)

def chk_card_validity(hand):
    card_validity_flg = 1
    hearts = ['2h','3h','4h','5h','6h','7h','8h','9h','10h','Jh','Qh','Kh','Ah']
    diamonds = ['2d','3d','4d','5d','6d','7d','8d','9d','10d','Jd','Qd','Kd','Ad']
    clubs = ['2c','3c','4c','5c','6c','7c','8c','9c','10c','Jc','Qc','Kc','Ac']
    spades = ['2s','3s','4s','5s','6s','7s','8s','9s','10s','Js','Qs','Ks','As']
    full_deck = hearts + diamonds + clubs + spades
    for h in range(len(hand)):
        if (hand[h] not in full_deck):
            card_validity_flg = 0
    return(card_validity_flg)

def enter_ply_bid(ply_nm):
    Player_Bid = 'Not Entered'
    nil_flg = 0
    while (Player_Bid == 'Not Entered'):
        try:
            input_prnt_stmt = 'Enter the bid for player ' + ply_nm + ': '
            Player_Bid = int(input(input_prnt_stmt))
            #Check if player is bidding nil
            if (Player_Bid == 0):
                nil_flg = 1
        except:
            Player_Bid = 'Not Entered'
    return(Player_Bid,nil_flg)

def enter_team_bid(team_num,ply1_nm,ply2_nm,resn_flg):
    Team_Bid = 'Not Entered'
    blind_flg = 0
    wheel_flg = 0
    while (Team_Bid == 'Not Entered'):
        try:
            input_prnt_stmt = 'Enter the ' + resn_flg + ' total bid for team ' + str(team_num) + ' (' + ply1_nm + ' and ' + ply2_nm + '): '
            Team_Bid = input(input_prnt_stmt)
            #Check if team is bidding wheels or blind
            if (Team_Bid == 'Wheels'):
                wheel_flg = 1
            elif (Team_Bid == 'Blind'):
                blind_flg = 1
                input_prnt_stmt = 'Enter the blind bid for team ' + str(team_num) + ' (' + ply1_nm + ' and ' + ply2_nm + '): '
                Team_Bid = input(input_prnt_stmt)
            else:
                Team_Bid = int(Team_Bid)
        except:
            Team_Bid = 'Not Entered'
    return(Team_Bid,wheel_flg,blind_flg)

def Acquire_Player_Bids(ply1_nm,ply2_nm,ply3_nm,ply4_nm,dealer,num_carl_hand_list):
    import Carl_Bidding_With_MCS_Std
    #Team 1 bids first
    if ((dealer == ply1_nm) or (dealer == ply3_nm)):
        bid_time_permit = 30
        [Carl_Bid,num_of_games,P4_Conv_Books,All_iters,Rnd_Crd_Count] = Carl_Bidding_With_MCS_Std.Placing_A_Bid(num_carl_hand_list,bid_time_permit)
        #Calculate the average number of rounds
        total_iters = 0
        for ai in range(len(All_iters)):
            total_iters += All_iters[ai]
        avg_iters = round((total_iters/len(All_iters)),2)
        #Calculate the frequency for each book
        Carl_Bid_dict = {}
        for pcb in range(len(P4_Conv_Books)):
            if (P4_Conv_Books[pcb] in Carl_Bid_dict):
                Carl_Bid_dict[P4_Conv_Books[pcb]] += 1
            else:
                Carl_Bid_dict[P4_Conv_Books[pcb]] = 1
        sort_keys_list = sorted(Carl_Bid_dict)
        #Print the frequencies
        print()
        for key in sort_keys_list:
            freq = round((Carl_Bid_dict[key]/num_of_games)*100,2)
            prnt_stmt = 'Chance of winning ' + str(key) + ' books: ' + str(freq) + '%'
            print(prnt_stmt)
        print()
        #Announce Carl's bid
        carls_bid_prnt_stmt_1 = 'Carl is estimating a bid of ' + str(Carl_Bid) + ' after analyzing '
        carls_bid_prnt_stmt_2 = str(total_iters) + ' simulations with an average of ' + str(avg_iters)
        carls_bid_prnt_stmt_3 = ' simulations per converged round for a total of ' + str(num_of_games) + ' games'
        carls_bid_prnt_stmt = carls_bid_prnt_stmt_1 + carls_bid_prnt_stmt_2 + carls_bid_prnt_stmt_3
        print(carls_bid_prnt_stmt)
        #Check if Carl wants to consider a nil bid
        nil_inquiry_ans = input('Does Carl want to consider a Nil bid? (yes,no) ')
        while (((nil_inquiry_ans != 'yes') or (nil_inquiry_ans != 'no')) == False):
            #Check if Carl wants to consider a nil bid
            nil_inquiry_ans = input('Does Carl want to consider a Nil bid? (yes,no) ')
        if (nil_inquiry_ans == 'yes'):
            [Carl_Bid,num_of_games,P4_Conv_Books,All_iters,Rnd_Crd_Count_1,Rnd_Crd_Count_2,Rnd_Crd_Count_3] = Carl_Bidding_With_MCS_Std.Placing_A_Nil_Bid(num_carl_hand_list,bid_time_permit)
            #Calculate the average number of rounds
            total_iters = 0
            for ai in range(len(All_iters)):
                total_iters += All_iters[ai]
            avg_iters = round((total_iters/len(All_iters)),2)
            #Calculate the frequency for each book
            Carl_Bid_dict = {}
            for pcb in range(len(P4_Conv_Books)):
                if (P4_Conv_Books[pcb] in Carl_Bid_dict):
                    Carl_Bid_dict[P4_Conv_Books[pcb]] += 1
                else:
                    Carl_Bid_dict[P4_Conv_Books[pcb]] = 1
            sort_keys_list = sorted(Carl_Bid_dict)
            #Print the frequencies
            print()
            for key in sort_keys_list:
                freq = round((Carl_Bid_dict[key]/num_of_games)*100,2)
                prnt_stmt = 'Chance of winning ' + str(key) + ' books: ' + str(freq) + '%'
                print(prnt_stmt)
            print()
            #Announce Carl's bid
            carls_bid_prnt_stmt_1 = 'Carl is estimating a bid of ' + str(Carl_Bid) + ' after analyzing '
            carls_bid_prnt_stmt_2 = str(total_iters) + ' simulations with an average of ' + str(avg_iters)
            carls_bid_prnt_stmt_3 = ' simulations per converged round for a total of ' + str(num_of_games) + ' games'
            carls_bid_prnt_stmt = carls_bid_prnt_stmt_1 + carls_bid_prnt_stmt_2 + carls_bid_prnt_stmt_3
            print(carls_bid_prnt_stmt)
        
        [Player_4_Bid,nil_4_flg] = enter_ply_bid(ply4_nm)
        [Player_2_Bid,nil_2_flg] = enter_ply_bid(ply2_nm)
        [Player_1_Bid,nil_1_flg] = enter_ply_bid(ply1_nm)
        [Player_3_Bid,nil_3_flg] = enter_ply_bid(ply3_nm)

        #Confirm bid information
        resn_flg = ''
        Team_1_Bids = enter_team_bid(1,ply1_nm,ply3_nm,resn_flg)
        resn_flg = 'valid'
        while ((Player_1_Bid + Player_3_Bid) != Team_1_Bids):    
            [Player_1_Bid,nil_1_flg] = enter_ply_bid(ply1_nm)
            [Player_3_Bid,nil_3_flg] = enter_ply_bid(ply3_nm)
            [Team_1_Bids,wheel_1_flg,blind_1_flg] = enter_team_bid(1,ply1_nm,ply3_nm,resn_flg)
        resn_flg = ''
        Team_2_Bids = enter_team_bid(2,ply2_nm,ply4_nm,resn_flg)
        resn_flg = 'bump'
        while ((Player_2_Bid + Player_4_Bid) != Team_2_Bids):    
            [Player_2_Bid,nil_2_flg] = enter_ply_bid(ply2_nm)
            [Player_4_Bid,nil_4_flg] = enter_ply_bid(ply4_nm)
            [Team_2_Bids,wheel_2_flg,blind_2_flg] = enter_team_bid(2,ply2_nm,ply4_nm,resn_flg)
    else:
        [Player_1_Bid,nil_1_flg] = enter_ply_bid(ply1_nm)
        [Player_3_Bid,nil_3_flg] = enter_ply_bid(ply3_nm)
        bid_time_permit = 30
        [Carl_Bid,num_of_games,P4_Conv_Books,All_iters,Rnd_Crd_Count] = Carl_Bidding_With_MCS_Std.Placing_A_Bid(num_carl_hand_list,bid_time_permit)
        #Calculate the average number of rounds
        total_iters = 0
        for ai in range(len(All_iters)):
            total_iters += All_iters[ai]
        avg_iters = round((total_iters/len(All_iters)),2)
        #Calculate the frequency for each book
        Carl_Bid_dict = {}
        for pcb in range(len(P4_Conv_Books)):
            if (P4_Conv_Books[pcb] in Carl_Bid_dict):
                Carl_Bid_dict[P4_Conv_Books[pcb]] += 1
            else:
                Carl_Bid_dict[P4_Conv_Books[pcb]] = 1
        sort_keys_list = sorted(Carl_Bid_dict)
        #Print the frequencies
        print()
        for key in sort_keys_list:
            freq = round((Carl_Bid_dict[key]/num_of_games)*100,2)
            prnt_stmt = 'Chance of winning ' + str(key) + ' books: ' + str(freq) + '%'
            print(prnt_stmt)
        print()
        #Announce Carl's bid
        carls_bid_prnt_stmt_1 = 'Carl is estimating a bid of ' + str(Carl_Bid) + ' after analyzing '
        carls_bid_prnt_stmt_2 = str(total_iters) + ' simulations with an average of ' + str(avg_iters)
        carls_bid_prnt_stmt_3 = ' simulations per converged round for a total of ' + str(num_of_games) + ' games'
        carls_bid_prnt_stmt = carls_bid_prnt_stmt_1 + carls_bid_prnt_stmt_2 + carls_bid_prnt_stmt_3
        print(carls_bid_prnt_stmt)
        #Check if Carl wants to consider a nil bid
        nil_inquiry_ans = input('Does Carl want to consider a Nil bid? (yes,no) ')
        while (((nil_inquiry_ans != 'yes') or (nil_inquiry_ans != 'no')) == False):
            #Check if Carl wants to consider a nil bid
            nil_inquiry_ans = input('Does Carl want to consider a Nil bid? (yes,no) ')
        if (nil_inquiry_ans == 'yes'):
            [Carl_Bid,num_of_games,P4_Conv_Books,All_iters,Rnd_Crd_Count_1,Rnd_Crd_Count_2,Rnd_Crd_Count_3] = Carl_Bidding_With_MCS_Std.Placing_A_Nil_Bid(num_carl_hand_list,bid_time_permit)
            #Calculate the average number of rounds
            total_iters = 0
            for ai in range(len(All_iters)):
                total_iters += All_iters[ai]
            avg_iters = round((total_iters/len(All_iters)),2)
            #Calculate the frequency for each book
            Carl_Bid_dict = {}
            for pcb in range(len(P4_Conv_Books)):
                if (P4_Conv_Books[pcb] in Carl_Bid_dict):
                    Carl_Bid_dict[P4_Conv_Books[pcb]] += 1
                else:
                    Carl_Bid_dict[P4_Conv_Books[pcb]] = 1
            sort_keys_list = sorted(Carl_Bid_dict)
            #Print the frequencies
            print()
            for key in sort_keys_list:
                freq = round((Carl_Bid_dict[key]/num_of_games)*100,2)
                prnt_stmt = 'Chance of winning ' + str(key) + ' books: ' + str(freq) + '%'
                print(prnt_stmt)
            print()
            #Announce Carl's bid
            carls_bid_prnt_stmt_1 = 'Carl is estimating a bid of ' + str(Carl_Bid) + ' after analyzing '
            carls_bid_prnt_stmt_2 = str(total_iters) + ' simulations with an average of ' + str(avg_iters)
            carls_bid_prnt_stmt_3 = ' simulations per converged round for a total of ' + str(num_of_games) + ' games'
            carls_bid_prnt_stmt = carls_bid_prnt_stmt_1 + carls_bid_prnt_stmt_2 + carls_bid_prnt_stmt_3
            print(carls_bid_prnt_stmt)
        [Player_4_Bid,nil_4_flg] = enter_ply_bid(ply4_nm)
        [Player_2_Bid,nil_2_flg] = enter_ply_bid(ply2_nm)
        
        #Confirm Bid information
        resn_flg = ''
        Team_2_Bids = enter_team_bid(2,ply2_nm,ply4_nm,resn_flg)
        resn_flg = 'valid'
        while ((Player_2_Bid + Player_4_Bid) != Team_2_Bids):    
            [Player_2_Bid,nil_2_flg] = enter_ply_bid(ply2_nm)
            [Player_4_Bid,nil_4_flg] = enter_ply_bid(ply4_nm)
            [Team_2_Bids,wheel_2_flg,blind_2_flg] = enter_team_bid(2,ply2_nm,ply4_nm,resn_flg)
        resn_flg = ''
        Team_1_Bids = enter_team_bid(1,ply1_nm,ply3_nm,resn_flg)
        resn_flg = 'bump'
        while ((Player_1_Bid + Player_3_Bid) != Team_1_Bids):    
            [Player_1_Bid,nil_1_flg] = enter_ply_bid(ply1_nm)
            [Player_3_Bid,nil_3_flg] = enter_ply_bid(ply3_nm)
            [Team_1_Bids,wheel_1_flg,blind_1_flg] = enter_team_bid(1,ply1_nm,ply3_nm,resn_flg)
    nil_flgs = [nil_1_flg,nil_2_flg,nil_3_flg,nil_4_flg]
    othr_bonus_flgs = [wheel_1_flg,wheel_2_flg,blind_1_flg,blind_2_flg]
    return(Player_1_Bid,Player_2_Bid,Player_3_Bid,Player_4_Bid,Team_1_Bids,Team_2_Bids,nil_flgs,othr_bonus_flgs)

def New_Ply_Order(winning_ply,ply_nms,nil_flgs):
    if (winning_ply == ply_nms[0]):
        ply_order = [ply_nms[0],ply_nms[1],ply_nms[2],ply_nms[3]]
        Team_1_players = ['T','O','T','O']
        Team_2_players = ['O','T','O','T']
        new_nil_flgs = [nil_flgs[0],nil_flgs[1],nil_flgs[2],nil_flgs[3]]
    elif (winning_ply == ply_nms[1]):
        ply_order = [ply_nms[1],ply_nms[2],ply_nms[3],ply_nms[0]]
        Team_1_players = ['O','T','O','T']
        Team_2_players = ['T','O','T','O']
        new_nil_flgs = [nil_flgs[1],nil_flgs[2],nil_flgs[3],nil_flgs[0]]
    elif (winning_ply == ply_nms[2]):
        ply_order = [ply_nms[2],ply_nms[3],ply_nms[0],ply_nms[1]]
        Team_1_players = ['T','O','T','O']
        Team_2_players = ['O','T','O','T']
        new_nil_flgs = [nil_flgs[2],nil_flgs[3],nil_flgs[0],nil_flgs[1]]
    elif (winning_ply == ply_nms[3]):
        ply_order = [ply_nms[3],ply_nms[0],ply_nms[1],ply_nms[2]]
        Team_1_players = ['O','T','O','T']
        Team_2_players = ['T','O','T','O']
        new_nil_flgs = [nil_flgs[3],nil_flgs[0],nil_flgs[1],nil_flgs[2]]
    return(ply_order,Team_1_players,Team_2_players,new_nil_flgs)

def human_ply_entry(ply_nm,First_Card,First_Cut):
    player_card = 'Not Entered'
    card_validity_flg = 0
    while ((player_card == 'Not Entered') or (card_validity_flg != 1)):
        try:
            input_prnt_stmt = 'Enter the book card for ' + ply_nm + ': '
            player_card = input(input_prnt_stmt)
            #Check if player card is valid
            card_validity_flg = chk_card_validity([player_card])
        except:
            player_card = 'Not Entered'
    if (First_Card == 0):
        str_First_Card = [player_card]
        First_Card_list = Reverse_Hand_Translator(str_First_Card)
        First_Card = First_Card_list[0]
    if ((player_card[-1] == 's') and (player_card == 'Big') and (player_card == 'Little')):
        First_Cut = 1
    return(player_card,First_Card,First_Cut)

def New_Dealer(curr_dealer,ply_nms):
    if (curr_dealer == ply_nms[0]):
        new_dealer = ply_nms[1]
    elif (curr_dealer == ply_nms[1]):
        new_dealer = ply_nms[2]
    elif (curr_dealer == ply_nms[2]):
        new_dealer = ply_nms[3]
    elif (curr_dealer == ply_nms[3]):
        new_dealer = ply_nms[0]
    return(new_dealer)

def Bonus_Adjust(T1_Change_no_bon,T2_Change_no_bon,All_Player_Books,Team_1_Bids,Team_2_Bids,nil_flgs,othr_bonus_flgs):
    #Parse bonus lists
    nil_1_flg = nil_flgs[0]
    nil_2_flg = nil_flgs[1]
    nil_3_flg = nil_flgs[2]
    nil_4_flg = nil_flgs[3]
    
    if ((nil_1_flg == 1) and (All_Player_Books[0] == 0)):
        T1_Change_no_bon += 100
    elif ((nil_1_flg == 1) and (All_Player_Books[0] > 0)):
        T1_Change_no_bon += -100
    if ((nil_3_flg == 1) and (All_Player_Books[2] == 0)):
        T1_Change_no_bon += 100
    elif ((nil_3_flg == 1) and (All_Player_Books[2] > 0)):
        T1_Change_no_bon += -100

    if ((nil_2_flg == 1) and (All_Player_Books[1] == 0)):
        T2_Change_no_bon += 100
    elif ((nil_2_flg == 1) and (All_Player_Books[1] > 0)):
        T2_Change_no_bon += -100
    if ((nil_4_flg == 1) and (All_Player_Books[3] == 0)):
        T2_Change_no_bon += 100
    elif ((nil_4_flg == 1) and (All_Player_Books[3] > 0)):
        T2_Change_no_bon += -100
    
    Team_1_Books = All_Player_Books[0] + All_Player_Books[2]
    Team_2_Books = All_Player_Books[1] + All_Player_Books[3]
    wheel_1_flg = othr_bonus_flgs[0]
    wheel_2_flg = othr_bonus_flgs[1]
    blind_1_flg = othr_bonus_flgs[2]
    blind_2_flg = othr_bonus_flgs[3]
    
    if ((wheel_1_flg == 1) and (Team_1_Books >= 10)):
        T1_Change_no_bon += 100
    elif ((wheel_1_flg == 1) and (Team_1_Books < 10)):
        T1_Change_no_bon += -100
    if ((wheel_2_flg == 1) and (Team_2_Books >= 10)):
        T2_Change_no_bon += 100
    elif ((wheel_2_flg == 1) and (Team_2_Books < 10)):
        T2_Change_no_bon += -100
    
    if ((blind_1_flg == 1) and (Team_1_Books >= Team_1_Bids)):
        T1_Change_no_bon += 10*Team_1_Books
    if ((blind_2_flg == 1) and (Team_2_Books >= Team_2_Bids)):
        T2_Change_no_bon += 10*Team_2_Books
    return(T1_Change_no_bon,T2_Change_no_bon)

def Manual_Carl():
    #Import libraries
    import Carl_Bidding_With_MCS_Std
    import csv
    
    #Set master file name
    master_file_nm = 'Master_Game_File.txt'
    #Get game information
    [ply_nms,game_params,game_bonuses,Team_1_status,Team_2_status,current_round,dealer] = Proc_Master_Game_File(master_file_nm)
    #Game information
    ply1_nm = ply_nms[0]
    ply2_nm = ply_nms[1]
    ply3_nm = ply_nms[2]
    ply4_nm = ply_nms[3]
    game_set = game_params[0]
    bag_limit = game_params[1]
    wheel_bonus = game_bonuses[0]
    nil_bonus = game_bonuses[1]
    Team_1_Points = Team_1_status[0]
    Team_1_Bags = Team_1_status[1]
    Team_1_Blinds = Team_1_status[2]
    Team_1_Wheels = Team_1_status[3]
    Team_1_Nils = Team_1_status[4]
    Team_2_Points = Team_2_status[0]
    Team_2_Bags = Team_2_status[1]
    Team_2_Blinds = Team_2_status[2]
    Team_2_Wheels = Team_2_status[3]
    Team_2_Nils = Team_2_status[4]
    
    #Check if the game is over
    if (Team_1_Points >= game_set):
        winner = 'TEAM 1'
        winner_points = str(Team_1_Points)
        loser_points = str(Team_2_Points)
        win_prnt_stmt = winner + ' wins with ' + winner_points + ' over ' + loser_points
        print(win_prnt_stmt)
    elif (Team_2_Points >= game_set):
        winner = 'TEAM 2'
        winner_points = str(Team_2_Points)
        loser_points = str(Team_1_Points)
        win_prnt_stmt = winner + ' wins with ' + winner_points + ' over ' + loser_points
        print(win_prnt_stmt)
    elif ((Team_1_Points == Team_2_Points) and (Team_1_Points >= game_set)):
        winner = 'TEAM 1 and TEAM 2'
        winner_points = str(Team_1_Points)
        loser_points = str(Team_2_Points)
        win_prnt_stmt = winner + ' wins with ' + winner_points
        print(win_prnt_stmt)
    else:
        '''
        Play the game
        '''
        dealer_prnt_stmt = 'Dealer is ' + dealer
        print()
        print(dealer_prnt_stmt)
        
        headers_1 = ['Team 1 Bids','Team_2_Bids','Dealer','Starting Player','Player 1 Card','Second Player','Player 2 Card','Third Player']
        headers_2 = ['Player 3 Card','Fourth Player','Player 4 Card','Team 1 Books','Team 1 Bags','Team 1 Score','Team 2 Books']
        headers_3 = ['Team 2 Bags','Team 2 Score','Team 1 Blinds','Team 1 Wheels','Team 1 Nils','Team 2 Blinds','Team 2 Wheels','Team 2 Nils']
        tot_headers = headers_1 + headers_2 + headers_3
    
        #Open the round csv file
        round_csv_fl_nm = 'Round_' + str(current_round) + '.csv'
        with open(round_csv_fl_nm, 'w', newline='') as f:
            writer = csv.DictWriter(f,fieldnames = tot_headers)
            
            writer.writeheader()
            '''
            Initialize the round
            '''
            #Accept the hand string for Carl
            carl_hand_string = input('Enter the cards for Carls hand separated by commas: ')
            #Split hand string into a list
            carl_hand_list = carl_hand_string.split(',')
            #Complete hand checks
            max_count = chk_repeated_cards(carl_hand_list)
            card_validity_flg = chk_card_validity(carl_hand_list)
            while ((len(carl_hand_list) != 13) or (max_count != 1) or (card_validity_flg != 1)):
                #Accept the hand string for Carl
                carl_hand_string = input('Please enter exactly 13 unrepeating valid cards for Carl separated by commas: ')
                #Split hand string into a list
                carl_hand_list = carl_hand_string.split(',')
                #Complete hand checks
                max_count = chk_repeated_cards(carl_hand_list)
                card_validity_flg = chk_card_validity(carl_hand_list)
            num_carl_hand_list = Reverse_Hand_Translator(carl_hand_list)
            [Player_1_Bid,Player_2_Bid,Player_3_Bid,Player_4_Bid,Team_1_Bids,Team_2_Bids,nil_bid_flgs,othr_bonus_flgs] = Acquire_Player_Bids(ply1_nm,ply2_nm,ply3_nm,ply4_nm,
                                                                                                                                             dealer,num_carl_hand_list)
            #Freeze the initial nil flag list
            orig_nil_flgs = list(nil_bid_flgs)
            '''
            Play the round
            '''
            #Initialize the round
            First_Cut = 0
            All_Player_Books = [0]*4
            Team_1_Books = []
            Team_2_Books = []
            Round_Books = 13
            #The winning ply is to the left of the dealer
            if (dealer == ply1_nm):
                winning_ply = str(ply2_nm)
            elif (dealer == ply2_nm):
                winning_ply = str(ply3_nm)
            elif (dealer == ply3_nm):
                winning_ply = str(ply4_nm)
            elif (dealer == ply4_nm):
                winning_ply = str(ply1_nm)
            [ply_order,Team_1_players,Team_2_players,nil_bid_flgs] = New_Ply_Order(winning_ply,ply_nms,nil_bid_flgs)
            Rnd_Crd_Count = 0
            while (Round_Books > 0):
                print()
                book_prnt_stmt = 'Book Number: ' + str(Round_Books)
                print(book_prnt_stmt)
                Round_Books += -1
                #Initialize the book
                Book = []
                #Initialize the first card
                First_Card = 0
                for plor in range(len(ply_order)):
                    if (ply_order[plor] != 'Carl'):
                        ply_nm = ply_order[plor]
                        [player_card,First_Card,First_Cut] = human_ply_entry(ply_nm,First_Card,First_Cut)
                        Book.append(player_card)
                    else:
                        #Translate the book into numbers
                        num_Book = Reverse_Hand_Translator(Book)
                        if ((Player_4_Bid == 0) and (All_Player_Books[3] == 0)):
                            [carl_card,First_Cut,Rnd_Crd_Count] = Carl_Bidding_With_MCS_Std.Carl_Ply4_Nil(num_Book,num_carl_hand_list,First_Cut,Team_2_players,Rnd_Crd_Count)
                        elif ((Player_2_Bid == 0) and (All_Player_Books[1] == 0)):
                            [carl_card,First_Cut,Rnd_Crd_Count] = Carl_Bidding_With_MCS_Std.Carl_Ply_W_Nil(num_Book,num_carl_hand_list,First_Cut,Team_2_players,Rnd_Crd_Count)
                        else:
                            [carl_card,First_Cut,Rnd_Crd_Count] = Carl_Bidding_With_MCS_Std.Carl(num_Book,num_carl_hand_list,First_Cut,
                                                                                                 Team_2_players,len(Team_2_Books),
                                                                                                 Team_2_Bids,Rnd_Crd_Count)
                        #Convert carl card to a string
                        disp_carl_card = Hand_Translator([carl_card])
                        prnt_stmt = 'Carl plays the card: ' + disp_carl_card[0]
                        print()
                        print(prnt_stmt)
                        Book.append(disp_carl_card[0])
                        num_carl_hand_list.remove(carl_card)
                        if (First_Card == 0):
                            First_Card = carl_card
                #Translate the book into numbers
                num_Book = Reverse_Hand_Translator(Book)
                #Evaluate the Book and decide who has the winning card
                [winning_card,winning_ply,Hierarchy] = Carl_Bidding_With_MCS_Std.Book_Grading(num_Book,First_Card)
                #Use the index to get the actual player number
                winning_ply = ply_order[winning_ply]
                #New player order
                [ply_order,Team_1_players,Team_2_players,nil_bid_flgs] = New_Ply_Order(winning_ply,ply_nms,nil_bid_flgs)
                #Track team books
                if ((winning_ply == ply1_nm) or (winning_ply == ply3_nm)):
                    Team_1_Books.append(winning_ply)
                elif ((winning_ply == ply2_nm) or (winning_ply == ply4_nm)):
                    Team_2_Books.append(winning_ply)
                #Track player books
                if (winning_ply == 1):
                    All_Player_Books[0] += 1
                elif (winning_ply == 2):
                    All_Player_Books[1] += 1
                elif (winning_ply == 3):
                    All_Player_Books[2] += 1
                elif (winning_ply == 4):
                    All_Player_Books[3] += 1
                    
                if (Round_Books > 0):
                    csv_row_1 = [Team_1_Bids,Team_2_Bids,dealer,ply_order[0],Book[0],ply_order[1],Book[1],ply_order[2],Book[2]]
                    csv_row_2 = [ply_order[3],Book[3],len(Team_1_Books),Team_1_Bags,Team_1_Points,len(Team_2_Books),Team_2_Bags,Team_2_Points]
                    csv_row_3 = [Team_1_Blinds,Team_1_Wheels,Team_1_Nils,Team_2_Blinds,Team_2_Wheels,Team_2_Nils]
                    all_csv_rows = csv_row_1 + csv_row_2 + csv_row_3
                    '''
                    Create the csv row
                    '''
                    csv_row_dict = {}
                    for th in range(len(tot_headers)):
                        csv_row_dict[tot_headers[th]] = all_csv_rows[th]
                    writer.writerow(csv_row_dict)
            #Initialize change values and calculate bonus adjustments
            T1_Change_no_bon = -Team_1_Bags
            T2_Change_no_bon = -Team_2_Bags
            [T1_Change,T2_Change] = Bonus_Adjust(T1_Change_no_bon,T2_Change_no_bon,All_Player_Books,Team_1_Bids,Team_2_Bids,orig_nil_flgs,othr_bonus_flgs)
            
            #Score the round for Team 1
            if (Team_1_Bids <= len(Team_1_Books)):
                T1_Change += (10*Team_1_Bids)
                if (othr_bonus_flgs[2] != 1):
                    Team_1_Bags += (len(Team_1_Books) - Team_1_Bids)
                T1_Change += Team_1_Bags
            elif (Team_1_Bids > len(Team_1_Books)):
                T1_Change += -(10*Team_1_Bids)
            if (Team_1_Bags >= bag_limit):
                Team_1_Bags += -bag_limit
                T1_Change += -10*bag_limit
                T1_Change += Team_1_Bags
            Team_1_Points += T1_Change
            print()
            print('TEAM 1 SCORE:',str(Team_1_Points-T1_Change),'+',str(T1_Change),'=',str(Team_1_Points))
            print('TEAM 1 BAGS:',str(Team_1_Bags))
            #Score the round for Team 2
            if (Team_2_Bids <= len(Team_2_Books)):
                T2_Change += (10*Team_2_Bids)
                if (othr_bonus_flgs[3] != 1):
                    Team_2_Bags += (len(Team_2_Books) - Team_2_Bids)
                T2_Change += Team_2_Bags
            elif (Team_2_Bids > len(Team_2_Books)):
                T2_Change += -(10*Team_2_Bids)
            if (Team_2_Bags >= bag_limit):
                Team_2_Bags += -bag_limit
                T2_Change += -10*bag_limit
                T2_Change += Team_2_Bags
            Team_2_Points += T2_Change
            print('TEAM 2 SCORE:',str(Team_2_Points-T2_Change),'+',str(T2_Change),'=',str(Team_2_Points))
            print('TEAM 2 BAGS:',str(Team_2_Bags))
            print()
            
            csv_row_1 = [Team_1_Bids,Team_2_Bids,dealer,ply_order[0],Book[0],ply_order[1],Book[1],ply_order[2],Book[2]]
            csv_row_2 = [ply_order[3],Book[3],len(Team_1_Books),Team_1_Bags,Team_1_Points,len(Team_2_Books),Team_2_Bags,Team_2_Points]
            csv_row_3 = [Team_1_Blinds,Team_1_Wheels,Team_1_Nils,Team_2_Blinds,Team_2_Wheels,Team_2_Nils]
            all_csv_rows = csv_row_1 + csv_row_2 + csv_row_3
            '''
            Create the csv row
            '''
            csv_row_dict = {}
            for th in range(len(tot_headers)):
                csv_row_dict[tot_headers[th]] = all_csv_rows[th]
            writer.writerow(csv_row_dict)
        f.close()
        
        #Read the master game file
        master_file_obj = open(master_file_nm,'r')
        raw_data = master_file_obj.readlines()
        master_file_obj.close()
        #Process the data
        proc_data = []
        for rd in range(len(raw_data)):
            row_info = raw_data[rd].strip('\n').split('\t')
            proc_data.append(row_info)
        
        #Game time information
        expl_str = proc_data[0][0]
        game_date = proc_data[0][1]
        prnt_stmt_for_write = expl_str + '\t' + game_date + '\n'
        #Team 1 name information
        team1_nm = proc_data[1][0]
        prnt_stmt_for_write = prnt_stmt_for_write + team1_nm + '\t' + ply1_nm + '\t' + ply3_nm + '\n'
        #Team 2 name information
        team2_nm = proc_data[2][0]
        prnt_stmt_for_write = prnt_stmt_for_write + team2_nm + '\t' + ply2_nm + '\t' + ply4_nm + '\n'
        #Game Limit information
        game_scr_lim_str = proc_data[3][0]
        prnt_stmt_for_write = prnt_stmt_for_write + game_scr_lim_str + '\t' + str(game_set) + '\n'
        game_bag_lim_str = proc_data[4][0]
        prnt_stmt_for_write = prnt_stmt_for_write + game_bag_lim_str + '\t' + str(bag_limit) + '\n'
        #Bonus information
        wheel_bonus_str = proc_data[5][0]
        prnt_stmt_for_write = prnt_stmt_for_write + wheel_bonus_str + '\t' + str(wheel_bonus) + '\n'
        nil_bonus_str = proc_data[6][0]
        prnt_stmt_for_write = prnt_stmt_for_write + nil_bonus_str + '\t' + str(nil_bonus) + '\n'
        
        #Team status information
        team_1_stat_str_1 = proc_data[7][0]
        team_2_stat_str_1 = proc_data[8][0]
        team_stat_str_2 = proc_data[7][2]
        team_stat_str_3 = proc_data[7][4]
        team_stat_str_4 = proc_data[7][6]
        team_stat_str_5 = proc_data[7][8]
        team_stat_str_6 = proc_data[7][10]
        
        #New Team 1 point information
        Team_1_Points = int(Team_1_Points)
        Team_1_Bags = int(Team_1_Bags)
        prnt_stmt_for_write = prnt_stmt_for_write + team_1_stat_str_1 + '\t' + str(Team_1_Points) + '\t' + team_stat_str_2 + '\t' + str(Team_1_Bags) + '\t'
        #New Team 1 bonus information
        Team_1_Blinds = int(proc_data[7][5])
        Team_1_Wheels = int(proc_data[7][7])
        Team_1_Nils = int(proc_data[7][9])
        prnt_stmt_for_write = prnt_stmt_for_write + team_stat_str_3 + '\t' + str(Team_1_Blinds) + '\t' + team_stat_str_4 + '\t' + str(Team_1_Wheels) + '\t' + team_stat_str_5 + '\t' + str(Team_1_Nils) + '\t' + team_stat_str_6 + '\n'
        #New Team 2 point information
        Team_2_Points = int(Team_2_Points)
        Team_2_Bags = int(Team_2_Bags)
        prnt_stmt_for_write = prnt_stmt_for_write + team_2_stat_str_1 + '\t' + str(Team_2_Points) + '\t' + team_stat_str_2 + '\t' + str(Team_2_Bags) + '\t'
        #New Team 2 bonus information
        Team_2_Blinds = int(proc_data[8][5])
        Team_2_Wheels = int(proc_data[8][7])
        Team_2_Nils = int(proc_data[8][9])
        prnt_stmt_for_write = prnt_stmt_for_write + team_stat_str_3 + '\t' + str(Team_2_Blinds) + '\t' + team_stat_str_4 + '\t' + str(Team_2_Wheels) + '\t' + team_stat_str_5 + '\t' + str(Team_2_Nils) + '\t' + team_stat_str_6 + '\n'
        #New Round
        round_str = proc_data[9][0]
        current_round = int(current_round+1)
        prnt_stmt_for_write = prnt_stmt_for_write + round_str + '\t' + str(current_round) + '\n'
        #New Dealer
        dealer_str = proc_data[10][0]
        dealer = New_Dealer(dealer,ply_nms)
        prnt_stmt_for_write = prnt_stmt_for_write + dealer_str + '\t' + dealer + '\n'
        #Check if the game is over
        winner_str = proc_data[11][0]
        if (Team_1_Points >= game_set):
            winner = 'TEAM 1'
            winner_points = str(Team_1_Points)
            loser_points = str(Team_2_Points)
            win_prnt_stmt = winner + ' wins with ' + winner_points + ' over ' + loser_points
            print(win_prnt_stmt)
        elif (Team_2_Points >= game_set):
            winner = 'TEAM 2'
            winner_points = str(Team_2_Points)
            loser_points = str(Team_1_Points)
            win_prnt_stmt = winner + ' wins with ' + winner_points + ' over ' + loser_points
            print(win_prnt_stmt)
        elif ((Team_1_Points == Team_2_Points) and (Team_1_Points >= game_set)):
            winner = 'TEAM 1 and TEAM 2'
            winner_points = str(Team_1_Points)
            loser_points = str(Team_2_Points)
            win_prnt_stmt = winner + ' wins with ' + winner_points
            print(win_prnt_stmt)
        else:
            winner = 'Undecided'
        prnt_stmt_for_write = prnt_stmt_for_write + winner_str + '\t' + winner
        
        #Rewrite the master game file with updated information
        master_file_obj = open(master_file_nm,'w')
        master_file_obj.write(prnt_stmt_for_write)
        master_file_obj.close()
    return(Team_1_Points,Team_2_Points,Rnd_Crd_Count)

Manual_Carl()