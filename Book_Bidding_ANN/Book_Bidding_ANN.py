# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 23:32:14 2020

This script is an artificial neural network that maps a spades hand
(13 poker cards) to a book bidding value (0-13)

The ANN is trained on a set of spades data:
    book values corresponding to spades hands

@author: justin paul
"""

'''
Python program for implementation of Quicksort Sort 
'''
# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot 
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

# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low --> Starting index, 
# high --> Ending index 
# Function to do Quick sort 
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

def BK_BID_ANN():
    '''
    Process training data as inputs for the neural network
    '''
    #Open the training data document
    train_data_file = open('Rand_Spades_Play.txt','r')
    #Build training set
    train_data = train_data_file.readlines()
    spades_train_set = []
    for td in range(len(train_data)):
        spades_hand = train_data[td].strip('\n').split('\t')
        spades_train_set.append(spades_hand)
    #Parse the training set into hands and corresponding book values
    Spades_Hands = []
    Book_Values = []
    for sts in range(len(spades_train_set)):
        #Convert card values from strings to integers
        spades_hand_num_cv = []
        for cv in range(len(spades_train_set[sts][0:13])):
            spades_hand_num_cv.append(int(spades_train_set[sts][cv]))
        Spades_Hands.append(spades_hand_num_cv)
        Book_Values.append(float(spades_train_set[sts][13]))
    #Sort all the spades hands in the training set by ascending value
    Spades_Hands_Sorted = []
    for SH in range(len(Spades_Hands)):
        spades_hand = Spades_Hands[SH]
        n = len(spades_hand)
        spades_hand_sorted = quickSort(spades_hand,0,n-1)
        Spades_Hands_Sorted.append(spades_hand_sorted)

    '''
    Train the neural network
    '''
    
    return()

BK_BID_ANN()