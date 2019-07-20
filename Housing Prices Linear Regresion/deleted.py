import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('train.csv')
#plt.scatter(df['BldgType'],df['SalePrice'])
#plt.show()
plt.scatter(df['HouseStyle'],df['SalePrice'])
plt.show()
print(df.groupby(by='HouseStyle')['SalePrice'].mean())