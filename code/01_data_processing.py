import pandas as pd
import numpy as np
#sort
df = pd.read_csv("total_stand.csv")
df.sort_values(by='smiles',inplace=True,ascending=False)
print(df)
r = np.array(df)
df = pd.DataFrame(r)
df.to_csv('total_stand_sort.csv')

#Filter out duplicate data
import pandas as pd
import numpy as np
df = pd.read_csv("total_stand_sort.csv")

#delete duplicate data
total_drop = df.drop_duplicates(subset=['smiles'],keep=False)
r = np.array(total_drop)
df = pd.DataFrame(r)
df.to_csv('total_stand_drop1.csv')

#Merge the two tables and remove duplicates, retaining the intersection
df1 = pd.read_csv("total_stand_sort.csv")
df2 = pd.read_csv("total_stand_drop1.csv")
set1 = df1.values.tolist()  
set2 = df2.values.tolist()
tmp = [val for val in set1 if val not in set2]  
r = np.array(tmp)
df = pd.DataFrame(r)
df.to_csv('total_stand_repeat.csv')

#delete repeat smiles in total_stand_repeat.csv and calculate the average
df = pd.read_csv("total_stand_repeat.csv")
drop = df.drop_duplicates(subset=['smiles'],keep='first')
r = np.array(drop)
df = pd.DataFrame(r)
df.to_csv('repeat.csv')


