import numpy as np
import pandas as pd

df2 = pd.DataFrame(
    data=np.random.randn(4,8),
    columns=
    [('A123','open'), ('A123','high'), ('A123','low'), ('A123','close'), ('A434','open'), ('A434', 'high'), ('A434', 'low'), ('A434', 'close')],
    index=np.arange(4)
)

df2.loc[:, [('A123', 'open')]]


df2.iloc[0][('A123', 'open')]