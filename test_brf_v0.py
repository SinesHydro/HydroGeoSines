import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import hydrogeosines as hgs

#%% test the model
hgs = hgs.site('TEST', geoloc=[141.762065, -31.065781, 160])

fg_data = hgs.data.import_csv('test_data/fowlers_gap/acworth_short.csv', dt_fmt='%d/%m/%Y %H:%M')
print(fg_data)

timefloat = hgs.data.tf.values
data = hgs.data.all['{BP}'].values
data1, result1 = hgs.model.lin_window_ovrlp(timefloat, data)
data2, result2 = hgs.model.hals(timefloat, data1, freqs='AT')

#%% 
heads = hgs.data.correct_heads(locs=['Smith'])
# heads = hgs.data.correct_heads()
print(heads)

#%%
# new_t = pd.date_range(start='2014-10-21 00:00', end='2016-05-18 05:15', freq='15min').to_series()
# new_t.to_csv('time.csv')
