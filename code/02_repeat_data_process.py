import pandas as pd
import numpy as np
df = pd.read_csv("repeat.csv")
set1 = df.values.tolist()
new = []

for n,m in enumerate(set1):

    if m[0] != '1':
        new_list = []
        new_list.extend([str(i) for i in m])
    else:
        new_list.extend([str(m[1])])
        try:
            if set1[n+1][0][0]!= '1':
                new.append(new_list)
        except:
            pass

# new.append(new_list)
# print(new[:2])
with open('info.csv','w')as f:
    for line in new:
        print(line)
 #       print(type(line))
        f.write(','.join(line)+'\n')

