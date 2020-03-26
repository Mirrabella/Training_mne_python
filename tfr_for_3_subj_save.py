#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[ ]:

#%matplotlib inline

import mne
import os.path as op
from matplotlib import pyplot as plt
import numpy as np

#load raw data
subjects = [
    '030_koal',
    '051_vlro',
    '128_godz'
]

events_stim = {
    "left_hand_stim": 2,
    "right_hand_stim": 4
}

#only for stimul
L_freq = 15
H_freq = 25
f_step = 2
baseline = (-0.5, -0.1)
period_start = -1.000
period_end = 5.750

data_path = '/net/synology/volume1/data/programs/ANYA/SPEECH_LEARN/RAW_trans/'

for sub in subjects:
    raw_file = op.join(data_path, sub,"{0}_active1_raw_tsss_bads_trans.fif".format(sub))
    raw = mne.io.Raw(raw_file, preload=True) #differents between raw and read_raw_fif?

	#choose only gradiometrs
    grad_only = raw.copy().pick_types(meg='grad')

	#crop first 29 seconds, becouse it is empty
	#grad_only = grad_only.crop(29, 2577)

	#find events
    events = mne.find_events(raw, shortest_event = 1, stim_channel='STI101')


    epochs = mne.Epochs(grad_only, events=events, event_id = events_stim, tmin = period_start, tmax = 	period_end, preload = True,  reject=dict(grad=2500e-13))

    freqs = np.arange(L_freq, H_freq, f_step)
    tfr = mne.time_frequency.tfr_multitaper(epochs, freqs = freqs, n_cycles = 8, use_fft = False, return_itc = False)


    tfr.save(op.join('/net/server/data/home/vtretyakova/Desktop/Example_mne', "{0}_tfr.h5".format(sub)), overwrite=True)


