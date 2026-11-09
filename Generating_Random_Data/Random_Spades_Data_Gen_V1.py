#SPADES
#This code distributes hands for N games of "Spades" and estimates the books 
#won for each card as probability

#_________________________________________________________________________________

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

def Random_Cards(n):
    #Import the random library
    import random
    #Gather n unique cards
    hand = []
    while (len(hand) < n):
        #Call random integer for next card
        card = random.randint(1,52)
        if card in hand:
            #Skip duplicate card
            continue
        else:
            #Append unique card
            hand.append(card)
    #Give the hand back to main driver
    return(hand)

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

def MCS_Spades_Game(Player_1,Player_2,Player_3,Player_4,
                    bk_trking,Player_1_books,Player_2_books,
                    Player_3_books,Player_4_books):
    
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
                ply_1_card = Rand_Play(First_Card,Player_1,First_Cut)
                #Remove card played from Player 1
                for p1s in range(len(Player_1)):
                    if (ply_1_card in Player_1[p1s]):
                        Player_1[p1s].remove(ply_1_card)
                if (First_Card == 0):
                    First_Card = ply_1_card
                Book.append(ply_1_card)
            elif (ply_order[plor] == 2):
                ply_2_card = Rand_Play(First_Card,Player_2,First_Cut)
                #Remove card played from Player 2
                for p2s in range(len(Player_2)):
                    if (ply_2_card in Player_2[p2s]):
                        Player_2[p2s].remove(ply_2_card)
                if (First_Card == 0):
                    First_Card = ply_2_card
                Book.append(ply_2_card)
            elif (ply_order[plor] == 3):
                ply_3_card = Rand_Play(First_Card,Player_3,First_Cut)
                #Remove card played from Player 3
                for p3s in range(len(Player_3)):
                    if (ply_3_card in Player_3[p3s]):
                        Player_3[p3s].remove(ply_3_card)
                if (First_Card == 0):
                    First_Card = ply_3_card
                Book.append(ply_3_card)
            elif (ply_order[plor] == 4):
                ply_4_card = Rand_Play(First_Card,Player_4,First_Cut)
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
        #Increment the book tally for the card that won
        bk_trking[winning_card-1] += 1
        #Generate new player order based on who won the book
        ply_order = New_Ply_Order(winning_ply)
        '''
        #Track team books
        if ((winning_ply == 1) or (winning_ply == 3)):
            Team_1_Books.append(winning_card)
        elif ((winning_ply == 2) or (winning_ply == 4)):
            Team_2_Books.append(winning_card)
        '''
        #Track player books
        if (winning_ply == 1):
            Player_1_books += 1
        elif (winning_ply == 2):
            Player_2_books += 1
        elif (winning_ply == 3):
            Player_3_books += 1
        elif (winning_ply == 4):
            Player_4_books += 1
        '''
        #Print the game
        disp_hand = Hand_Translator(Book)
        print(disp_hand)
        disp_hand = Hand_Translator([winning_card])
        print(disp_hand)
        '''
    return(bk_trking,Player_1_books,Player_2_books,
           Player_3_books,Player_4_books)
    
def Spades_Data_Gen():
    #Number of Spades games
    num_of_gms = 1000
    #Initialize book tracking
    bk_trking = [0]*52
    #Averaging across each spades game
    num_of_reps = 100
    #Open the data file for writing
    data_file = open("Rand_Spades_Play.txt","w+")
    for ngms in range(num_of_gms):
        #Shuffle the deck
        rnd_deck = Random_Cards(52)
        #Initialize and organize the players
        Player_1_st = Org_Ply_Hnd(rnd_deck[0:13])
        Player_2_st = Org_Ply_Hnd(rnd_deck[13:26])
        Player_3_st = Org_Ply_Hnd(rnd_deck[26:39])
        Player_4_st = Org_Ply_Hnd(rnd_deck[39:52])
        Player_1_full_list = []
        Player_2_full_list = []
        Player_3_full_list = []
        Player_4_full_list = []
        for nrps in range(num_of_reps):
            Player_1_full_list.append(list(Org_Ply_Hnd(rnd_deck[0:13])))
            Player_2_full_list.append(list(Org_Ply_Hnd(rnd_deck[13:26])))
            Player_3_full_list.append(list(Org_Ply_Hnd(rnd_deck[26:39])))
            Player_4_full_list.append(list(Org_Ply_Hnd(rnd_deck[39:52])))
        '''
        #Print Player hands
        for p1t in range(len(Player_1_st)):
            if (p1t < len(Player_1_st)-1):
                print(Hand_Translator(Player_1_st[p1t]), end ="\t")
            elif (p1t < len(Player_1_st)):
                print(Hand_Translator(Player_1_st[p1t]))
        for p2t in range(len(Player_2_st)):
            if (p2t < len(Player_2_st)-1):
                print(Hand_Translator(Player_2_st[p2t]), end ="\t")
            elif (p2t < len(Player_2_st)):
                print(Hand_Translator(Player_2_st[p2t]))
        for p3t in range(len(Player_3_st)):
            if (p3t < len(Player_3_st)-1):
                print(Hand_Translator(Player_3_st[p3t]), end ="\t")
            elif (p3t < len(Player_3_st)):
                print(Hand_Translator(Player_3_st[p3t]))
        for p4t in range(len(Player_4_st)):
            if (p4t < len(Player_4_st)-1):
                print(Hand_Translator(Player_4_st[p4t]), end ="\t")
            elif (p4t < len(Player_4_st)):
                print(Hand_Translator(Player_4_st[p4t]))
        print()
        '''
        #Start the game repetition
        Player_1_Books = []
        Player_2_Books = []
        Player_3_Books = []
        Player_4_Books = []
        for node in range(num_of_reps):
            Player_1 = Player_1_full_list[node]
            Player_2 = Player_2_full_list[node]
            Player_3 = Player_3_full_list[node]
            Player_4 = Player_4_full_list[node]
            #Player books
            Player_1_books = 0
            Player_2_books = 0
            Player_3_books = 0
            Player_4_books = 0
            #Play a random MCS spades game
            [bk_trking,Player_1_books,Player_2_books,Player_3_books,Player_4_books] = MCS_Spades_Game(Player_1,Player_2,Player_3,Player_4,
                                                                                                      bk_trking,Player_1_books,Player_2_books,
                                                                                                      Player_3_books,Player_4_books)

            #Append books for each repetition of the game played
            Player_1_Books.append(Player_1_books)
            Player_2_Books.append(Player_2_books)
            Player_3_Books.append(Player_3_books)
            Player_4_Books.append(Player_4_books)
        #Average the books for each player
        Player_1_book_sum = 0
        Player_2_book_sum = 0
        Player_3_book_sum = 0
        Player_4_book_sum = 0
        for pBKS in range(len(Player_1_Books)):
            Player_1_book_sum += Player_1_Books[pBKS]
            Player_2_book_sum += Player_2_Books[pBKS]
            Player_3_book_sum += Player_3_Books[pBKS]
            Player_4_book_sum += Player_4_Books[pBKS]
        Player_1_BK_avg = round(Player_1_book_sum/num_of_reps,2)
        Player_2_BK_avg = round(Player_2_book_sum/num_of_reps,2)
        Player_3_BK_avg = round(Player_3_book_sum/num_of_reps,2)
        Player_4_BK_avg = round(Player_4_book_sum/num_of_reps,2)
        #Print the book averages for each player
        d_fl_prnt_stmt = ''
        for pnst in range(len(Player_1_st)):
            short_list_1 = Player_1_st[pnst]
            for sl in range(len(short_list_1)):
                d_fl_prnt_stmt = d_fl_prnt_stmt + str(short_list_1[sl]) + '\t'
        d_fl_prnt_stmt = d_fl_prnt_stmt + str(Player_1_BK_avg) + '\n'
        data_file.write(d_fl_prnt_stmt)
        d_fl_prnt_stmt = ''
        for pnst in range(len(Player_2_st)):
            short_list_2 = Player_2_st[pnst]
            for sl in range(len(short_list_2)):
                d_fl_prnt_stmt = d_fl_prnt_stmt + str(short_list_2[sl]) + '\t'
        d_fl_prnt_stmt = d_fl_prnt_stmt + str(Player_2_BK_avg) + '\n'
        data_file.write(d_fl_prnt_stmt)
        d_fl_prnt_stmt = ''
        for pnst in range(len(Player_3_st)):
            short_list_3 = Player_3_st[pnst]
            for sl in range(len(short_list_3)):
                d_fl_prnt_stmt = d_fl_prnt_stmt + str(short_list_3[sl]) + '\t'
        d_fl_prnt_stmt = d_fl_prnt_stmt + str(Player_3_BK_avg) + '\n'
        data_file.write(d_fl_prnt_stmt)
        d_fl_prnt_stmt = ''
        for pnst in range(len(Player_4_st)):
            short_list_4 = Player_4_st[pnst]
            for sl in range(len(short_list_4)):
                d_fl_prnt_stmt = d_fl_prnt_stmt + str(short_list_4[sl]) + '\t'
        d_fl_prnt_stmt = d_fl_prnt_stmt + str(Player_4_BK_avg) + '\n'
        data_file.write(d_fl_prnt_stmt)
        '''
        #Print the player book values for each round
        for pnb in range(len(Player_1_Books)):
            d_fl_prnt_stmt = str(Player_1_Books[pnb]) + '\t' + str(Player_2_Books[pnb]) + '\t' + str(Player_3_Books[pnb]) + '\t' + str(Player_4_Books[pnb]) + '\n'
            data_file.write(d_fl_prnt_stmt)
        '''
    data_file.close()
    '''
    for bkt in range(len(bk_trking)):
        bk_trking[bkt] = round(100*(bk_trking[bkt]/(num_of_gms)),3)
    print(bk_trking[1:13])
    print(bk_trking[13:26])
    print(bk_trking[26:39])
    print(bk_trking[39:52])
    '''
    return(1)
    
Spades_Data_Gen()