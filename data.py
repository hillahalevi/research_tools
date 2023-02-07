import pandas as pd

a = pd.read_parquet("/Users/hhalevi/Downloads/hashtags_all_145")
a.drop(1)
print(a.hist)
