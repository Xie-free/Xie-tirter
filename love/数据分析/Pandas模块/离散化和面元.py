import pandas as pd
import numpy as np

pd = pd.cut(np.array([1, 7, 5, 4, 6, 3, 11, 65, 99, 35]), 3)
print(pd)
