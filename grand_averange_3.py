#!/usr/bin/env python
# coding: utf-8

import mne
import os.path as op
from matplotlib import pyplot as plt
import numpy as np

#open tfr
subjects = [
    '030_koal',
    '051_vlro',
    '128_godz'
]

L_freq = 15
H_freq = 25
f_step = 2
#period_start = -1.000
#period_end = 5.750
freqs = np.arange(L_freq, H_freq, f_step)
times = np.linspace(-1.000, 5.750, num = 10) 

data_path = '/net/server/data/home/vtretyakova/Desktop/Example_mne'

data = []
for sub in subjects:
    freq_file = op.join(data_path, "{0}_tfr.h5".format(sub))   
    data.append(mne.time_frequency.read_tfrs(freq_file)[0]) #why use [0]? Script does not work with out it.

#tfr_ave = mne.time_frequency.AverageTFR(info=freqs, data=data, nave=3, freqs=freqs, times = times)
#tfr_ave = mne.time_frequency.AverageTFR(data=data, nave=3)
tfr_ga = mne.grand_average(data)
tfr_ga.apply_baseline(baseline=(-0.5,-0.1), mode="logratio")

tfr_ga.save('/net/server/data/home/vtretyakova/Desktop/Example_mne/ave_tfr.h5', overwrite=True)

g_ave_topomap = tfr_ga.plot_topo(fig_facecolor='w', font_color='k', border='k');
g_ave_topomap.savefig('/net/server/data/home/vtretyakova/Desktop/Example_mne/grand_ave_for_3_subj_topomap.pdf')

mag0422 = tfr_ga.plot(['MEG0422'])
mag0422.savefig('/net/server/data/home/vtretyakova/Desktop/Example_mne/mag0422.pdf')



