import pandas as pd
import matplotlib.pyplot as plt

# import the data
df = pd.read_csv('data/ckd.csv')

# plot blood pressure as a function of age
plt.figure()
plt.scatter(df['Age'], df['Blood Pressure'])
plt.xlabel('Age')
plt.ylabel('Blood Pressure')
plt.show()