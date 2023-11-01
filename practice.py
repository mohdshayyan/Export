import pandas as pd
import numpy as np

#--------------------------------------------------------- Series -------------------------------------------------------------------
#s1=pd.Series()
#print(s1)
'''
df=pd.DataFrame({'Age':[36,40,35],'Desg':['Manager','Clerk','Accountant']},index=['Shaha','Parth','Neha'])
df=index.name('Name')
print(df)
'''
#df=pd.DataFrame({'Green':[2,'F'],'Red':[1,6],'Yellow':[3,7]})
#print(df)
#x=pd.Series([10,20,30],index=['kam','Jam','tam'])#(['kam','Jam','tam'],index=[10,20,30])     #,dtype=np.object_)
# tam ko 35 pr:-->
#x['tam']=35
# Modify full index in series:-->
#x.index=['k','J','t']
#print(x)
# Slicing:-->
#x=x[x>10]
#print(x)
'''
df[20]=25
df=df.T
df=df.drop(10,axis=0)
df[25]='Jam'
print(df)
'''
#Naming index:-->
#x.index.name='Name'
#x.name='Result'
#print(x)

#--------------------------------------------------------- DataFrame -------------------------------------------------------------------
#Dataframe from dict of series :
'''
s1=pd.Series(['A','B'])
s2=pd.Series(['C','D'])
df=pd.DataFrame({'A1':s1,'A2':s2})
print(df)
'''

#DataFrame from List of Dictionaries
'''
l=[{'Name':'A','Sr':'a'},{'Name':'B','Sr':'b'},{'Name':'C','Sr':'c'}]
df=pd.DataFrame(l)
print(df)
'''

# To Access Single Row

idx=['Sub1','Sub2','Sub3']
data={'A':[1,2,3],'B':[4,5,6],'C':[7,8,9]}
df=pd.DataFrame(data,index=idx)

#print(df.loc[:,:'A'])
for i,val in df.iterrows():
    print(val['B'])
print(df)

#Sort values in df:-->
'''
data={'Age':[2,1,3,5,4]}
df=pd.DataFrame(data)
df=df.sort_values(by='Age')
print(df)
'''
# Add a Column in df:-->#df['D']=[10,11,12]
#df['D']=20
#--------------------------------------------------
# Add a Row in df:-->
#df.loc['Sub4']=[10,11,12]
#--------------------------------------------------
# Drop a Column in df:-->
#1) df.pop('C')
#2) del df['C']
#3) df=df.drop(['C'],axis=1)
#--------------------------------------------------
# Drop a Row in df:-->
#df=df.drop(['Sub3'],axis=0)
#----------------------------------------------------------------------------------------
# Rename a Column in df:-->#df=df.rename({'A':'A1'},axis='columns')
#-----------------------------------------------------------------------------------------
'''
s = pd.Series([10,15,18,22])
df=pd.DataFrame(s)
df.columns=['List1']
'''
# Rename a Row(Index) in df:-->
#df=df.rename({'Sub3':'S3'})#,axis='index')
###print(df)
#-----------------------------------------------------------------------------------------
