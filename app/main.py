# test file to read and understand how this evnironment works

import pandas as pd 
from matplotlib import pyplot as plt

path_articles = "/home/baursafi/code/kaggle/hm-competition/data/articles.csv"
df_articles = pd.read_csv(path_articles)
df_transactions = pd.read_csv("/home/baursafi/code/kaggle/hm-competition/data/transactions_train.csv")
df_customers = pd.read_csv("/home/baursafi/code/kaggle/hm-competition/data/customers.csv")

df_transactions['t_dat'] = pd.to_datetime(df_transactions.t_dat)
df_transactions['doweek'] = df_transactions.t_dat.dt.dayofweek
df_transactions['weekofyear'] = df_transactions.t_dat.dt.isocalendar().week

df_trans_by_date = df_transactions.groupby(['t_dat', 'doweek', 'weekofyear']).agg({
    'customer_id': 'nunique',
    'article_id': ['nunique', 'count'],
    'price': 'sum'
}).reset_index(drop=False)
df_trans_by_date.columns = ['time','dayofweek','weekofyear', 'customers', 'items', 'orders', 'revenue']

# build a graph
time_ = df_trans_by_date['time']
# plt.subplot(211)
plt.plot(time_, df_trans_by_date['customers'], 'r--')
df_trans_by_date[df_trans_by_date.customers > 20000]
test = df_trans_by_date[df_trans_by_date.customers > df_trans_by_date.customers.mean() +2*  df_trans_by_date.customers.std()]