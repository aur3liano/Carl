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
    
    def Test_Function_1(Card):
        CP1['text'] = Card
        return(Card)
    
    def Test_Function_2(user_bid):
        UBL['text'] = 'South: ' + str(user_bid)
        return(user_bid)

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
    
    #Game Start Button
    STBTN = tk.Button(root,text = 'Start Game',font=font_val)
    STBTN.place(relx=strt_butt_loc[0],rely=strt_butt_loc[1])
    
    #Bidding entry
    bid_entry = tk.Entry(root,bg='white',font=font_val)
    bid_entry.place(anchor='n',relx=bid_coor[0],rely=bid_coor[1],relwidth=bid_dim[0],relheight=bid_dim[1])
    bid_button = tk.Button(root,text='Place Bid',font=font_val,command=lambda:Test_Function_2(bid_entry.get()))
    bid_button.place(anchor = 'n',relx=bid_coor[2],rely=bid_coor[3])
    narr_label = tk.Label(root,fg='black',text='Game Narration',font=font_val)
    narr_label.place(anchor='n',relx=narr_coor[0],rely=bid_coor[1],relwidth=narr_dim[0],relheight=narr_dim[1])

    #13 buttons for the user's cards
    C1 = tk.Button(root,text = user_button_disp[0],font=font_val,anchor=text_loc,command=lambda:Test_Function_1(user_button_disp[0]))
    C1.place(relx=user_button_x[0],rely=user_button_y,relwidth=butt_W,relheight=butt_H)
    C2 = tk.Button(root,text = user_button_disp[1],font=font_val,anchor=text_loc,command=lambda:Test_Function_1(user_button_disp[1]))
    C2.place(relx=user_button_x[1],rely=user_button_y,relwidth=butt_W,relheight=butt_H)
    C3 = tk.Button(root,text = user_button_disp[2],font=font_val,anchor=text_loc,command=lambda:Test_Function_1(user_button_disp[2]))
    C3.place(relx=user_button_x[2],rely=user_button_y,relwidth=butt_W,relheight=butt_H)
    C4 = tk.Button(root,text = user_button_disp[3],font=font_val,anchor=text_loc,command=lambda:Test_Function_1(user_button_disp[3]))
    C4.place(relx=user_button_x[3],rely=user_button_y,relwidth=butt_W,relheight=butt_H)    
    C5 = tk.Button(root,text = user_button_disp[4],font=font_val,anchor=text_loc,command=lambda:Test_Function_1(user_button_disp[4]))
    C5.place(relx=user_button_x[4],rely=user_button_y,relwidth=butt_W,relheight=butt_H)
    C6 = tk.Button(root,text = user_button_disp[5],font=font_val,anchor=text_loc,command=lambda:Test_Function_1(user_button_disp[5]))
    C6.place(relx=user_button_x[5],rely=user_button_y,relwidth=butt_W,relheight=butt_H)    
    C7 = tk.Button(root,text = user_button_disp[6],font=font_val,anchor=text_loc,command=lambda:Test_Function_1(user_button_disp[6]))
    C7.place(relx=user_button_x[6],rely=user_button_y,relwidth=butt_W,relheight=butt_H)
    C8 = tk.Button(root,text = user_button_disp[7],font=font_val,anchor=text_loc,command=lambda:Test_Function_1(user_button_disp[7]))
    C8.place(relx=user_button_x[7],rely=user_button_y,relwidth=butt_W,relheight=butt_H)    
    C9 = tk.Button(root,text = user_button_disp[8],font=font_val,anchor=text_loc,command=lambda:Test_Function_1(user_button_disp[8]))
    C9.place(relx=user_button_x[8],rely=user_button_y,relwidth=butt_W,relheight=butt_H)
    C10 = tk.Button(root,text = user_button_disp[9],font=font_val,anchor=text_loc,command=lambda:Test_Function_1(user_button_disp[9]))
    C10.place(relx=user_button_x[9],rely=user_button_y,relwidth=butt_W,relheight=butt_H)    
    C11 = tk.Button(root,text = user_button_disp[10],font=font_val,anchor=text_loc,command=lambda:Test_Function_1(user_button_disp[10]))
    C11.place(relx=user_button_x[10],rely=user_button_y,relwidth=butt_W,relheight=butt_H)
    C12 = tk.Button(root,text = user_button_disp[11],font=font_val,anchor=text_loc,command=lambda:Test_Function_1(user_button_disp[11]))
    C12.place(relx=user_button_x[11],rely=user_button_y,relwidth=butt_W,relheight=butt_H)    
    C13 = tk.Button(root,text = user_button_disp[12],font=font_val,anchor=text_loc,command=lambda:Test_Function_1(user_button_disp[12]))
    C13.place(relx=user_button_x[12],rely=user_button_y,relwidth=butt_W,relheight=butt_H)
    
    #Give the labels their values
    CP_Disp = ['NC','NC','NC','NC']
    
    #4 Labels for the cards played
    CP1 = tk.Label(root,text = CP_Disp[0],font=font_val,anchor=text_loc)
    CP1.place(anchor='n',relx=CPx[0],rely=CPy[0],relwidth=butt_W,relheight=butt_H)
    CP2 = tk.Label(root,text = CP_Disp[1],font=font_val,anchor=text_loc)
    CP2.place(anchor='n',relx=CPx[1],rely=CPy[1],relwidth=butt_W,relheight=butt_H)
    CP3 = tk.Label(root,text = CP_Disp[2],font=font_val,anchor=text_loc)
    CP3.place(anchor='n',relx=CPx[2],rely=CPy[2],relwidth=butt_W,relheight=butt_H)
    CP4 = tk.Label(root,text = CP_Disp[3],font=font_val,anchor=text_loc)
    CP4.place(anchor='n',relx=CPx[3],rely=CPy[3],relwidth=butt_W,relheight=butt_H)
    
    #6 Labels for the bidding information
    UBL = tk.Label(root,text = 'South: no bid',font=font_val)
    UBL.place(anchor='n',relx=user_bid_disp_coor[0],rely=user_bid_disp_coor[1],relwidth=bid_disp_dim[0],relheight=bid_disp_dim[1])
    FBL = tk.Label(root,text = 'North: no bid',font=font_val)
    FBL.place(anchor='n',relx=othr_bid_disp_coor[0],rely=othr_bid_disp_coor[1],relwidth=bid_disp_dim[0],relheight=bid_disp_dim[1])
    E1BL = tk.Label(root,text = 'East: no bid',font=font_val)
    E1BL.place(anchor='n',relx=othr_bid_disp_coor[2],rely=othr_bid_disp_coor[3],relwidth=bid_disp_dim[0],relheight=bid_disp_dim[1])
    E2BL = tk.Label(root,text = 'West: no bid',font=font_val)
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
    
    winner = 'Team 1'
    return(winner)

Single_Player_Spades()