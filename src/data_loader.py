import pandas as pd


def load_data():
customers = pd.read_csv('../data/raw/customers.csv')
products = pd.read_csv('../data/raw/products.csv')
orders = pd.read_csv('../data/raw/orders.csv')
return orders, customers, products


def merge_data(orders, customers, products):
df = orders.merge(customers, on='CustomerID').merge(products, on='ProductID')
return df