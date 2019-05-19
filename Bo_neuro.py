# -*- coding: utf-8 -*-
"""
Bo_neuro
neuronal network
Created on Sun May 19 21:29:13 2019

@author: Bo
"""

import numpy as np

class neuro:
    
    def __init__(self):
        # creats a Bo_neuro instance
        self.inputLayers    = 3
        self.outputLayers   = 3
        self.hiddenLayers   = np.array([3])         
        
        self.Wi = np.random.randn(self.inputLayers,self.hiddenLayers[0])
        self.Wo = np.random.randn(self.hiddenLayers[-1],self.outputLayers)
        self.hiddenWeights()
                
    def hiddenWeights(self):
        self.Wh=[np.random.randn(self.hiddenLayers[i],self.outputLayers[i+1]) \
                 for i in np.arange(len(self.hiddenLayers)-1)]
        
    
    def feed_forward():
        pass    
    
    def neuro_print(self):
        print(self.inputLayers)
        
    def sigmoid(z):
        return 1/(1+np.exp(-z))
    
    def sogmoidPrime(z):
        return np.exp(-z)/((np.exp(-z)+1)**2)
        
    def feeForward(self,inp):
        self
        
    
class Neural_Network(object):
    def __init__(self):        
        #Define Hyperparameters
        self.inputLayerSize = 2
        self.outputLayerSize = 1
        self.hiddenLayerSize = 3
        
        #Weights (parameters)
        self.W1 = np.random.randn(self.inputLayerSize,self.hiddenLayerSize)
        self.W2 = np.random.randn(self.hiddenLayerSize,self.outputLayerSize) 
        
if __name__ == '__main__':
    print('the name is __main__!')