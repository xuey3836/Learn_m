import pandas as pd
import numpy as np 

def knnclassfied(newdata, train_feature, train_label, k):
    ntest = newdata.shape[0]
    ntrain = train_label.shape[0]
    newlabel = np.array(['A']*ntest )
    for i in range(ntest):
        dist = np.array([np.nan]*ntrain)
        for j in range(ntrain):
            # Euclidean distance
            dist[j] = (sum ((newdata[i,:] - train_feature[j,:] )**2))**0.5
        sortindex = dist.argsort()
        classrecord = train_label[sortindex[:k]].tolist()
        ##choose the most common label
        re = dict((a, classrecord.count(a)) for a in classrecord)
        mostTimes_num = sorted(re.items(),key=lambda item: item[1], reverse=True)[0][0]
        newlabel[i] = mostTimes_num
    return newlabel
    

##normalize feature
def normalize(X, type):
    p = X.shape[1]
    if type == 'minmax':
        for i in range(p):
            min = X[:,i].min()
            max = X[:,i].max()
            X[:,i] = (X[:,i] - min)/ (max - min)
    elif type == 'normalization':
        for i in range(p):
            mean = X[:,i].mean()
            var = X[:,i].var()
            X[:,i] = (X[:,i] - mean)/ sqrt(var)
    return X


if __name__ == "__main__":
    #read data
    path = 'D:/Data/Machine-Learning-with-R-datasets-master/wisc_bc_data.csv'
    dat =  pd.read_csv(path)

    label = np.array(dat['diagnosis'])
    feature = np.array(dat.drop(['id','diagnosis'], axis=1))
    ##normalize
    feature_n = normalize(feature, type = 'minmax')

    ##spilt the training and test data
    wbcd_train = feature_n[:469,:]
    wbcd_test = feature_n[469:,:]

    wbcd_train_labels = label[:469]
    wbcd_test_labels = label[469:]
    ## predict
    wbcd_test_pred = knnclassfied(wbcd_test, wbcd_train, wbcd_train_labels, k=  5)

    ## evaluate： confusion matrix
    conmatrix  = np.zeros((2,2))
    for i in range(len(wbcd_test_labels)):
        if wbcd_test_labels[i] == 'B':
            if  wbcd_test_pred[i]== 'B':
                conmatrix[0,0] = conmatrix[0,0] + 1
            else:
                conmatrix[1,0] = conmatrix[1,0] + 1
        else:
            if  wbcd_test_pred[i]== 'B':
                conmatrix[0,1] = conmatrix[0,1] + 1
            else:
                conmatrix[1,1] = conmatrix[1,1] + 1
    print(conmatrix)


