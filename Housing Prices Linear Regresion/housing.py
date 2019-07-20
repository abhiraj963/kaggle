import CleanData.cleanhousing as clean
import Model
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('train.csv')
df_test = pd.read_csv('test.csv')
y = df['SalePrice']
df.drop(['SalePrice'],axis =1, inplace= True)
df = clean.clean_data(df)
std = StandardScaler()
std.fit(df)
#print(df.head())
#plt.scatter(df['LotFrontage'],y)
#plt.show()
model = Model.mod(df,y)
#lm = LinearRegression()
#X_train, X_test, y_train, y_test = train_test_split(df,y, test_size= 0.2)
#lm.fit(df,y)
#print(model.intercept_)
#pred = model.predict(df)
df_test = clean.clean_data(df_test)
std.fit(df_test)
predictions = model.predict(df_test)
#plt.scatter(pred,y)
#plt.show(block =True)
np.savetxt('pred.csv',predictions, delimiter= ',')
