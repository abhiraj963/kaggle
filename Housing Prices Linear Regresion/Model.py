from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor

def mod(df,y):
    clf = GradientBoostingRegressor()
    clf.fit(df,y)
    return clf