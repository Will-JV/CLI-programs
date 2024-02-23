import numpy as np
import pandas as pd

datas = np.array([[0,3],[10,7],[20,9],[30,14],[40,15]])
column_names = ['temperature','activity']
dataframe = pd.DataFrame(data=datas,columns=column_names)
dataframe['adjusted'] = dataframe['activity'] + 2
'''
print(dataframe,'\n\n')

print("Rows #0, #1, and #2:")
print(dataframe.head(3), '\n')

print("Row #2:")
print(dataframe.iloc[[2]], '\n')

print("Rows #1, #2, and #3:")
print(dataframe[1:4], '\n')

print("Column 'temperature':")
print(dataframe['temperature'])
'''

names = ['Eleanor','Chidi','Tahani','Jason']
d = np.random.randint(low=0,high=101,size=(3,4))
frame = pd.DataFrame(data=d,columns=names)

print(frame,'\n')
print(frame['Eleanor'][1],'\n')

frame['Janet'] = frame['Tahani'] + frame['Jason']
print(frame)

#To create true copy, use pandas.DataFrame.copy() --------- ex. frame.copy()
