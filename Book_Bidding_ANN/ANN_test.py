# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 00:31:38 2020

Playing with an artificial neural network class

@author: justin paul
"""

def sigmoid(x):
    import math
    import numpy as np
    z = x.shape
    y = np.zeros(z)
    for xv_1 in range(z[0]):
        for xv_2 in range(z[1]):
            y[xv_1][xv_2] = (1 / (1 + math.exp(-x[xv_1][xv_2])))
    return(y)

def sigmoid_derivative(x):
    y = sigmoid(x)*(1-sigmoid(x))
    return(y)

class NeuralNetwork:    
    def __init__(self, x, y):
        import numpy as np
        self.input      = x
        self.weights1   = np.random.rand(self.input.shape[1],4) 
        self.weights2   = np.random.rand(4,1)                 
        self.y          = y
        self.output     = np.zeros(self.y.shape)

    def feedforward(self):
        import numpy as np
        self.layer1 = sigmoid(np.dot(self.input, self.weights1))
        self.output = sigmoid(np.dot(self.layer1, self.weights2))

    def backprop(self):
        import numpy as np
        # application of the chain rule to find derivative of the loss function with respect to weights2 and weights1
        d_weights2 = np.dot(self.layer1.T, (2*(self.y - self.output) * sigmoid_derivative(self.output)))
        d_weights1 = np.dot(self.input.T,  (np.dot(2*(self.y - self.output) * sigmoid_derivative(self.output), self.weights2.T) * sigmoid_derivative(self.layer1)))
        # update the weights with the derivative (slope) of the loss function
        self.weights1 += d_weights1
        self.weights2 += d_weights2
        
def ANN_test():
    #import random
    import numpy as np
    Training_Inputs = np.array([[0,0,1],
                                [0,1,0],
                                [1,0,1],
                                [1,1,1]])
    #Build the training data outputs with matching dimensions to the inputs
    TO_shape = (4,1)
    Training_Outputs = np.zeros(TO_shape)
    Training_Outputs[1] = 1
    Training_Outputs[2] = 1
    #Establish the number of training iterations
    train_iters = 10000
    #Initialize the weight tracking
    W1_11 = []
    #Initialize the neural network
    ANN = NeuralNetwork(Training_Inputs,Training_Outputs)
    for ti in range(train_iters):
        #Train the neural network
        ANN.feedforward()
        ANN.backprop()
        #Track the value of the first weight
        W1_11.append(round(ANN.weights1[0][0],3))
        print(ANN.output)
    
    #Write the weight data to a history file
    weights_hist_fl = open('Weights_History.txt','a+')
    for w111 in range(len(W1_11)):
        weights_hist_fl.write(str(W1_11[w111]))
        weights_hist_fl.write('\n')
    weights_hist_fl.close()
    return(ANN)

ANN_test()