

import pandas as pd
import numpy as np

# converting a numpy array to series
alphabets = np.array(['a', 'b', 'c', 'd', 'e'])
pd_series = pd.Series(alphabets)
pd_series
     
0    a
1    b
2    c
3    d
4    e
dtype: object

# converting a dictionary to series
dictionary = {"a": 0, "b": 1, "c": 2}
pd_dict_series = pd.Series(dictionary)
pd_dict_series
     
a    0
b    1
c    2
dtype: int64

# combinin two arrays to form a object
new_list = np.array(['a', 'b', 'c'])
another_list = np.array([1, 2, 3])
new_series = pd.Series(new_list, another_list)
new_series
     
1    a
2    b
3    c
dtype: object

# converting the data type of list to a specific format using dtype
new_list_1 = np.array([1, 2, 3, 4])
pd_series = pd.Series(new_list_1, dtype=float)
pd_series
     
0    1.0
1    2.0
2    3.0
3    4.0
dtype: float64

new_list_1 = {'a': 1, 'b': 2, 'c': 3}
new_series = pd.Series(new_list_1, index=["b", "c", "d"]).fillna(1)
new_series
     
b    2.0
c    3.0
d    1.0
dtype: float64

# create a scalar value, and then covert it to series

scalar_value = 5
series = pd.Series(scalar_value)
print(series)
     
0    5
dtype: int64

# accessing values using internal and external index
new_series = pd.Series([1, 2, 3, 4, 5], index=["one", "two", "three", "four", "five"])
print(new_series[0:2])
print()
print(new_series['three'])
     
one    1
two    2
dtype: int64

3

from google.colab import files

sample_data = files.upload()
     
Upload widget is only available when the cell has been executed in the current browser session. Please rerun this cell to enable.
Saving nyc_weather.csv to nyc_weather.csv

df = pd.read_csv("./nyc_weather.csv")
     

dataframe = pd.DataFrame()
print(dataframe)
     
Empty DataFrame
Columns: []
Index: []

# list to dataframe example
data = ['Alice', 'Bob', 'Claire', 'David']
df = pd.DataFrame(data)
print(df)

     
        0
0   Alice
1     Bob
2  Claire
3   David

# create two dimensional data , assign column names manually, using Dataframe
data = [['Alice', 20], ['Bob', 21], ['Claire', 20], ['David', 22]]
df = pd.DataFrame(data, columns=['Name', 'Age'])
print(df)
     
     Name  Age
0   Alice   20
1     Bob   21
2  Claire   20
3   David   22

# changing data type of column
data = [['Alice', 20], ['Bob', 21], ['Claire', 20], ['David', 22]]
df = pd.DataFrame(data, columns=['Name', 'Age'], dtype=float)

print(df)
     
     Name   Age
0   Alice  20.0
1     Bob  21.0
2  Claire  20.0
3   David  22.0
<ipython-input-51-4d3ec82502ce>:5: FutureWarning: Could not cast to float64, falling back to object. This behavior is deprecated. In a future version, when a dtype is passed to 'DataFrame', either all columns will be cast to that dtype, or a TypeError will be raised.
  df = pd.DataFrame(data, columns=['Name', 'Age'], dtype=float)

# creating a dataframe from dictionary

import pandas as pd
data = {'Name':['Alice', 'Bob', 'Claire', 'David'],
        'Age':[20, 21, 20, 22]}
df = pd.DataFrame(data)
print(df)
     
     Name  Age
0   Alice   20
1     Bob   21
2  Claire   20
3   David   22

# creating a dataframe from a list of dictionary
data = [{'Name': 'Alice', 'Age': 20},
        {'Name': 'Bob', 'Age': 21},
        {'Name': 'Claire', 'Age': 20},
        {'Name': 'David', 'Age': 22}]
df = pd.DataFrame(data)
print(df)
     
     Name  Age
0   Alice   20
1     Bob   21
2  Claire   20
3   David   22

pd.DataFrame(df)
     
EST	Temperature	DewPoint	Humidity	Sea Level PressureIn	VisibilityMiles	WindSpeedMPH	PrecipitationIn	CloudCover	Events	WindDirDegrees
0	1/1/2016	38	23	52	30.03	10	8.0	0	5	NaN	281
1	1/2/2016	36	18	46	30.02	10	7.0	0	3	NaN	275
2	1/3/2016	40	21	47	29.86	10	8.0	0	1	NaN	277
3	1/4/2016	25	9	44	30.05	10	9.0	0	3	NaN	345
4	1/5/2016	20	-3	41	30.57	10	5.0	0	0	NaN	333
5	1/6/2016	33	4	35	30.50	10	4.0	0	0	NaN	259
6	1/7/2016	39	11	33	30.28	10	2.0	0	3	NaN	293
7	1/8/2016	39	29	64	30.20	10	4.0	0	8	NaN	79
8	1/9/2016	44	38	77	30.16	9	8.0	T	8	Rain	76
9	1/10/2016	50	46	71	29.59	4	NaN	1.8	7	Rain	109
10	1/11/2016	33	8	37	29.92	10	NaN	0	1	NaN	289
11	1/12/2016	35	15	53	29.85	10	6.0	T	4	NaN	235
12	1/13/2016	26	4	42	29.94	10	10.0	0	0	NaN	284
13	1/14/2016	30	12	47	29.95	10	5.0	T	7	NaN	266
14	1/15/2016	43	31	62	29.82	9	5.0	T	2	NaN	101
15	1/16/2016	47	37	70	29.52	8	7.0	0.24	7	Rain	340
16	1/17/2016	36	23	66	29.78	8	6.0	0.05	6	Fog-Snow	345
17	1/18/2016	25	6	53	29.83	9	12.0	T	2	Snow	293
18	1/19/2016	22	3	42	30.03	10	11.0	0	1	NaN	293
19	1/20/2016	32	15	49	30.13	10	6.0	0	2	NaN	302
20	1/21/2016	31	11	45	30.15	10	6.0	0	1	NaN	312
21	1/22/2016	26	6	41	30.21	9	NaN	0.01	3	Snow	34
22	1/23/2016	26	21	78	29.77	1	16.0	2.31	8	Fog-Snow	42
23	1/24/2016	28	11	53	29.92	8	6.0	T	3	Snow	327
24	1/25/2016	34	18	54	30.25	10	3.0	0	2	NaN	286
25	1/26/2016	43	29	56	30.03	10	7.0	0	2	NaN	244
26	1/27/2016	41	22	45	30.03	10	7.0	T	3	Rain	311
27	1/28/2016	37	20	51	29.90	10	5.0	0	1	NaN	234
28	1/29/2016	36	21	50	29.58	10	8.0	0	4	NaN	298
29	1/30/2016	34	16	46	30.01	10	7.0	0	0	NaN	257
30	1/31/2016	46	28	52	29.90	10	5.0	0	0	NaN	241


     
