import pandas as pd
import numpy as np
import math
panda_data = pd.read_csv('./csv_result-KDDTrain+ .csv')
copy_panda=panda_data.copy()
for columns in panda_data.columns:
    if panda_data[columns].dtype =='object':
        copy_panda = copy_panda.drop(columns, axis=1)
    else:
        varianceValue = np.var(panda_data[columns])
        if varianceValue < 0:
            copy_panda = copy_panda.drop(columns, axis=1)

#print(copy_panda.head())
print(list(copy_panda.head(0)))
