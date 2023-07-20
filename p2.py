import pandas as pd

data = {
    2014: [100.5, 150.8, 200.9, 30000, 40000],
    2015: [12000, 18000, 22000, 30000, 45000],
    2016: [20000, 50000, 70000, 100000, 125000],
    2017: [50000, 60000, 70000, 80000, 90000]
}
index = ['Madhu', 'kusum', 'kinshuk', 'Ankit', 'Shuriti']
Sales = pd.DataFrame(data, index=index)

Sales2 = pd.DataFrame({2018: [50000]}, index=['Neha'])  # Corrected the dimensions of Sales2
Sales = Sales._append(Sales2)

def func():
    global Sales  # Add this line to access the global variable 'Sales'
    ch = input('Enter the option (a-k): ')
    if ch == 'a':
        print(Sales)
    elif ch == 'b':
        print(Sales.T)
    elif ch == 'c':
        print(Sales[2017])
    elif ch == 'd':
        selected_sales = Sales.loc[['Madhu', 'Ankit'], [2017, 2018]]
        print(selected_sales)
    elif ch == 'e':
        selected_sales = Sales.loc[['Shuriti'], [2016]]
        print(selected_sales)
    elif ch == 'f':
        salesman_data = [196.2, 37800, 52000, 78438, 38852]
        years = [2014, 2015, 2016, 2017, 2018]
        Sales.loc['Sumeet'] = salesman_data
        print(Sales)
    elif ch == 'g':
        Sales = Sales.drop(columns=[2014])
        print(Sales)
    elif ch == 'h':
        Sales = Sales.drop('kinshuk')
        print(Sales)
    elif ch == 'i':
        Sales = Sales.rename(index={'Ankit': 'Vivaan', 'Madhu': 'Shailesh'})
        print(Sales)
    elif ch == 'j':
        Sales.loc['Shailesh', 2018] = 100000
        print(Sales)
    elif ch == 'k':
        Sales.to_csv('salesFigures.csv', header=False, index=False)
        print("Sales data has been written to salesFigures.csv")
    else:
        print("Invalid option, please try again.")
    func()

func()



'''
import pandas as pd
data = {2014: [100.5, 150.8, 200.9, 30000, 40000],
2015: [12000, 18000, 22000, 30000, 45000],
2016: [20000, 50000, 70000, 100000, 125000],
2017: [50000, 60000, 70000, 80000, 90000]}
index = ['Madhu', 'kusum', 'kinshuk', 'Ankit', 'Shuriti']
Sales = pd.DataFrame(data, index=index)
Sales2 = pd.DataFrame({2018: [50000]}, index=['Neha'])  # Corrected the dimensions of Sales2
Sales = Sales._append(Sales2)
def func():
    ch=input('Enter the point: ')
# a)=>
    if ch=='a':
        print(Sales)
        func()

# b)=>
    if ch=='b':
        print(Sales.T)
        func()

# c)=>
    if ch=='c':
        print(Sales[2017])
        func()
              
# d)=>
    if ch=='d':
        selected_sales = Sales.loc[['Madhu', 'Ankit'], [2017, 2018]]  
        print(selected_sales)           
        func()
        
# e)=>
    if ch=='e':
         selected_sales = Sales.loc[['Shuriti'], [2016]]
         print(selected_sales)
         func()
         
# f)=>
    if ch=='f':
        salesman_data = [196.2, 37800, 52000, 78438, 38852]
        years = [2014, 2015, 2016, 2017, 2018]
        Sales.loc['Sumeet'] = salesman_data
        print(Sales)
        func()
         
# g)=>
    if ch=='g':
        Sales = Sales.drop(columns=[2014])
        print(Sales)
        func()
        
# h)=>
    if ch=='h':
        Sales = Sales.drop('kinshuk')
        print(Sales)
        func()
# i)=>
    if ch=='i':
        Sales = Sales.rename(index={'Ankit': 'Vivaan', 'Madhu': 'Shailesh'})
        print(Sales)
        func()
# j)=>
    if ch=='j':
        Sales.loc['Shailesh', 2018] = 100000
        print(Sales)
        func()

# k)=>
    if ch=='k':
        Sales.to_csv('salesFigures.csv', header=False, index=False)
        print("Sales data has been written to salesFigures.csv")
        func()

print(func())
'''
'''
data = {2014: [100.5, 150.8, 200.9, 30000, 40000],
        2015: [12000, 18000, 22000, 30000, 45000],
        2016: [20000, 50000, 70000, 100000, 125000],
        2017: [50000, 60000, 70000, 80000, 90000]}
index = ['Madhu', 'kusum', 'kinshuk', 'Ankit', 'Shuriti']
Sales = pd.DataFrame(data, index=index)

Sales2 = pd.DataFrame({2018: [50000]}, index=['Neha'])  # Corrected the dimensions of Sales2
Sales = Sales._append(Sales2)
print(Sales)
#b)
print(Sales.T)
#c)
print(Sales[2017])
#d)
selected_sales = Sales.loc[['Madhu', 'Ankit'], [2017, 2018]]  
print(selected_sales)

#e)
selected_sales = Sales.loc[['Shuriti'], [2016]]
print(selected_sales)

#(f)
salesman_data = [196.2, 37800, 52000, 78438, 38852]
years = [2014, 2015, 2016, 2017, 2018]
Sales.loc['Sumeet'] = salesman_data
print(Sales)

# g) delete the data for the year 2014 from DataFrame Sales.
# Delete data for the year 2014
Sales = Sales.drop(columns=[2014])
print(Sales)

# h) delete the data for salesman kinshuk from  the dataframe sales.
# Delete data for the salesman "kinshuk"
Sales = Sales.drop('kinshuk')
print(Sales)

# i) change the name of the salesperson Ankit to vivaan and Madhu to Shailesh.
# Change the names "Ankit" to "Vivaan" and "Madhu" to "Shailesh"
Sales = Sales.rename(index={'Ankit': 'Vivaan', 'Madhu': 'Shailesh'})
print(Sales)

# J) Update the sales made by Shailesh in 2018 to 100000.
# Update the sales made by "Shailesh" in 2018 to 100000
Sales.loc['Shailesh', 2018] = 100000
print(Sales)

# K) write the values of dataframe Sales to a comma separated file salesFigures.csv on the disk. do not write the row lables and column lables.
Sales.to_csv('salesFigures.csv', header=False, index=False)
print("Sales data has been written to salesFigures.csv")
'''
