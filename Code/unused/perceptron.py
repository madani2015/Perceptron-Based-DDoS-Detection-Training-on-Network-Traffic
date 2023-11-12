import numpy as np

class Perceptron:
    
    def __init__(self):
        '''
        Constructor of the class. Defines the class' two parameters w and b as None
        '''
        self.w = None
        self.b = None
        
    def initialize_weights(self, X, w = None,b = None):
        '''
        Initializes the weights (w) and bias term (b) of the perceptron, making sure that w matches the feature dimension space.
        Both w and b can be provided by the user.
        
        Inputs:
        X - Input dataset
        w - (optional) vector of weights. If not provided, w will be initialized with a random vector
        b - (optional) bias 
        '''
        
        if w is None:
            w = np.random.rand(X.shape[1],1)
        
        if b is None:
            b =  np.random.rand(1,1)   
            
        self.w = w
        self.b = b
        
    def gradient_descent_step(self, x, y, w, b, alpha):
        '''
        Performs a gradient descent step for the perceptron updating w and b
        
        Input:
        x - input sample
        y - label associated to x
        w - Parameters vector of size D x 1
        b - Bias term (scalar)
        alpha - Learning rate 
        '''
        
        #YOUR CODE HERE
        w = w + (alpha * x * y)
        b = b + alpha * y
        
        
        
        self.w = w
        self.b = b
        
        return
    
    def perceptron_algorithm(self, X, y, w = None, b = None, alpha = 0.01):
        '''
        Implements the perceptron algorithm as seen in the course. 
        Input:
        X - Matrix with input features
        y - vector of labels
        w - Parameters vector of size D x 1 (optional)
        b - Bias term (optional)
        alpha - Learning rate (default value 0.01)
        
        Returns
        Number of iterations performed
        '''
        
        self.initialize_weights(X, w, b)
        print(f'Initial weights: ({self.w},{self.b})')

        iteration = 0
    
        while True:
            print("*************** Iteration No: ", iteration, "************************")
            #YOUR CODE HERE
            m = 0
            n = y.size
            for k in range(n):
                x = X[k][np.newaxis]
                if ((self.w.transpose().dot(x.T) + self.b) * y[k]) < 0:
                    self.gradient_descent_step(x.T, y[k], self.w, self.b, alpha)
                    print(f'updated weights: {self.w} and bias: {self.b})')
                    m += 1

            if m == 0:
                return iteration
            iteration += 1

        return iteration
    
    def predict(self, X):
        '''
        Predicts labels y given an input matrix X
        Input: 
        X- matrix of dimensions N x D

        Output:
        y_pred - vector of labels (dimensions N x 1)
        '''
        
        #YOUR CODE HERE
        y_pred = np.zeros(X.shape[0])
        cmpt = 0
        for x in X:
            if self.w.transpose().dot(x) + self.b > 0:
                y_pred[cmpt] = 1
            else :
                y_pred[cmpt] = -1
            cmpt += 1
        return y_pred

