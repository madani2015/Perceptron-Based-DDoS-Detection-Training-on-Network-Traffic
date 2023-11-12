from scipy import stats
import numpy as np

class KNN:
    '''
    k nearest neighboors algorithm class
    __init__() initialize the model
    train() trains the model
    predict() predict the class for a new point
    '''

    def __init__(self, k):
        '''
        INPUT :
        - k : is a natural number bigger than 0 
        '''

        if k <= 0:
            raise Exception("Sorry, no numbers below or equal to zero. Start again!")
            
        # empty initialization of X and y
        self.X = []
        self.y = []
        # k is the parameter of the algorithm representing the number of neighborhoods
        self.k = k
        
    def train(self,X,y):
        '''
        INPUT :
        - X : is a 2D Nx2 numpy array containing the coordinates of points
        - y : is a 1D Nx1 numpy array containing the labels for the corrisponding row of X
        '''        
        
        self.X=X.copy() # copy your training points
        self.y=y.copy()
       
    def predict(self,X_new,p):
        '''
        INPUT :
        - X_new : is a Mx2 numpy array containing the coordinates of new points whose label has to be predicted
        
        OUTPUT :
        - y_hat : is a Mx1 numpy array containing the predicted labels for the X_new points
        ''' 
            
        dst = self.minkowski_dist(X_new, p) #Estimates the Minkowski distance, order p, of a set of X_new points to the data in the training set.
        ordered = np.argsort(dst, axis=1) # Orders all distances in ascending order
        neighbors = self.y[ordered[:,0:self.k]] #For every point in the test set, picks the k closest points in the training set
        y_hat, _ = stats.mode(neighbors, axis=1) #As seen in the lecture, we use the mode to assign labels to the new data

        return y_hat

    def predict_train(self, X_new, p):
        '''
        INPUT :
        - X_new : is a Mx2 numpy array containing the coordinates of new points whose label has to be predicted
        
        OUTPUT :
        - y_hat : is a Mx1 numpy array containing the predicted labels for the X_new points
        ''' 
        # prediction part"    
        dst = self.minkowski_dist(X_new, p) #Estimates the Minkowski distance, order p, of a set of X_new points to the data in the training set.
        ordered = np.argsort(dst, axis=1) # Orders all distances in ascending order
        neighbors = self.y[ordered[:,0:self.k]] #For every point in the test set, picks the k closest points in the training set
        y_hat, _ = stats.mode(neighbors, axis=1) #As seen in the lecture, we use the mode to assign labels to the new data

        #training part
        
        X = np.vstack((np.array(self.X), X_new ))
        y = np.array(self.y.copy())
        for k in range(y_hat.size):
            y = np.append(y,y_hat[k])
        self.train(X, y)

        return y_hat

    
    def minkowski_dist(self,X_new,p):
        '''
        INPUT : 
        - X_new : is a Mx2 numpy array containing the coordinates of points for which the distance to the training set X will be estimated
        - p : parameter of the Minkowski distance
        
        OUTPUT :
        - dst : is an MxN numpy array containing the distance of each point in X_new to X
        '''
        ######### Task 1.2 YOUR CODE HERE - do not delete this line ################
        M = X_new.shape[0]
        N = self.X.shape[0]
        
        dst = np.zeros((M,N))
        
        for j in range(N):
            for i in range(M):
                dst[i,j] = ((abs(self.X[j,0] - X_new[i,0]) ** p) + (abs(self.X[j,1] - X_new[i,1]) ** p))  ** (1/p)
        ######## Task 1.2 END OF YOUR CODE HERE - do not delete this line ##########
        
        
        return dst