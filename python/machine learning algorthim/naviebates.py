import numpy as np 

class NaiveBayes:
    def train(self, train_feature, train_label):
        n = train_label.shape[0]
        self.p = train_feature.shape[1]
        self.re = self.npcount(train_label)
        self.x = {}
        for k in self.re.keys():
            x1 = {}
            for i in range(self.p):
                 x1[i] = self.npcount(train_feature[train_label == k,i])
            self.x[k] = x1

    def predict(self, newfeature):
        result = {}
        for i in self.re.keys():
            L = 1
            for j in range(self.p):
                L = L*self.x[i][j][newfeature[j]]
            result[i] = self.re[i] * L
        return sorted(result.items(),  key=lambda item: item[1], reverse = True)[0][0]
    
    def npcount(self, array1):  
        n = len(array1)
        yclass  = np.unique(array1)
        result = {}
        for k in yclass:
            result[k] = sum(array1 == k)/n
        return result

if __name__ == "__main__":
    feature = np.array([np.repeat(np.arange(1,4,1),5),
            ['S','M','M','S','S','S','M','M','L','L','L','M','M','L','L']]).T
    label = np.array([-1,-1,1,1,-1,-1,-1,1,1,1,1,1,1,1,-1])
    nb = NaiveBayes()
    nb.train(feature, label)
    newfeature = np.array([2,'S'])
    pre = nb.predict(newfeature)
    print(pre)




