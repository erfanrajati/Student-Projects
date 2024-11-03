# address to find the necessary file: https://github.com/erfanrajati/LA-Crime-Analysis/blob/main/Crime_Data_from_2020_to_Present.csv


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
data = pd.read_csv("Crime_Data_from_2020_to_Present.csv")
plt.text(0.01,1.1,'made by:erfan rajati,kiarash abp , arta... ,amir reza naeemi',
         transform=plt.gca().transAxes,fontsize=12,bbox=dict(facecolor='white',alpha=0.8))
crime_types = list(set(data["Crm Cd Desc"]))
crime_counts = []
for crm in crime_types:
    count = list(data["Crm Cd Desc"]).count(crm)
    crime_counts.append(count)

temp = dict(zip(crime_types, crime_counts))

to_delete = [crm for crm, count in temp.items() if count < 11000]

for crm in to_delete:
    del temp[crm]
plt.bar(temp.keys(), temp.values())
plt.show()

# for item in temp.items():
#     with open("output.txt", 'a') as file:
#         file.write(str(item) + '\n')

# -------------------------------------------------------------------------------

# import pandas as pd
# import matplotlib.pyplot as plt

# data = pd.read_csv("Crime_Data_from_2020_to_Present.csv")
# plt.text(0.01,1.1,'made by Kiarash Akbarpour',
#          transform=plt.gca().transAxes,fontsize=12,bbox=dict(facecolor='white',alpha=0.8))
# crime_counts = data["Crm Cd Desc"].value_counts()
# crime_counts = crime_counts[crime_counts >= 11000]

# # Plot the bar chart
# plt.bar(crime_counts.index, crime_counts.values)
# plt.xticks(rotation=45)
# plt.xlabel("Crime Discription")
# plt.ylabel("Count")
# plt.title("Crime Type Distribution")
# plt.show()