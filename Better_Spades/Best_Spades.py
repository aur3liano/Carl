# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 13:14:46 2020

Spades but better!

@author: Justin Paul
"""

def main():
    #Import libraries
    import Carl_Bidding_With_MCS
    import Random_Bidding
    import random
    import time
    import math
    import os
    import tkinter as tk
    
    '''
    App design parameters
    '''
    canv_H = 1100
    canv_W = 1950
    #For Cards
    butt_W = 0.1
    butt_H = 0.2      #MAKE SURE BUTTON AR MATCHES THE CARD IMAGES
    #Start game
    strt_butt_loc = [0.05,0.05]
    #For User
    user_button_disp = ['NC1','NC2','NC3','NC4','NC5','NC6','NC7','NC8','NC9','NC10','NC11','NC12','NC13']
    user_button_y = 0.775
    user_button_x = [0.025,0.0958,0.1667,0.2375,0.3083,0.3792,0.45,0.5208,0.5917,0.6625,0.7333,0.8042,0.875]
    user_button_x = [user_button_x[i] + 0.05 for i in range(len(user_button_x))]
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
    
    #Universal Game Functions
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
    
    def Human_Play(human_hand,Book,Spade_Cut):
        Human_Card = -1
        Spades_Cards = [40,14,1,13,12,11,10,9,8,7,6,5,4,3,2]
        while (Human_Card not in human_hand):
            try:
                #Print the book for the human to see
                print(Hand_Translator(Book))
                if (Spade_Cut == 0):
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
                if (Spade_Cut == 0):
                '''
                if (Human_Card in Spades_Cards):
                    Spade_Cut = 1
            except:
                [Human_Card,Spade_Cut] = Human_Play(human_hand,Book,Spade_Cut)
        return(Human_Card,Spade_Cut)
    
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

    def Human_Bidding(human_bid_start):
        Bid_Val = -1
        Possible_Bids = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
        while (Bid_Val not in Possible_Bids):
            try:
                Bid_Val = int(input('Enter a valid Bid (0-13): '))
                Bid_Time = time.time() - human_bid_start  
            except:
                [Bid_Val,Bid_Time] = Human_Bidding(human_bid_start)
        return(Bid_Val,Bid_Time)
    
    #Classify card objects
    class Card(object):
        def __init__(self, value, suit):
            self.value = value
            self.suit = suit
            self.identity = value + ((suit-1)*13)
            
        def __repr__(self):
            '''
            if (self.suit == 1):
                suit_nm = 's'
            elif (self.suit == 2):
                suit_nm = 'd'
            elif (self.suit == 3):
                suit_nm = 'c'
            elif (self.suit == 4):
                suit_nm = 'h'
            if ((self.value == 1) and (self.suit == 2)):
                valu_nm = 'Little'
                suit_nm = ''
            elif ((self.value == 1) and (self.suit == 4)):
                valu_nm = 'Big'
                suit_nm = ''
            elif (self.value == 13):
                valu_nm = 'A'
            elif (self.value == 12):
                valu_nm = 'K'
            elif (self.value == 11):
                valu_nm = 'Q'
            elif (self.value == 10):
                valu_nm = 'J'
            elif (self.value < 10):
                valu_nm = str(self.value + 1)
            card_nm = valu_nm + suit_nm
            '''
            card_nm = str(self.identity)
            return(card_nm)
                
    #Classify deck list with methods
    class Std_Deck(list):
        def __init__(self):
            super().__init__()
            suits = list(range(1,5))
            values = list(range(1,14))
            [[self.append(Card(i,j)) for j in suits] for i in values]
            
        #Pull random cards from the deck
        def Rand_Deal(quant,deck):
            hand = []
            for q in range(quant):
                rand_flg = random.randint(0,len(deck)-1)
                hand.append(deck[rand_flg])
                deck.remove(deck[rand_flg])
            return(hand,deck)
    
    #Classify a player object with attributes
    class Player(object):
        def __init__(self,name,identity):
            self.name = name
            self.controller = ''
            self.identity = identity
            if ((self.identity == 1) or (self.identity == 3)):
                self.team = 'Team 1'
            else:
                self.team = 'Team 2'
            self.team_players = []
            self.hand = []
            self.carl_hand = []
            self.bid = 0
            self.books = 0
            
        def __repr__(self):
            ply_str_stmt = '--------------PLAYER ' + str(self.identity) + ' INFORMATION--------------' + '\n'
            ply_str_stmt += 'Name: ' + self.name + '\n'
            ply_str_stmt += 'Alliance: ' + self.team + '\n'
            ply_str_stmt += 'Hand: '
            for h in range(len(self.hand)):
                ply_str_stmt += str(self.hand[h]) + ' '
            ply_str_stmt += '\n'
            ply_str_stmt += 'Bid: ' + str(self.bid) + '\n'
            ply_str_stmt += 'Books: ' + str(self.books) + '\n'
            ply_str_stmt += '------------------------------------------------' + '\n'
            return(ply_str_stmt)
    
    #Classify a round between two Carls and Carl plus Human
    class Carl_Vs_Carman_Round():
        def __init__(self,Players):
            self.Players = Players
            self.identity = 0
            self.ply_order = []
            for p in range(len(self.Players)):
                self.ply_order.append(self.Players[p].identity)
            self.current_book = int(52/len(Players))
            self.Spade_Cut = 0
            self.Team_1_Bids = 0
            self.Team_2_Bids = 0
            self.Team_1_Books = []
            self.Team_2_Books = []
            self.Player_Books = [0]*len(Players)
        
        def __repr__(self):
            rond_str_stmt = '--------------ROUND ' + str(self.identity) + ' INFORMATION--------------' + '\n'
            rond_str_stmt += 'Current Player Order: ' + '\n'
            for plor in range(len(self.ply_order)):
                rond_str_stmt += 'Player ' + str(self.ply_order[plor])  + ' plays ' + str(plor+1) + '\n'
            rond_str_stmt += '\n'
            rond_str_stmt += 'Current Book: ' + str(self.current_book) + '\n'
            if (self.Spade_Cut == 0):
                rond_str_stmt += 'Spades have not been played' + '\n'
            else:
                rond_str_stmt += 'Spades have been played' + '\n'
            rond_str_stmt += 'Team 1 have won their books with these cards: ' + '\n'
            for t1b in range(len(self.Team_1_Books)):
                rond_str_stmt += str(self.Team_1_Books[t1b]) + ' '
            rond_str_stmt += '\n'
            rond_str_stmt += 'Team 2 have won their books with these cards: ' + '\n'
            for t2b in range(len(self.Team_2_Books)):
                rond_str_stmt += str(self.Team_2_Books[t2b]) + ' '
            rond_str_stmt += '\n'
            rond_str_stmt += '------------------------------------------------' + '\n'
            return(rond_str_stmt)
        
        def Player_Reorg(self):
            #Establish new list for players
            new_ply_list = []
            #Acquire the new player order
            new_ply_ordr = list(self.ply_order)
            #Pull the players
            while (len(new_ply_list) < 4):
                for p in range(len(self.Players)):
                    if (len(new_ply_ordr) == 0):
                        continue
                    elif (self.Players[p].identity == new_ply_ordr[0]):
                        new_ply_list.append(self.Players[p])
                        new_ply_ordr.remove(new_ply_ordr[0])
            self.Players = new_ply_list
        
        def Process(self):
            while (self.current_book > 0):
                #Subtract a book for each book played
                self.current_book += -1
                #Initialize the book
                Book = []
                #Initialize the first card variable
                First_Card = 0
                #Progress through round attribute ordered list of players
                for plor in range(len(self.Players)):
                    if ((self.Players[plor].controller == 'Computer') and (self.Players[plor].team == 'Team 1')):
                        [ply_card,self.Spade_Cut] = Carl_Bidding_With_MCS.Carl(Book,self.Players[plor].carl_hand,self.Spade_Cut,
                                                                               self.Players[plor].team_players,
                                                                               len(self.Team_1_Books),self.Team_1_Bids)
                        #Remove card played from Player
                        self.Players[plor].carl_hand.remove(ply_card)
                        if (First_Card == 0):
                            First_Card = ply_card
                        Book.append(ply_card)
                    elif ((self.Players[plor].controller == 'Computer') and (self.Players[plor].team == 'Team 2')):
                        [ply_card,self.Spade_Cut] = Carl_Bidding_With_MCS.Carl(Book,self.Players[plor].carl_hand,self.Spade_Cut,
                                                                               self.Players[plor].team_players,
                                                                               len(self.Team_2_Books),self.Team_2_Bids)
                        #Remove card played from Player
                        self.Players[plor].carl_hand.remove(ply_card)
                        if (First_Card == 0):
                            First_Card = ply_card
                        Book.append(ply_card)
                    elif (self.Players[plor].controller == 'Human'):
                        #Print the human hand
                        print('Your Hand:')
                        print(Hand_Translator(Org_Ply_Hnd(self.Players[plor].carl_hand)))
                        [ply_card,self.Spade_Cut] = Human_Play(self.Players[plor].carl_hand,Book,self.Spade_Cut)
                        #Remove card played from Player 4
                        self.Players[plor].carl_hand.remove(ply_card)
                        if (First_Card == 0):
                            First_Card = ply_card
                        Book.append(ply_card)
                #Evaluate the Book and decide who has the winning card
                [winning_card,winning_ply_index,Hierarchy] = Carl_Bidding_With_MCS.Book_Grading(Book,First_Card)
                #Use the index to get the actual player number
                winning_ply = self.ply_order[winning_ply_index]
                #Extract team player information
                for p in range(2):
                    if ((self.Players[p].identity == 1) or (self.Players[p].identity == 3)):
                        Team_1_players = self.Players[p].team_players
                    else:
                        Team_2_players = self.Players[p].team_players
                #Generate new player order based on who won the book
                [self.ply_order,Team_1_players,Team_2_players] = New_Ply_Order(winning_ply,
                                                                               Team_1_players,
                                                                               Team_2_players)
                #Reorganize players based on new player order
                Carl_Vs_Carman_Round.Player_Reorg(self)
                #Update team players attribute for each player on each team
                for p in range(len(self.Players)):
                    if ((self.Players[p].identity == 1) or (self.Players[p].identity == 3)):
                        self.Players[p].team_players = Team_1_players
                    else:
                        self.Players[p].team_players = Team_2_players
                #Track team books
                if ((winning_ply == 1) or (winning_ply == 3)):
                    self.Team_1_Books.append(winning_card)
                elif ((winning_ply == 2) or (winning_ply == 4)):
                    self.Team_2_Books.append(winning_card)
                #Track player books
                if (winning_ply == 1):
                    self.Player_Books[0] += 1
                elif (winning_ply == 2):
                    self.Player_Books[1] += 1
                elif (winning_ply == 3):
                    self.Player_Books[2] += 1
                elif (winning_ply == 4):
                    self.Player_Books[3] += 1
        
    #Classify full game
    class Game():
        def __init__(self):
            self.Team_1_Points = 0
            self.Team_1_Bags = 0
            self.Team_2_Points = 0
            self.Team_2_Bags = 0
            self.game_limit = 500
            self.bag_limit = 10
            self.players = []
            self.Rounds = 0
            self.winner = ''
        
        def __repr__(self):
            gam_str_stmt = 'Team 1 has: ' + str(self.Team_1_Points) + ' points' + '\n'
            gam_str_stmt += 'Team 2 has: ' + str(self.Team_2_Points) + ' points' + '\n'
            gam_str_stmt += 'Team 1 has: ' + str(self.Team_1_Bags) + ' bags' + '\n'
            gam_str_stmt += 'Team 2 has: ' + str(self.Team_2_Bags) + ' bags' + '\n'
            gam_str_stmt += 'Game ends at: ' + str(self.game_limit) + ' points' + '\n'
            gam_str_stmt += 'Bag limit set at: ' + str(self.bag_limit) + ' bags' + '\n'
            gam_str_stmt += 'Game has cycled through: ' + str(self.Rounds) + ' rounds' + '\n'
            return(gam_str_stmt)
    
    #Classify GUI
    class Spades_GUI():
        def __init__(self):
            #User fields
            self.user_hand = []
            self.user_cardimg = []
            self.user_bid_prnt = 'South: no bid'
            self.user_bid_needed = False
            
            #Bidding values
            self.north_bid_prnt = 'North: no bid'
            self.west_bid_prnt = 'West: no bid'
            self.east_bid_prnt = 'East: no bid'
            self.good_tem_bid_prnt = 'Good: no bid'
            self.enmy_tem_bid_prnt = 'Enmy: no bid'
            
            #Scoring information
            self.good_tem_scor_prnt = 'Good: no score'
            self.good_tem_bag_prnt = 'Good: no bags'
            self.enmy_tem_scor_prnt = 'Enmy: no score'
            self.enmy_tem_bag_prnt = 'Enmy: no bags'
            
            #Parametrize the gui state
            self.game_start = False
            self.game_over = True
            
            #Start the gui
            self.set_up_gui()

        def flip(self, event):
            if event.widget.flipped:
                event.widget.flipped = False
                event.widget.configure(image=event.widget.cardimage)
            else:
                event.widget.flipped = True
                event.widget.configure(image=self.backimg)
        
        def start_new_game(self):
        
            #Initialize the players
            Ply1 = Player('Player 1',1)
            Ply3 = Player('Player 3',3)
            Team_1_players = ['T','O','T','O']
            Ply1.team_players = Team_1_players
            Ply3.team_players = Team_1_players
            Ply1.controller = 'Computer'
            Ply3.controller = 'Computer'
            
            Ply2 = Player('Player 2',2)
            Ply4 = Player('Player 4',4)
            Team_2_players = ['O','T','O','T']
            Ply2.team_players = Team_2_players
            Ply4.team_players = Team_2_players
            Ply2.controller = 'Computer'
            Ply4.controller = 'Human'
            
            #Testing initialization of a round of spades
            Players = [Ply1,Ply2,Ply3,Ply4]               #THIS LIST WILL BE RANDOMIZED IN FURTURE
            spades_round = Carl_Vs_Carman_Round(Players)
            print(spades_round)
            
            #Initialize the deck for the round
            deck = Std_Deck()
            [rnd_deck,deck_2] = Std_Deck.Rand_Deal(len(deck), deck)
            
            #Deal hands to players
            Ply1.hand = rnd_deck[0:13]
            Ply2.hand = rnd_deck[13:26]
            Ply3.hand = rnd_deck[26:39]
            Ply4.hand = rnd_deck[39:52]
            for bc in range(len(Ply1.hand)):
                Ply1.carl_hand.append(int(Ply1.hand[bc].identity))
                Ply2.carl_hand.append(int(Ply2.hand[bc].identity))
                Ply3.carl_hand.append(int(Ply3.hand[bc].identity))
                Ply4.carl_hand.append(int(Ply4.hand[bc].identity))
            
            print(spades_round.Players)
            
            #Have players submit their bids
            Total_Bid_Time = 0
            [Player_1_Bid,bid_time_1] = Carl_Bidding_With_MCS.Placing_A_Bid(Ply1.carl_hand)
            print('Player 1 Bid:')
            print(Player_1_Bid)
            [Player_3_Bid,bid_time_3] = Carl_Bidding_With_MCS.Placing_A_Bid(Ply2.carl_hand)
            print('Player 3 Bid:')
            print(Player_3_Bid)
            Team_1_Bids = int(math.floor(Player_1_Bid) + math.floor(Player_3_Bid))
            print('Team 1 Bid:')
            print(Team_1_Bids)
            print()
            #Place and calculate the bids for team CarMan
            [Player_2_Bid,bid_time_2] = Carl_Bidding_With_MCS.Placing_A_Bid(Ply3.carl_hand)
            print('Player 2 Bid:')
            print(Player_2_Bid)
            print('Your Hand:')
            print(Hand_Translator(Org_Ply_Hnd(Ply4.carl_hand)))
            #Record human bid start
            human_bid_start = time.time()
            [Player_4_Bid,human_bid_time] = Human_Bidding(human_bid_start)
            print('Player 4 Bid:')
            print(Player_4_Bid)
            Team_2_Bids = int(math.floor(Player_2_Bid) + math.floor(Player_4_Bid))
            print('Team 2 Bid:')
            print(Team_2_Bids)
            print()
            sub_total_bid_time = round((bid_time_1+bid_time_2+bid_time_3+human_bid_time)/60,3)
            Total_Bid_Time += sub_total_bid_time
            
            #Testing a round of spades
            spades_round.Process()
            print(spades_round)
        
        def strt_button_clicked(self):
            if ((self.game_over) and (self.game_start == False)):
                self.start_new_game(self)
                self.game_start = True
                self.game_over = False
            elif ((self.game_start) and (self.game_over == False)):
                curr_narration_lbl = self.narr_label['text']
                self.narr_label['text'] = 'Game already in Progress'
                time.sleep(5)
                self.narr_label['text'] = curr_narration_lbl
            elif (self.game_start and self.game_over):
                self.narr_label['text'] = 'Starting new game...'
                self.start_new_game(self)
                self.game_start = True
                self.game_over = False
        
        def bid_button_clicked(self):
            if self.user_bid_needed:
                new_bid_stmt = 'South: ' + str(self.bid_entry.get())
                self.user_bid_prnt = new_bid_stmt
            else:
                curr_narration_lbl = self.narr_label['text']
                self.narr_label['text'] = 'No user bid yet'
                time.sleep(5)
                self.narr_label['text'] = curr_narration_lbl
        
        def set_up_gui(self):
            #Initialize GUI
            self.root = tk.Tk()
            
            #Pack the background
            canvas = tk.Canvas(self.root,height=canv_H,width=canv_W)
            canvas.pack()
            #Pack the Frame
            #frame_cardfile = str(self.imgdir) + "table_felt.png"
            frame_cardfile = "table_felt.png"
            self.frameimg = tk.PhotoImage(file=frame_cardfile)
            table_felt_label = tk.Label(self.root,image=self.frameimg)
            table_felt_label.place(x=0,y=0,relwidth=1,relheight=1)
            
            STBTN = tk.Button(self.root,text = 'Start Game',font=font_val,command = self.strt_button_clicked(self))
            STBTN.place(relx=strt_butt_loc[0],rely=strt_butt_loc[1])
            
            #Bidding entry
            self.bid_entry = tk.Entry(self.root,bg='white',font=font_val)
            self.bid_entry.place(anchor='n',relx=bid_coor[0],rely=bid_coor[1],relwidth=bid_dim[0],relheight=bid_dim[1])
            bid_button = tk.Button(self.root,text='Place Bid',font=font_val,command = self.bid_button_clicked(self))
            bid_button.place(anchor = 'n',relx=bid_coor[2],rely=bid_coor[3])
            self.narr_label = tk.Label(self.root,fg='black',text='Game Narration',font=font_val)
            self.narr_label.place(anchor='n',relx=narr_coor[0],rely=bid_coor[1],relwidth=narr_dim[0],relheight=narr_dim[1])

            #Set back image
            #null_cardfile = str(self.imgdir) + "null_card.png"
            null_cardfile = "null_card.png"
            self.backimg = tk.PhotoImage(file=null_cardfile)
            
            #Set up cards in play images
            for num in range(1,4):
                self.CP_lbl = tk.Label(self.root, image = self.backimg)
                self.CP_lbl.flipped = True
                self.CP_lbl.place(anchor='n',relx=CPx[num],rely=CPy[num],relwidth=butt_W,relheight=butt_H)
        
            #Set up the card in play for the user
            self.User_lbl = tk.Label(self.root, image = self.backimg)
            self.User_lbl.flipped = True
            self.User_lbl.place(anchor='n',relx=CPx[0],rely=CPy[0],relwidth=butt_W,relheight=butt_H)
            
            #Set up the user card buttons
            for num in range(13):
                self.User_C = tk.Label(self.root, image = self.backimg)
                self.User_lbl.bind("<Button-1>", self.flip)
                self.User_C.flipped = True
                self.User_C.place(anchor='n',relx=user_button_x[num],rely=user_button_y,relwidth=butt_W,relheight=butt_H)
        
            #6 Labels for the bidding information
            self.UBL = tk.Label(self.root,text = self.user_bid_prnt,font=font_val)
            self.UBL.place(anchor='n',relx=user_bid_disp_coor[0],rely=user_bid_disp_coor[1],relwidth=bid_disp_dim[0],relheight=bid_disp_dim[1])
            self.NBL = tk.Label(self.root,text = self.north_bid_prnt,font=font_val)
            self.NBL.place(anchor='n',relx=othr_bid_disp_coor[0],rely=othr_bid_disp_coor[1],relwidth=bid_disp_dim[0],relheight=bid_disp_dim[1])
            self.WBL = tk.Label(self.root,text = self.west_bid_prnt,font=font_val)
            self.WBL.place(anchor='n',relx=othr_bid_disp_coor[2],rely=othr_bid_disp_coor[3],relwidth=bid_disp_dim[0],relheight=bid_disp_dim[1])
            self.EBL = tk.Label(self.root,text = self.east_bid_prnt,font=font_val)
            self.EBL.place(anchor='n',relx=othr_bid_disp_coor[4],rely=othr_bid_disp_coor[5],relwidth=bid_disp_dim[0],relheight=bid_disp_dim[1])
            self.GTBL = tk.Label(self.root,text = self.good_tem_bid_prnt,font=font_val)
            self.GTBL.place(anchor='n',relx=good_team_bid_coor[0],rely=good_team_bid_coor[1],relwidth=bid_disp_dim[0],relheight=bid_disp_dim[1])
            self.ETBL = tk.Label(self.root,text = self.enmy_tem_bid_prnt,font=font_val)
            self.ETBL.place(anchor='n',relx=enmy_team_bid_coor[0],rely=enmy_team_bid_coor[1],relwidth=bid_disp_dim[0],relheight=bid_disp_dim[1])
            
            #4 Labels for the scoring information
            self.TSL = tk.Label(self.root,text = self.good_tem_scor_prnt,font=font_val)
            self.TSL.place(anchor='n',relx=good_team_score_coor[0],rely=good_team_score_coor[1],relwidth=score_disp_dim[0],relheight=score_disp_dim[1])
            self.TBL = tk.Label(self.root,text = self.good_tem_bag_prnt,font=font_val)
            self.TBL.place(anchor='n',relx=good_team_bag_coor[0],rely=good_team_bag_coor[1],relwidth=score_disp_dim[0],relheight=score_disp_dim[1])
            
            self.ESL = tk.Label(self.root,text = self.enmy_tem_scor_prnt,font=font_val)
            self.ESL.place(anchor='n',relx=enmy_team_score_coor[0],rely=enmy_team_score_coor[1],relwidth=score_disp_dim[0],relheight=score_disp_dim[1])
            self.EBL = tk.Label(self.root,text = self.enmy_tem_bag_prnt,font=font_val)
            self.EBL.place(anchor='n',relx=enmy_team_bag_coor[0],rely=enmy_team_bag_coor[1],relwidth=score_disp_dim[0],relheight=score_disp_dim[1])
            
    
    SG = Spades_GUI()
    tk.mainloop()
    
    return(1)

main()