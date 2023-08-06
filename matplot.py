import matplotlib.pyplot as plt
month=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
units=[12,11,14,10,13,15,17,13,14,17,12,11]
# Plotting a line chart: 
plt.plot(month,units,marker='D',linestyle='dashed',color='red') #or 'dotted'
# Modifying:
plt.xlabel('Months Names')
plt.xticks(month)
plt.ylabel('Units in Lakhs')
plt.yticks(units)
plt.title('Month-wise Production')
plt.grid(True)
#plt.legend()
plt.show()


















'''
data={'A':[30,40,50,60,78,58,74],'B':[45,78,58,74,78,58,74],'C':[6000,6700,6250,7520,78,58,74],'E':[6000,6700,6250,7570,78,58,74],'F':[6000,6700,6250,7525,78,58,74],'G':[6000,6700,6250,7740,78,58,74]}
cdf=pd.DataFrame(data)

#print(cdf)
print(cdf.max())# column
print('--------------------------------------')
print(cdf.max(axis=1))# Row
'''
'''
import pandas as pd
names = ['shruti', 'renu', 'rinku', 'nidhi', 'tinku', 'Rohit']
marks = [80, 60, 89, 90, 78, 99]
st = pd.Series(marks, index=names)
'''
#print(st['Renu']=70)
#st=st['renu']+10

#print(st)
#print(st[st> 85])

#st['renu'] += 10
#print(st)


#print(st.drop(['tinku']))







