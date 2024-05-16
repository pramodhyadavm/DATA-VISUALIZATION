

from google.colab import files
df = files.upload()
     
Upload widget is only available when the cell has been executed in the current browser session. Please rerun this cell to enable.
Saving train.csv to train.csv

import pandas as pd
import numpy as np

data = pd.read_csv('./train.csv')
data.head()
     
PassengerId	Survived	Pclass	Name	Sex	Age	SibSp	Parch	Ticket	Fare	Cabin	Embarked
0	493	0	1	Molson, Mr. Harry Markland	male	55.0	0	0	113787	30.5000	C30	S
1	53	1	1	Harper, Mrs. Henry Sleeper (Myna Haxtun)	female	49.0	1	0	PC 17572	76.7292	D33	C
2	388	1	2	Buss, Miss. Kate	female	36.0	0	0	27849	13.0000	NaN	S
3	192	0	2	Carbines, Mr. William	male	19.0	0	0	28424	13.0000	NaN	S
4	687	0	3	Panula, Mr. Jaako Arnold	male	14.0	4	1	3101295	39.6875	NaN	S

cols = ['Name', 'Ticket', 'Cabin']
filtered_data = data.drop(cols, axis = 1)
filtered_data.info()
     
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 712 entries, 0 to 711
Data columns (total 9 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   PassengerId  712 non-null    int64  
 1   Survived     712 non-null    int64  
 2   Pclass       712 non-null    int64  
 3   Sex          712 non-null    object 
 4   Age          566 non-null    float64
 5   SibSp        712 non-null    int64  
 6   Parch        712 non-null    int64  
 7   Fare         712 non-null    float64
 8   Embarked     710 non-null    object 
dtypes: float64(2), int64(5), object(2)
memory usage: 50.2+ KB

data = data.dropna()
data.info()
     
<class 'pandas.core.frame.DataFrame'>
Int64Index: 148 entries, 0 to 695
Data columns (total 12 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   PassengerId  148 non-null    int64  
 1   Survived     148 non-null    int64  
 2   Pclass       148 non-null    int64  
 3   Name         148 non-null    object 
 4   Sex          148 non-null    object 
 5   Age          148 non-null    float64
 6   SibSp        148 non-null    int64  
 7   Parch        148 non-null    int64  
 8   Ticket       148 non-null    object 
 9   Fare         148 non-null    float64
 10  Cabin        148 non-null    object 
 11  Embarked     148 non-null    object 
dtypes: float64(2), int64(5), object(5)
memory usage: 15.0+ KB

data.head()
     
PassengerId	Survived	Pclass	Name	Sex	Age	SibSp	Parch	Ticket	Fare	Cabin	Embarked
0	493	0	1	Molson, Mr. Harry Markland	male	55.0	0	0	113787	30.5000	C30	S
1	53	1	1	Harper, Mrs. Henry Sleeper (Myna Haxtun)	female	49.0	1	0	PC 17572	76.7292	D33	C
9	752	1	3	Moor, Master. Meier	male	6.0	0	1	392096	12.4750	E121	S
10	541	1	1	Crosby, Miss. Harriet R	female	36.0	0	2	WE/P 5735	71.0000	B22	S
14	873	0	1	Carlsson, Mr. Frans Olof	male	33.0	0	0	695	5.0000	B51 B53 B55	S

dummies = []
cols = ['Pclass', 'Sex', 'Embarked']
for col in cols:
  dummies.append(pd.get_dummies(data[col]))

dummies
     
[     1  2  3
 0    1  0  0
 1    1  0  0
 2    0  1  0
 3    0  1  0
 4    0  0  1
 ..  .. .. ..
 707  0  0  1
 708  1  0  0
 709  0  0  1
 710  0  1  0
 711  1  0  0
 
 [712 rows x 3 columns],
      female  male
 0         0     1
 1         1     0
 2         1     0
 3         0     1
 4         0     1
 ..      ...   ...
 707       1     0
 708       0     1
 709       0     1
 710       0     1
 711       0     1
 
 [712 rows x 2 columns],
      C  Q  S
 0    0  0  1
 1    1  0  0
 2    0  0  1
 3    0  0  1
 4    0  0  1
 ..  .. .. ..
 707  1  0  0
 708  1  0  0
 709  0  0  1
 710  0  0  1
 711  0  0  1
 
 [712 rows x 3 columns]]

titanic_dummies = pd.concat(dummies, axis = 1)
titanic_dummies
     
1	2	3	female	male	C	Q	S
0	1	0	0	0	1	0	0	1
1	1	0	0	1	0	1	0	0
2	0	1	0	1	0	0	0	1
3	0	1	0	0	1	0	0	1
4	0	0	1	0	1	0	0	1
...	...	...	...	...	...	...	...	...
707	0	0	1	1	0	1	0	0
708	1	0	0	0	1	1	0	0
709	0	0	1	0	1	0	0	1
710	0	1	0	0	1	0	0	1
711	1	0	0	0	1	0	0	1
712 rows × 8 columns


data.drop(['Pclass', 'Sex', 'Embarked'], axis = 1)
     
PassengerId	Survived	Name	Age	SibSp	Parch	Ticket	Fare	Cabin
0	493	0	Molson, Mr. Harry Markland	55.0	0	0	113787	30.5000	C30
1	53	1	Harper, Mrs. Henry Sleeper (Myna Haxtun)	49.0	1	0	PC 17572	76.7292	D33
2	388	1	Buss, Miss. Kate	36.0	0	0	27849	13.0000	NaN
3	192	0	Carbines, Mr. William	19.0	0	0	28424	13.0000	NaN
4	687	0	Panula, Mr. Jaako Arnold	14.0	4	1	3101295	39.6875	NaN
...	...	...	...	...	...	...	...	...	...
707	859	1	Baclini, Mrs. Solomon (Latifa Qurban)	24.0	0	3	2666	19.2583	NaN
708	65	0	Stewart, Mr. Albert A	NaN	0	0	PC 17605	27.7208	NaN
709	130	0	Ekstrom, Mr. Johan	45.0	0	0	347061	6.9750	NaN
710	21	0	Fynney, Mr. Joseph J	35.0	0	0	239865	26.0000	NaN
711	476	0	Clifford, Mr. George Quincy	NaN	0	0	110465	52.0000	A14
712 rows × 9 columns


data['Age'] = data['Age'].interpolate()
print(data)
     
     PassengerId  Survived  Pclass                                      Name  \
0            493         0       1                Molson, Mr. Harry Markland   
1             53         1       1  Harper, Mrs. Henry Sleeper (Myna Haxtun)   
2            388         1       2                          Buss, Miss. Kate   
3            192         0       2                     Carbines, Mr. William   
4            687         0       3                  Panula, Mr. Jaako Arnold   
..           ...       ...     ...                                       ...   
707          859         1       3     Baclini, Mrs. Solomon (Latifa Qurban)   
708           65         0       1                     Stewart, Mr. Albert A   
709          130         0       3                        Ekstrom, Mr. Johan   
710           21         0       2                      Fynney, Mr. Joseph J   
711          476         0       1               Clifford, Mr. George Quincy   

        Sex   Age  SibSp  Parch    Ticket     Fare Cabin Embarked  
0      male  55.0      0      0    113787  30.5000   C30        S  
1    female  49.0      1      0  PC 17572  76.7292   D33        C  
2    female  36.0      0      0     27849  13.0000   NaN        S  
3      male  19.0      0      0     28424  13.0000   NaN        S  
4      male  14.0      4      1   3101295  39.6875   NaN        S  
..      ...   ...    ...    ...       ...      ...   ...      ...  
707  female  24.0      0      3      2666  19.2583   NaN        C  
708    male  34.5      0      0  PC 17605  27.7208   NaN        C  
709    male  45.0      0      0    347061   6.9750   NaN        S  
710    male  35.0      0      0    239865  26.0000   NaN        S  
711    male  35.0      0      0    110465  52.0000   A14        S  

[712 rows x 12 columns]

from sklearn.preprocessing import MinMaxScaler
data = [[-1, 1], [-0.5, 6], [0, 10], [1, 10]]
scaler = MinMaxScaler()
print(scaler.fit(data))
print(scaler.data_max_)
print(scaler.transform(data))
     
MinMaxScaler()
[ 1. 10.]
[[0.         0.        ]
 [0.25       0.55555556]
 [0.5        1.        ]
 [1.         1.        ]]

from sklearn.preprocessing import StandardScaler
d = np.asarray([[100, 0.001], [0.05, 1], [50, 0.005], [6, 1.5]])
scaler = StandardScaler()
scaled = scaler.fit_transform(scaler)
p
     
StandardScaler()
[[ 1.51898988 -0.96516257]
 [-0.97042252  0.5763201 ]
 [ 0.27366102 -0.95899047]
 [-0.82222838  1.34783294]]


     
