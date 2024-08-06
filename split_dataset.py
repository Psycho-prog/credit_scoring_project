import pandas as pd

df = pd.read_csv('/Users/bad_boy/Zypl final project/credit_scoring_project/source/test.csv')

customers = df[['customer_id', 'name', 'email']].drop_duplicates()
customers.to_csv('source/customers.csv', index=False)

orders = df[['order_id', 'customer_id', 'order_date', 'order_amount']].drop_duplicates()
orders.to_csv('source/orders.csv', index=False)

products = df[['product_id', 'product_name', 'product_price']].drop_duplicates()
products.to_csv('source/products.csv', index=False)

print("Данные успешно разделены и сохранены в файлы .csv")