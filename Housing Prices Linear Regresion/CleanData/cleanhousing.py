import pandas as pd
def clean_data(df):
    def Pool(col):
        if col == 'Ex':
            return 5
        elif col == 'Fa':
            return 2
        elif col == 'Gd':
            return 4
        elif col == 'TA':
            return 3
        elif col == 'Po':
            return 1
        else:
            return 0

    df['PoolQC'] = df['PoolQC'].apply(Pool)

    df['LotFrontage'].fillna(value=0, inplace=True)

    msZoning = pd.get_dummies(df['MSZoning'], drop_first=True)
    street = pd.get_dummies(df['Street'], drop_first=True)
    df.drop(['MSZoning'], inplace=True, axis=1)
    df = pd.concat([df, msZoning, street], axis=1)
    df.drop(['Street'], inplace=True, axis=1)
    alley = pd.get_dummies(df['Alley'])
    df = pd.concat([df, alley], axis=1)
    df.drop(['Alley'], inplace=True, axis=1)
    df = pd.get_dummies(data=df, columns=['LotConfig', 'Neighborhood', 'SaleCondition'], drop_first=True)
    def utility(col):
        if col == 'AllPub':
            return 4
        elif col == 'NoSewr':
            return 3
        elif col == 'NoSeWa':
            return 2
        elif col == 'ELO':
            return 1
        else:
            return 0

    df['Utilities'] = df['Utilities'].apply(utility)
    def building(col):
        if col == '1Fam':
            return 5
        elif col == '2fmCon':
            return 1
        elif col == 'Duplex':
            return 2
        elif col == 'Twnhs':
            return 3
        else:
            return 4

    df['BldgType'] = df['BldgType'].apply(building)
    #df1 = pd.read_csv('train.csv')
    #df['HouseStyle'] = df['HouseStyle'].apply(lambda x : (df1.groupby(by='HouseStyle')['SalePrice'].mean()[x])/1000)
    #df.drop(['BldgType'],inplace=True,axis=1)
    df = pd.get_dummies(data=df, columns=['Condition1', 'RoofStyle','CentralAir'], drop_first=True)
    df.drop(['Condition2','HouseStyle'], axis=1, inplace=True)
    def roof(col):
        if col == 'ClyTile':
            return 8
        elif col == 'CompShg':
            return 7
        elif col == 'Membran':
            return 6
        elif col == 'Metal':
            return 5
        elif col == 'Roll':
            return 4
        elif col == 'Tar&Grv':
            return 3
        elif col == 'WdShake':
            return 2
        elif col == 'WdShngl':
            return 1
        else:
            return 0

    df['RoofMatl'] = df['RoofMatl'].apply(roof)
    df.drop(['Exterior2nd', 'Exterior1st', 'MasVnrType'], inplace=True, axis=1)
    df['ExterQual'] = df['ExterQual'].apply(Pool)
    df['ExterCond'] = df['ExterCond'].apply(Pool)
    df['BsmtQual'] = df['BsmtQual'].apply(Pool)
    df['BsmtCond'] = df['BsmtCond'].apply(Pool)
    df['HeatingQC'] = df['HeatingQC'].apply(Pool)
    df['FireplaceQu'] = df['FireplaceQu'].apply(Pool)
    df['KitchenQual'] = df['KitchenQual'].apply(Pool)
    df['GarageQual'] = df['GarageQual'].apply(Pool)
    df['GarageCond'] = df['GarageCond'].apply(Pool)

    def fence(col):
        if col == 'GdPrv':
            return 5
        elif col == 'MnPrv':
            return 4
        elif col == 'GdWo':
            return 3
        elif col == 'MnWw':
            return 2
        else:
            return 0

    df['Fence'] = df['Fence'].apply(fence)
    df.drop(['MiscFeature'], axis=1, inplace=True)
    df.drop(['SaleType'], axis=1, inplace=True)

    def foundation(col):
        if col == 'BrkTil':
            return 6
        elif col == 'CBlock':
            return 5
        elif col == 'PConc':
            return 4
        elif col == 'Slab':
            return 3
        elif col == 'Stone':
            return 2
        elif col == 'Wood':
            return 1
        else:
            return 0

    df['Foundation'] = df['Foundation'].apply(foundation)

    def basement(col):
        if col == 'GLQ':
            return 6
        elif col == 'ALQ':
            return 5
        elif col == 'BLQ':
            return 4
        elif col == 'Rec':
            return 3
        elif col == 'LwQ':
            return 2
        elif col == 'Unf':
            return 1
        else:
            return 0

    df['BsmtFinType1'] = df['BsmtFinType1'].apply(basement)
    df['BsmtFinType2'] = df['BsmtFinType2'].apply(basement)
    def exposure(col):
        if col == 'Gd':
            return 4
        elif col == 'Av':
            return 3
        elif col == 'Mn':
            return 2
        elif col == 'No':
            return 1
        else:
            return 0


    df['BsmtExposure'] = df['BsmtExposure'].apply(exposure)

    def shape(col):
        if col == 'Reg':
            return 4
        elif col == 'IR1':
            return 3
        elif col == 'IR2':
            return 2
        elif col == 'IR3':
            return 1
        else:
            return 0


    df['LotShape'] = df['LotShape'].apply(shape)

    def contour(col):
        if col == 'Lvl':
            return 4
        elif col == 'Bnk':
            return 3
        elif col == 'HLS':
            return 2
        elif col == 'Low':
            return 1
        else:
            return 0


    df['LandContour'] = df['LandContour'].apply(contour)

    def slope(col):
        if col == 'Gtl':
            return 4
        elif col == 'Mod':
            return 3
        elif col == 'Sev':
            return 2
        else:
            return 0


    df['LandSlope'] = df['LandSlope'].apply(slope)

    def heating(col):
        if col == 'Floor':
            return 6
        elif col == 'GasA':
            return 5
        elif col == 'GasW':
            return 4
        elif col == 'Grav':
            return 3
        elif col == 'OthW':
            return 2
        elif col == 'Wall':
            return 1
        else:
            return 0


    df['Heating'] = df['Heating'].apply(heating)

    def electrical(col):
        if col == 'SBrkr':
            return 5
        elif col == 'FuseA':
            return 4
        elif col == 'FuseF':
            return 3
        elif col == 'FuseP':
            return 2
        elif col == 'Mix':
            return 1
        else:
            return 0


    df['Electrical'] = df['Electrical'].apply(electrical)

    def functional(col):
        if col == 'Typ':
            return 8
        elif col == 'Min1':
            return 7
        elif col == 'Min2':
            return 6
        elif col == 'Mod':
            return 5
        elif col == 'Maj1':
            return 4
        elif col == 'Maj2':
            return 3
        elif col == 'Sev':
            return 2
        elif col == 'Sal':
            return 1
        else:
            return 0


    df['Functional'] = df['Functional'].apply(functional)

    def garagetype(col):
        if col == '2Types':
            return 6
        elif col == 'Attchd':
            return 5
        elif col == 'Basment':
            return 4
        elif col == 'BuiltIn':
            return 3
        elif col == 'CarPort':
            return 2
        elif col == 'Detchd':
            return 1
        else:
            return 0


    df['GarageType'] = df['GarageType'].apply(garagetype)

    def garagefin(col):
        if col == 'Fin':
            return 3
        elif col == 'RFn':
            return 2
        elif col == 'Unf':
            return 1
        else:
            return 0


    df['GarageFinish'] = df['GarageFinish'].apply(garagefin)

    def paved(col):
        if col == 'Y':
            return 3
        elif col == 'P':
            return 2
        elif col == 'N':
            return 1
        else:
            return 0


    df['PavedDrive'] = df['PavedDrive'].apply(paved)

    def sale(col):
        if col == 'Normal':
            return 6
        elif col == 'Abnorml':
            return 5
        elif col == 'Basment':
            return 4
        elif col == 'BuiltIn':
            return 3
        elif col == 'CarPort':
            return 2
        elif col == 'Detchd':
            return 1
        else:
            return 0


    df['GarageType'] = df['GarageType'].apply(garagetype)

    df.fillna(value=0, inplace=True)
    
    return df