import pandas as pd
import numpy as np

# document http://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#the-query-method
n = 100
df = pd.DataFrame(np.random.rand(n, 3), columns=list('abc'))

print(df)
df1 = df[(df.a < df.b) & (df.b < df.c)]
df2 = df.query('(a < b) & (b < c)')
pass
