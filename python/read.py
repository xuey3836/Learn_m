import os
os.chdir("C:/Users/xuey3/Dropbox/baihua/")
import re
import pandas as pd
import numpy as np

r = open('list_split3', 'r')
s = r.readlines()
cs = ''.join(s)
spilt_s = cs.split("/zydeng/")

columns=["age", "name", "number"]
data=pd.DataFrame({},columns=columns)


for j, line in enumerate(spilt_s):
    if (j > 0):
        pid=[np.nan]*3
        pid[0]=re.findall('/CACD/(\d+?)_',line,flags=re.DOTALL)[0]#记录'Total time spent in G的值
        pid[1]=re.findall('\d+_(.+?)_\d+',line,flags=re.DOTALL)[0]#记录'Total time spent in G的值
        pid[2]=re.findall('_(\d+?)\.',line,flags=re.DOTALL)[0]#记录'Total time spent in G的值
        X = pd.DataFrame({'age': [pid[0]], 'name':[pid[1]], 'number':[pid[2]]})
        data=pd.concat([data,X])
    else:
        continue

data.to_csv('list_split3.txt')