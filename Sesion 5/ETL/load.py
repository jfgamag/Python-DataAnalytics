import pandas as pd

def load_dw_retail(dimension, conn, df):
    df.to_sql(dimension, conn, if_exists='append', index=False)
    