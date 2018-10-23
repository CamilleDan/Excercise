# -*- coding: utf-8 -*-
"""
@author: Yangdan
"""
#pandas
import numpy as np
import pandas as pd
s=pd.Series([i*2 for i in range(1,11)])
print type(s)
dates=pd.date_range('20170301',periods=8)
df=pd.DataFrame(np.random.rand(8,5),index=dates,columns=list('ABCDE'))
print(df)
df1=pd.DataFrame({'A':1,'B':pd.Timestamp('20170301'),'C':pd.Series(1,index=list(range(4)),dtype='float32'),\
                 'D':np.array([3]*4,dtype='float32'),'E':pd.Categorical(['police','student','teacher','doctor'])})
print df1