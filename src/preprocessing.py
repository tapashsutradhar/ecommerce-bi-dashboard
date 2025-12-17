import pandas as pd


def clean_data(df)
df['Price'].fillna(0, inplace=True)
df.drop_duplicates(subset=['CustomerID','ProductID','OrderDate'], inplace=True)
df['OrderDate'] = pd.to_datetime(df['OrderDate'])
return df