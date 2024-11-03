# address to find the necessary file: https://github.com/erfanrajati/LA-Crime-Analysis/blob/main/Crime_Data_from_2020_to_Present.csv

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("Crime_Data_from_2020_to_Present.csv") 
time=list(data['TIME OCC'])

occ_hour = [str(10000 + int(i))[1:3] for i in time]
occ_set = set(occ_hour)

info = {0:0}
for h in occ_set:
    info[h] = occ_hour.count(h)

# sort_by_count = sorted(info.items(), key=lambda item:item[1])[::-1]
sort_by_hour = sorted(info.items(), key=lambda item:int(item[0]))
# for item in sort_by_count:
#     print(item)

plt.plot(
    [str(i[0]) for i in sort_by_hour], 
    [i[1] for i in sort_by_hour]
)
plt.show()


