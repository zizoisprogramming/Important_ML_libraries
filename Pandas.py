import pandas as pd
"""

    Create the data frame either by reading from file or by hand


"""
data = [[10,"ziad"],
        [20,"Mohamed"],
        [12,"youssef"],
        [13,"xena"],
        [15,"samer"]]
data_frame = pd.DataFrame(data, columns=['age','name'])
print(data_frame)


"""

        Clean the data by certain conditions


"""

data_frame_less_than_15 = data_frame[data_frame['age'] < 15]
print(data_frame_less_than_15)


print(data_frame.head(2)) # takes int as argument and display first n rows
print(data_frame.tail(2)) # takes int as argument and display last n rows

"""

    sort values depending on certain column

"""


sorted_data_frame_by_age = data_frame.sort_values('age') # sort values depending on age
print(sorted_data_frame_by_age)

sorted_data_frame_by_name = data_frame.sort_values('name') # sort values depending on name
print(sorted_data_frame_by_name)

"""

    Convert dictionary to dataframe


"""

dict_1 = {'age':[12,14],
        'name':['ziad','xena'],
       }
  
df = pd.DataFrame(dict_1)
print(df)

"""

    Concatenate two dfs


"""

data_frame = pd.concat([data_frame,df],ignore_index=True)
print(data_frame)

"""

    Groupby method to group values according to certain value


"""



data_frame_by_age = data_frame.groupby('name')['age'].mean()
print(data_frame_by_age)

"""

    Important information about datasets


"""

print(data_frame.info()) # .info() prints non-null and count
print(data_frame.isna().sum()) # .isna().sum() prints sum of na
print(data_frame.describe()) # prints important statistical data 
print(data_frame.groupby('name').describe()) # print statistiacl data on the frame based on groups