import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# A dictionary which represents data

df_cpu = pd.read_csv('cpu.csv')
df_mem = pd.read_csv('mem.csv')

cpulist = []
memlist = []

for i in range(1, len(df_cpu.values)):
    cpulist.append(df_cpu.values[i][0])
for j in range(1, len(df_mem.values)):
    memlist.append(df_mem.values[j][0])

data_dict = {'time': range(1, len(cpulist)+1),
             'cpu_util': cpulist,
             'mem_util': memlist
             }

df = pd.DataFrame(data_dict)
# show the dataframe
# bydefault head() show
# first five rows from top
print(df.head(n=50))
# Get current axis
ax = plt.gca()

# line plot for math marks
df.plot(kind='line',
        x='time',
        y='cpu_util',
        color='blue', ax=ax)

# line plot for physics marks
df.plot(kind='line', x='time',
        y='mem_util',
        color='red', ax=ax)

# line plot for chemistry marks


# set the title
plt.title('CPU & MEM use')

# show the plot
plt.show()
