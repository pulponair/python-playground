import pandas as pd
import random
import time

df = pd.DataFrame(random.sample(range(100), 100), columns=['Close'])

t1 = time.time()
(df.loc[1:, 'Close'] - df.shift(1).loc[1:, 'Close']) / df.shift(1).loc[1:, 'Close']
print(time.time() - t1)

t1 = time.time()
(df.pct_change())[1:]
print(time.time() - t1)
