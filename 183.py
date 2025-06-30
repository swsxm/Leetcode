import pandas as pd


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged = customers.merge(orders, left_on="id", right_on="customerId", how="left")
    no_orders = merged[merged["customerId"].isna()]
    return no_orders[["name"]].rename(columns={"name": "Customers"})
