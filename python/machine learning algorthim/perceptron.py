#### 04-04-2019: 20:28
## author: yuan

import numpy as np

class Perceptron:
    def __init__(self):
        self.learningrate = 0.01
        self.max_iteration = 5000
       
    ##generate linear SeparableData
    #@weight array 
    #@bias 
    #@n the sample size
    def gen_linear_separ(self, weight, bias, n):
        ## generate norm data
        weight = np.array(weight)
        p = len(weight)
        mu = np.zeros(p)
        sigma = np.eye(p)
        x = np.random.multivariate_normal(mu, sigma, n )
        y = (np.dot(x, weight) + bias > 0) * 1
        dat = np.column_stack((x, y))
        return dat
    #@x the feature array(n,p)
    #$y the label array(n)
    def train_perceptron_simple(self, x, y ):
        n = x.shape[0]
        p = x.shape[1] + 1
        self.weight = np.ones(p)
        x = np.column_stack((x,np.ones(n)))
        i = 0
        while i < n:
            if y[i]*(np.dot(self.weight, x[i,:])) <= 0:
                self.weight = self.weight + self.learningrate * y[i] * x[i,:]
                i = 0
            else:
                i = i + 1
    
    def perdict(self, x):
        labels = np.dot(self.weight, x)
        return 2*labels - 1

if __name__ == '__main__':
    p = 2
    w= np.random.random(p)
    bias = 0.4
    n = 100
    per = Perceptron()
    dat = per.gen_linear_separ(w, bias, n)
    x = dat[:,0:-1]
    y = 2*dat[:,-1]-1
    per.train_perceptron_simple(x, y)
    ## data  visualization
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_title('Linear separable data set')
    plt.xlabel('X')
    plt.ylabel('Y')
    labels = np.array(dat[:,p])
    idx_1 = np.where(dat[:,2]==1)
    p1 = ax.scatter(dat[idx_1,0], dat[idx_1,1], marker='o', color='g', label=1, s=20)
    idx_2 = np.where(dat[:,p]==0)
    p2 = ax.scatter(dat[idx_2,0], dat[idx_2,1], marker='x', color='r', label=2, s=20)
    plt.legend(loc = 'upper right')
    x1 = dat[:,1]
    x2 = (- per.weight[2] - x1 * per.weight[0])/per.weight[1]
    # yhat = np.dot(dat[:,0:-1], fit[0]) +fit[1]
    plt.plot(x1,x2, linewidth=1)
    plt.show()



