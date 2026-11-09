# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 10:12:20 2020

Single player application for spades against Carl

Features:
    1 button for game start
    4 Labels for the cards being played
    1 Entry for user bidding
    1 Button for user bidding
    1 Label for user bidding
    5 Labels for additional bidding information
    4 Labels for scoring
    1 Label for game narration
    13 buttons for each user's cards (dynamic?)
    
@author: Justin Paul
"""

def Single_Player_Spades():
    
    import tkinter as tk
    
    '''
    App design parameters
    '''
    canv_H = 1080
    canv_W = 1920
    #For Cards
    butt_W = 0.1
    butt_H = 0.2      #MAKE SURE BUTTON AR MATCHES THE CARD IMAGES
    #Start game
    strt_butt_loc = [0.05,0.05]
    #For User
    user_button_disp = ['NC','NC','NC','NC','NC','NC','NC','NC','NC','NC','NC','NC','NC']
    user_button_y = 0.775
    user_button_x = [0.025,0.0958,0.1667,0.2375,0.3083,0.3792,0.45,0.5208,0.5917,0.6625,0.7333,0.8042,0.875]
    #Card Parameters
    font_val = ('times', 20)
    text_loc = 'nw'
    #Cards in play
    CPx = [0.5,0.35,0.5,0.65]
    CPy = [0.25,0.135,0.025,0.135]
    #Bidding and narration
    bid_coor = [0.2,0.6,0.3,0.588]
    bid_dim = [0.1,0.025]
    narr_coor = [0.75,0.6]
    narr_dim = [0.2,0.025]
    #Bid displays
    user_bid_disp_coor = [0.4,0.6]
    othr_bid_disp_coor = [0.85,0.05,0.85,0.1,0.85,0.15]
    good_team_bid_coor = [0.85,0.25]
    enmy_team_bid_coor = [0.85,0.3]
    bid_disp_dim = [0.1,0.025]
    #Score displays
    good_team_score_coor = [0.775,0.45]
    enmy_team_score_coor = [0.925,0.45]
    good_team_bag_coor = [0.775,0.5]
    enmy_team_bag_coor = [0.925,0.5]
    score_disp_dim = [0.1,0.025]
    
    #Set the basis of the application
    root = tk.Tk()
    
    #Pack the background
    canvas = tk.Canvas(root,height=canv_H,width=canv_W)
    canvas.pack()
    #Pack the Frame
    frame = tk.Label(root)
    frame.place(relwidth=1,relheight=1)
    table_felt = tk.PhotoImage(file='table_felt.png')
    table_felt_label = tk.Label(root,image=table_felt)
    table_felt_label.place(x=0,y=0,relwidth=1,relheight=1)
    
    #Bidding entry
    bid_entry = tk.Entry(root,bg='white',font=font_val)
    bid_entry.place(anchor='n',relx=bid_coor[0],rely=bid_coor[1],relwidth=bid_dim[0],relheight=bid_dim[1])
    bid_button = tk.Button(root,text='Place Bid',font=font_val,command=lambda:User_Bid_Placed(bid_entry.get()))
    bid_button.place(anchor = 'n',relx=bid_coor[2],rely=bid_coor[3])
    narr_label = tk.Label(root,fg='black',text='Game Narration',font=font_val)
    narr_label.place(anchor='n',relx=narr_coor[0],rely=bid_coor[1],relwidth=narr_dim[0],relheight=narr_dim[1])
    
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
    
    def Human_Bidding(human_bid_start,bid_entry):
        import time
        Bid_Val = -1
        Possible_Bids = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
        while (Bid_Val not in Possible_Bids):
            try:
                Bid_Val = int(bid_entry.get())
                Bid_Time = time.time() - human_bid_start  
            except:
                [Bid_Val,Bid_Time] = Human_Bidding(human_bid_start,bid_entry)
        return(Bid_Val,Bid_Time)
    
    def Human_Play(human_hand,Book,First_Cut):
        Human_Card = -1
        Spades_Cards = [40,14,1,13,12,11,10,9,8,7,6,5,4,3,2]
        while (Human_Card not in human_hand):
            try:
                #Print the book for the human to see
                print(Hand_Translator(Book))
                if (First_Cut == 0):
                    print('Spades have not been played')
                else:
                    print('Spades have been played')
                Human_Card_Str = input('Enter a valid card: ')
                print()
                human_hand_readable = Hand_Translator(human_hand)
                Human_Card_Index = human_hand_readable.index(Human_Card_Str)
                Human_Card = human_hand[Human_Card_Index]
                '''
                #Obtain the suits of the book
                Book_suits = Obtain_Suits(Book)
                #Check the first cut
                if (First_Cut == 0):
                '''
                if (Human_Card in Spades_Cards):
                    First_Cut = 1
            except:
                [Human_Card,First_Cut] = Human_Play(human_hand,Book,First_Cut)
        return(Human_Card,First_Cut)

    def User_Cards_Delt(Cards_Delt):
        C1['text'] = Cards_Delt[0]
        C2['text'] = Cards_Delt[1]
        C3['text'] = Cards_Delt[2]
        C4['text'] = Cards_Delt[3]
        C5['text'] = Cards_Delt[4]
        C6['text'] = Cards_Delt[5]
        C7['text'] = Cards_Delt[6]
        C8['text'] = Cards_Delt[7]
        C9['text'] = Cards_Delt[8]
        C10['text'] = Cards_Delt[9]
        C11['text'] = Cards_Delt[10]
        C12['text'] = Cards_Delt[11]
        C13['text'] = Cards_Delt[12]
        return(1)

    def User_Card_Played(Card):
        CP1['text'] = Card
        return(Card)
    
    def User_Bid_Placed(user_bid):
        UBL['text'] = 'South Bid: ' + str(user_bid)
        return(user_bid)
    
    def Spades_Against_Carl():        
        #Import libraries
        import Carl_Bidding_With_MCS
        import time
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
        ply_order = [1,2,3,4]
        Team_1_players = ['T','O','T','O']
        Team_2_players = ['O','T','O','T']
        while ((Team_1_Points < game_set) and (Team_2_Points < game_set)):
            #Shuffle the deck
            rnd_deck = Random_Cards(52,[])
            #Initialize the players
            Player_1 = rnd_deck[0:13]
            Player_2 = rnd_deck[13:26]
            Player_3 = rnd_deck[26:39]
            Player_4 = rnd_deck[39:52]
            #Place and calculate the bids for team Carl
            narr_label['text'] = 'West is bidding'
            [Player_1_Bid,bid_time_1] = Carl_Bidding_With_MCS.Placing_A_Bid(Player_1)
            E1BL['text'] = 'West Bid: ' + str(Player_1_Bid)
            narr_label['text'] = 'East is bidding'
            [Player_3_Bid,bid_time_3] = Carl_Bidding_With_MCS.Placing_A_Bid(Player_3)
            E2BL['text'] = 'East Bid: ' + str(Player_3_Bid)
            Team_1_Bids = int(math.floor(Player_1_Bid) + math.floor(Player_3_Bid))
            ETBL['text'] = 'Enmy Bid: ' + str(Team_1_Bids)
            #Place and calculate the bids for team CarMan
            narr_label['text'] = 'North is bidding'
            [Player_2_Bid,bid_time_2] = Carl_Bidding_With_MCS.Placing_A_Bid(Player_2)
            FBL['text'] = 'North Bid: ' + str(Player_2_Bid)
            User_Cards_Delt(Hand_Translator(Org_Ply_Hnd(Player_4)))
            #Record human bid start
            narr_label['text'] = 'South is bidding'
            human_bid_start = time.time()
            [Player_4_Bid,human_bid_time] = Human_Bidding(human_bid_start,bid_entry)
            Team_2_Bids = int(math.floor(Player_2_Bid) + math.floor(Player_4_Bid))
            FTBL['text'] = 'Good Bid: ' + str(Team_1_Bids)
            sub_total_bid_time = round((bid_time_1+bid_time_2+bid_time_3+human_bid_time)/60,3)
            Total_Bid_Time += sub_total_bid_time
            narr_label['text'] = 'Match Starting'
            #Initialize the round
            First_Cut = 0
            All_Player_Books = [0]*4
            Team_1_Books = []
            Team_2_Books = []
            Round_Books = 13
            while (Round_Books > 0):
                #Subtract a book for each book played
                Round_Books += -1
                #Initialize the book
                Book = []
                #Each Player plays a card
                First_Card = 0
                for plor in range(len(ply_order)):
                    if (ply_order[plor] == 1):
                        [ply_1_card,First_Cut] = Carl_Bidding_With_MCS.Carl(Book,Player_1,First_Cut,
                                                                            Team_1_players,len(Team_1_Books),
                                                                            Team_1_Bids)
                        CP2['text'] = ply_1_card
                        #Remove card played from Player 1
                        Player_1.remove(ply_1_card)
                        if (First_Card == 0):
                            First_Card = ply_1_card
                        Book.append(ply_1_card)
                    elif (ply_order[plor] == 2):
                        [ply_2_card,First_Cut] = Carl_Bidding_With_MCS.Carl(Book,Player_2,First_Cut,
                                                                            Team_2_players,len(Team_2_Books),
                                                                            Team_2_Bids)
                        CP3['text'] = ply_2_card
                        #Remove card played from Player 2
                        Player_2.remove(ply_2_card)
                        if (First_Card == 0):
                            First_Card = ply_2_card
                        Book.append(ply_2_card)
                    elif (ply_order[plor] == 3):
                        [ply_3_card,First_Cut] = Carl_Bidding_With_MCS.Carl(Book,Player_3,First_Cut,
                                                                            Team_1_players,len(Team_1_Books),
                                                                            Team_1_Bids)
                        CP4['text'] = ply_3_card
                        #Remove card played from Player 3
                        Player_3.remove(ply_3_card)
                        if (First_Card == 0):
                            First_Card = ply_3_card
                        Book.append(ply_3_card)
                    elif (ply_order[plor] == 4):
                        #Print the human hand
                        print('Your Hand:')
                        print(Hand_Translator(Org_Ply_Hnd(Player_4)))
                        [ply_4_card,First_Cut] = Human_Play(Player_4,Book,First_Cut)
                        
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
                
                #Print the round
                disp_Book = Hand_Translator(Book)
                print(disp_Book)
                disp_Card = Hand_Translator([winning_card])
                print('P',str(winning_ply),':',disp_Card[0])
                print()
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
            '''
            #Cycle the dealer to keep it fair
            [ply_order,Team_1_players,Team_2_players] = Carl_Bidding_With_MCS.New_Ply_Order(winning_ply,
                                                                                            Team_1_players,
                                                                                            Team_2_players) 
            '''
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
            print('TEAM CARL SCORE:',str(Team_1_Points-T1_Change),'+',str(T1_Change),'=',str(Team_1_Points))
            print('TEAM CARL BAGS:',str(Team_1_Bags))
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
            print('TEAM CARMAN SCORE:',str(Team_2_Points-T2_Change),'+',str(T2_Change),'=',str(Team_2_Points))
            print('TEAM CARMAN BAGS:',str(Team_2_Bags))
            print()
            
            #Check if human wants to keep playing
            cont_play = input('Do you want to keep playing (yes/no)?:')
            if (cont_play == 'no'):
                winner = 'QUIT'
                return(winner,Total_Bid_Time)
            print()
        #Declare the winner
        if (Team_1_Points > Team_2_Points):
            winner = 'TEAM CARL'
        elif (Team_2_Points > Team_1_Points):
            winner = 'TEAM CARMAN'
        else:
            winner = 'TIE'
        print(winner)
        return(winner,Total_Bid_Time)
    
    #Game Start Button
    STBTN = tk.Button(root,text = 'Start Game',font=font_val,command=lambda:Spades_Against_Carl())
    STBTN.place(relx=strt_butt_loc[0],rely=strt_butt_loc[1])
    
    #13 buttons for the user's cards
    C1 = tk.Button(root,text = user_button_disp[0],font=font_val,anchor=text_loc,command=lambda:User_Card_Played(user_button_disp[0]))
    C1.place(relx=user_button_x[0],rely=user_button_y,relwidth=butt_W,relheight=butt_H)
    C2 = tk.Button(root,text = user_button_disp[1],font=font_val,anchor=text_loc,command=lambda:User_Card_Played(user_button_disp[1]))
    C2.place(relx=user_button_x[1],rely=user_button_y,relwidth=butt_W,relheight=butt_H)
    C3 = tk.Button(root,text = user_button_disp[2],font=font_val,anchor=text_loc,command=lambda:User_Card_Played(user_button_disp[2]))
    C3.place(relx=user_button_x[2],rely=user_button_y,relwidth=butt_W,relheight=butt_H)
    C4 = tk.Button(root,text = user_button_disp[3],font=font_val,anchor=text_loc,command=lambda:User_Card_Played(user_button_disp[3]))
    C4.place(relx=user_button_x[3],rely=user_button_y,relwidth=butt_W,relheight=butt_H)    
    C5 = tk.Button(root,text = user_button_disp[4],font=font_val,anchor=text_loc,command=lambda:User_Card_Played(user_button_disp[4]))
    C5.place(relx=user_button_x[4],rely=user_button_y,relwidth=butt_W,relheight=butt_H)
    C6 = tk.Button(root,text = user_button_disp[5],font=font_val,anchor=text_loc,command=lambda:User_Card_Played(user_button_disp[5]))
    C6.place(relx=user_button_x[5],rely=user_button_y,relwidth=butt_W,relheight=butt_H)    
    C7 = tk.Button(root,text = user_button_disp[6],font=font_val,anchor=text_loc,command=lambda:User_Card_Played(user_button_disp[6]))
    C7.place(relx=user_button_x[6],rely=user_button_y,relwidth=butt_W,relheight=butt_H)
    C8 = tk.Button(root,text = user_button_disp[7],font=font_val,anchor=text_loc,command=lambda:User_Card_Played(user_button_disp[7]))
    C8.place(relx=user_button_x[7],rely=user_button_y,relwidth=butt_W,relheight=butt_H)    
    C9 = tk.Button(root,text = user_button_disp[8],font=font_val,anchor=text_loc,command=lambda:User_Card_Played(user_button_disp[8]))
    C9.place(relx=user_button_x[8],rely=user_button_y,relwidth=butt_W,relheight=butt_H)
    C10 = tk.Button(root,text = user_button_disp[9],font=font_val,anchor=text_loc,command=lambda:User_Card_Played(user_button_disp[9]))
    C10.place(relx=user_button_x[9],rely=user_button_y,relwidth=butt_W,relheight=butt_H)    
    C11 = tk.Button(root,text = user_button_disp[10],font=font_val,anchor=text_loc,command=lambda:User_Card_Played(user_button_disp[10]))
    C11.place(relx=user_button_x[10],rely=user_button_y,relwidth=butt_W,relheight=butt_H)
    C12 = tk.Button(root,text = user_button_disp[11],font=font_val,anchor=text_loc,command=lambda:User_Card_Played(user_button_disp[11]))
    C12.place(relx=user_button_x[11],rely=user_button_y,relwidth=butt_W,relheight=butt_H)    
    C13 = tk.Button(root,text = user_button_disp[12],font=font_val,anchor=text_loc,command=lambda:User_Card_Played(user_button_disp[12]))
    C13.place(relx=user_button_x[12],rely=user_button_y,relwidth=butt_W,relheight=butt_H)
    
    #Give the labels their values
    CP_Disp = ['NC','NC','NC','NC']
    
    #4 Labels for the cards played
    CP1 = tk.Label(root,text = CP_Disp[0],font=font_val,anchor=text_loc)                #User card in play
    CP1.place(anchor='n',relx=CPx[0],rely=CPy[0],relwidth=butt_W,relheight=butt_H)
    CP2 = tk.Label(root,text = CP_Disp[1],font=font_val,anchor=text_loc)                #West (P1)
    CP2.place(anchor='n',relx=CPx[1],rely=CPy[1],relwidth=butt_W,relheight=butt_H)
    CP3 = tk.Label(root,text = CP_Disp[2],font=font_val,anchor=text_loc)                #North (P2)
    CP3.place(anchor='n',relx=CPx[2],rely=CPy[2],relwidth=butt_W,relheight=butt_H)
    CP4 = tk.Label(root,text = CP_Disp[3],font=font_val,anchor=text_loc)                #East (P3)
    CP4.place(anchor='n',relx=CPx[3],rely=CPy[3],relwidth=butt_W,relheight=butt_H)
    
    #6 Labels for the bidding information
    UBL = tk.Label(root,text = 'South: no bid',font=font_val)
    UBL.place(anchor='n',relx=user_bid_disp_coor[0],rely=user_bid_disp_coor[1],relwidth=bid_disp_dim[0],relheight=bid_disp_dim[1])
    FBL = tk.Label(root,text = 'North: no bid',font=font_val)
    FBL.place(anchor='n',relx=othr_bid_disp_coor[0],rely=othr_bid_disp_coor[1],relwidth=bid_disp_dim[0],relheight=bid_disp_dim[1])
    E1BL = tk.Label(root,text = 'West: no bid',font=font_val)
    E1BL.place(anchor='n',relx=othr_bid_disp_coor[2],rely=othr_bid_disp_coor[3],relwidth=bid_disp_dim[0],relheight=bid_disp_dim[1])
    E2BL = tk.Label(root,text = 'East: no bid',font=font_val)
    E2BL.place(anchor='n',relx=othr_bid_disp_coor[4],rely=othr_bid_disp_coor[5],relwidth=bid_disp_dim[0],relheight=bid_disp_dim[1])
    FTBL = tk.Label(root,text = 'Good: no bid',font=font_val)
    FTBL.place(anchor='n',relx=good_team_bid_coor[0],rely=good_team_bid_coor[1],relwidth=bid_disp_dim[0],relheight=bid_disp_dim[1])
    ETBL = tk.Label(root,text = 'Enmy: no bid',font=font_val)
    ETBL.place(anchor='n',relx=enmy_team_bid_coor[0],rely=enmy_team_bid_coor[1],relwidth=bid_disp_dim[0],relheight=bid_disp_dim[1])
    
    #4 Labels for the scoring information
    TSL = tk.Label(root,text = 'Good: no score',font=font_val)
    TSL.place(anchor='n',relx=good_team_score_coor[0],rely=good_team_score_coor[1],relwidth=score_disp_dim[0],relheight=score_disp_dim[1])
    TBL = tk.Label(root,text = 'Good: no bags',font=font_val)
    TBL.place(anchor='n',relx=good_team_bag_coor[0],rely=good_team_bag_coor[1],relwidth=score_disp_dim[0],relheight=score_disp_dim[1])
    
    ESL = tk.Label(root,text = 'Enmy: no score',font=font_val)
    ESL.place(anchor='n',relx=enmy_team_score_coor[0],rely=enmy_team_score_coor[1],relwidth=score_disp_dim[0],relheight=score_disp_dim[1])
    EBL = tk.Label(root,text = 'Enmy: no bags',font=font_val)
    EBL.place(anchor='n',relx=enmy_team_bag_coor[0],rely=enmy_team_bag_coor[1],relwidth=score_disp_dim[0],relheight=score_disp_dim[1])
    
    root.mainloop()
    
    return(1)

Single_Player_Spades()