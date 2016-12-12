#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 12.5, 25, 50, 100], dtype=np.float64)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1 , xlim=[-0.5, 100.5], ylim=[10, 1000])	#

ax.set_yscale('log')
ax.axhline(y=10, linewidth=2, color="black")
ax.axvline(x=-0.5, linewidth=2, color="black")
ax.tick_params(length=4, width=2)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('buttom')
# CH12F3
CH12F3 = np.array([78.160428, 98.82301708, 123.0165549, 99.3461206, 114.9084503, 127.0706072, \
				87.4455155, 101.9616382, 123.9319861, 68.48301287, 79.72973857, 102.6155176, \
				35.00438753, 47.55887203, 50.04361376], dtype=np.float64)
CH12F3_l = CH12F3[[i for i in range(15) if (i%3 == 0) ] ]
CH12F3_m = CH12F3[[i for i in range(15) if (i%3 == 1) ] ]
CH12F3_u = CH12F3[[i for i in range(15) if (i%3 == 2) ] ]

errbar = plt.errorbar(x, CH12F3_m, yerr=[CH12F3_m-CH12F3_l, CH12F3_u-CH12F3_m], color='blue', fmt='-o')

# 53BP1-/-
_53BP1 = np.array([87.6016572, 105.8309038, 106.567439, 101.0434249, 108.7770447, 116.3265306, \
				90.17953046, 110.2501151, 127.7428265, 78.94736842, 98.28141783, 104.5419672, \
				56.66717815, 95.33527697, 97.17661501], dtype=float64)
_53BP1_l = _53BP1[[i for i in range(15) if (i%3 == 0) ] ]
_53BP1_m = _53BP1[[i for i in range(15) if (i%3 == 1) ] ]
_53BP1_u = _53BP1[[i for i in range(15) if (i%3 == 2) ] ]

errbar1 = plt.errorbar(x, _53BP1_m, yerr=[_53BP1_m-_53BP1_l, _53BP1_u-_53BP1_m], color='green', fmt='-o')

ax.legend((errbar, errbar1),('one', 'two'))

# 53BP1-/-BRAC1-/- 
_53BP1_BRAC1 = np.array([78.42637341, 103.2817736, 118.291853, 67.61266033, 84.72092281, 91.49966833, \
					55.50775763, 74.23000714, 86.65770725, 43.56425363, 59.38132649, 72.131824, \
					16.93346769, 31.45935093, 34.04173017], dtype=float64)
_53BP1_BRAC1_l = _53BP1_BRAC1[[i for i in range(15) if (i%3 == 0) ] ]
_53BP1_BRAC1_m = _53BP1_BRAC1[[i for i in range(15) if (i%3 == 1) ] ]
_53BP1_BRAC1_u = _53BP1_BRAC1[[i for i in range(15) if (i%3 == 2) ] ]

plt.errorbar(x, _53BP1_BRAC1_m, yerr=[_53BP1_BRAC1_m-_53BP1_BRAC1_l, _53BP1_BRAC1_u-_53BP1_BRAC1_m], color='red', fmt='-o')

# ATM-/-
ATM = np.array([84.92772454, 105.3922365, 109.680039, 44.58340101, 62.51421147, 68.94591522, \
				34.4485951, 46.14260192, 46.53240214, 26.06789021, 36.78739646, 50.62530453, \
				15.34838395, 25.28828975, 25.48318987], dtype=float64)
ATM_l = ATM[[i for i in range(15) if (i%3 == 0) ] ]
ATM_m = ATM[[i for i in range(15) if (i%3 == 1) ] ]
ATM_u = ATM[[i for i in range(15) if (i%3 == 2) ] ]

plt.errorbar(x, ATM_m, yerr=[ATM_m-ATM_l, ATM_u-ATM_m], color='magenta', fmt='-o')

# H2AX-/-
H2AX = np.array([83.94714452, 107.8515177, 108.2013378, 53.39618953, 84.29696461, 91.99300671, \
				49.08174168, 73.80236175, 74.15218185, 42.43515987, 58.29367086, 59.10991775, \
				19.46364028, 32.05716371, 32.9900173], dtype=np.float64)
H2AX_l = H2AX[[i for i in range(15) if (i%3 == 0) ] ]
H2AX_m = H2AX[[i for i in range(15) if (i%3 == 1) ] ]
H2AX_u = H2AX[[i for i in range(15) if (i%3 == 2) ] ]

plt.errorbar(x, H2AX_m, yerr=[H2AX_m-H2AX_l, H2AX_u-H2AX_m], color='cyan', fmt='-o')

# Lig4-/-
Lig4 = np.array([84.46089616, 103.0126834, 112.5264204, 73.99578541, 79.54546536, 96.67019203, \
				71.77591344, 83.19239789, 97.46300346, 57.34674559, 61.46936497, 70.82453973, \
				35.62371267, 41.17339261, 44.82032515], dtype=np.float64)
Lig4_l = Lig4[[i for i in range(15) if (i%3 == 0) ] ]
Lig4_m = Lig4[[i for i in range(15) if (i%3 == 1) ] ]
Lig4_u = Lig4[[i for i in range(15) if (i%3 == 2) ] ]

plt.errorbar(x, Lig4_m, yerr=[Lig4_m-Lig4_l, Lig4_u-Lig4_m], color='black', fmt='-o')




