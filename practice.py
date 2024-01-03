import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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
#ser=pd.Series([10,20,30],index=['kam','Jam','tam'])                                    #(['kam','Jam','tam'],index=[10,20,30])     #,dtype=np.object_)
# tam ko 35 pr:-->
#ser['tam']=35
# Modify full index in series:-->
#x.index=['k','J','t']
#print(x)
# Slicing:-->
#x=ser[ser>10]
#print(x)
'''
df[20]=25
df=df.T
df=df.drop(10,axis=0)
df[25]='Jam'
print(df)
'''
#Naming index:-->
#ser.index.name='Name'
#ser.name='Result'
#print(ser)

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
'''
idx=['Sub1','Sub2','Sub3']
data={'A':[1,2,3],'B':[4,5,6],'C':[7,8,9]}
df=pd.DataFrame(data,index=idx)

#print(df.loc[:,:'A'])
for i,val in df.iterrows():
    print(val['B'])
print(df)
'''
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
# Rename a Column in df:-->#df=df.rename({'A':'A1'},axis='columns' or 1)
#-----------------------------------------------------------------------------------------
'''
s = pd.Series([10,15,18,22])
df=pd.DataFrame(s)
df.columns=['List1']
'''
# Rename a Row(Index) in df:-->
#df=df.rename({'Sub3':'S3'})#,axis='index')
###print(df)
#--------------------------------------------------------- Matplotlib-------------------------------------------------------------------

#---------------------------------------------------------Line-chart---------------------------------------------------
#--------------------------Type=> 1--------------------------------
'''
s_name=['joy','roy','sam','john','carl']#x
marks=[10,20,30,50,40]#y
plt.plot(s_name,marks,color='blue')
plt.title('Students-Marks Distrubution')
plt.xlabel('Students Names')
plt.ylabel('Marks')
plt.grid(True)
plt.show()
'''
#--------------------------Type=> 2--------------------------------
'''
s_name=['joy','roy','sam','john','carl']#x
marks=[10,20,30,50,40]#y_1
height=[7,6,5,6,4]#y_2
plt.plot(s_name,marks,color='red',label='Marks') #linestyle='dotted')
plt.plot(s_name,height,color='blue',label='Height') #linestyle='dashed')
plt.title('Students-Marks & Height Distrubution')
plt.xlabel('Students Names')
plt.ylabel('Marks & Height')
plt.legend()  #(loc='upper right')
plt.grid(True)
plt.show()
'''
#---------------------------------------------------------Bar-chart---------------------------------------------------
#--------------------------Type=> 1--------------------------------
'''
s_name=['joy','roy','sam','john','carl']
marks=[10,20,30,50,40]
plt.bar(s_name,marks,color=['red','blue','green','purple','yellow'])
plt.title('Students-Marks Distrubution')
plt.xlabel('Students Names')
plt.ylabel('Marks')
#plt.grid(True)
plt.show()
'''
#--------------------------Type=> 2--------------------------------
'''
s_name=['joy','roy','sam','john','carl']
marks=[10,20,30,50,40]
height=[7,6,5,6,4]
plt.bar(s_name,marks,color='blue',label='Marks')
plt.bar(s_name,height,color='red',label='Height')
plt.title('Students-Marks & Height Distrubution')
plt.xlabel('Students Names')
plt.ylabel('Marks & Height')
plt.legend()
#plt.grid(True)
plt.show()
'''
#--------------------------Type=> 3--------------------------------
'''
data = {'Name':['joy','roy','sam','john','carl','tony'],'Height' : [60,61,63,65,61,60],'Weight' : [47,89,52,58,50,47]}
df=pd.DataFrame(data)
#print(df)
#df.index=df['Name']
df.plot(kind='bar',color=['red','blue'])
plt.show()
'''
#---------------------------------------------------------Pie-chart---------------------------------------------------
'''
s_name=['joy','roy','sam','john','carl']
marks=[10,20,30,50,40]
plt.pie(marks,colors=['red','blue','green','cyan','pink'],labels=s_name)
plt.title('Students-Marks Distrubution')
plt.show()
'''
#---------------------------------------------------------Histogram----------------------------------------------------
#--------------------------Type=> 1--------------------------------
'''
s_name=['joy','roy','sam','john','carl']
marks=[10,20,30,50,40]
plt.hist(marks)
plt.title('Students-Marks Distrubution')
plt.show()
'''
#--------------------------Type=> 2--------------------------------
'''
data = {'Name':['Arnav', 'Sheela', 'Azhar'],'Height' : [60,61,63],'Weight' : [47,89,52]}
df=pd.DataFrame(data)
df.index=df['Name']
df.hist()
plt.show()
'''
#---------------------------------------------------------Boxplot---------------------------------------------------
'''
import matplotlib.pyplot as plt
boys = [8,5,6,10,11,9,7,16,2,4]#2,4,5,6,7,8,9,10,11,16
girls=[4,10,11,12,2,3,8,7,13,14]#2,3,4,7,8,10,11,12,13,14
plt.boxplot([boys,girls])
plt.show()
'''








