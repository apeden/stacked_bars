"""
=================
Stacked Bar Graph
=================

This is an example of creating a stacked bar plot with error bars
using `~matplotlib.pyplot.bar`.  Note the parameters *yerr* used for
error bars, and *bottom* to stack the bars on top of each other.
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#data from Copy%20of%20CDI_2313.004%20Collation%20(1).xlsx

 
brain_results = {"labels":('FFI case 1', 'FFI case 2', 'vCJD FC','vCJD thal', 'sCJD MM1 FC', 'sCJD MM1 Th', "sCJD MM2T FC", "sCJD MM2C Th"),
                 "resPrPSc":(0.03632391854361572, 0.011603473979211762, 255.9755260750229, 811.2243954743768, 66.67804534377764, 425.2746610186009, 36.67000554219439, 8.953835150833408),# val after digestion with 50ug/ml PK
                 "senPrPSc":(10.158619888586296, 17.15144803787777, 264.75297346752046, 622.5828218590547, 321.4260740631576, 240.10343236939386, 131.04493245132778, 9.471136987775695), # val after digestion with 2.5ug/ml PK minus value after digestion with 50ug/ml
                 "resStd":(0.0032695263504265246, 0.05973147296593388, 22.299421011866396, 58.5209758282598, 5.954675158511161, 45.38269792579953, 2.0252854619742, 0.2629892667077108),
                 "senStd":(0.5793248032987457, 1.680742959295882, 87.65763624791052, 49.56795161238866, 40.31280991143169, 61.888749313890365, 13.904239278745587, 0.7667624619943259)}

pmca_results = {"labels":('case 1','case 2','PMCA case 1','PMCA case 2'),
                 "resPrPSc":(0.03632391854361572, 0.011603473979211762, 0.4690770007938217, 0.309142222976386),# val after digestion with 50ug/ml PK
                 "senPrPSc":(10.158619888586296, 17.15144803787777, 28.083181687858016, 8.047449917984666), # val after digestion with 2.5ug/ml PK minus value after digestion with 50ug/ml
                 "resStd":(0.0032695263504265246, 0.05973147296593388, 0.08002683096621434, 0.06486443244926617),
                 "senStd":(0.5793248032987457, 1.680742959295882, 3.832876692091353, 1.8732440249348945)}


sFI_FFI_results = {"labels":('FFI case 1', 'FFI case 2', "sCJD MM2T FC"),
                 "resPrPSc":(0.03632391854361572,  0.011603473979211762, 36.67000554219439),# val after digestion with 50ug/ml PK
                 "senPrPSc":(10.158619888586296,  17.15144803787777,  131.04493245132778), # val after digestion with 2.5ug/ml PK minus value after digestion with 50ug/ml
                 "resStd":(0.0032695263504265246,  0.05973147296593388,  2.0252854619742),
                 "senStd":(0.5793248032987457, 1.680742959295882,  13.904239278745587)}

##df = pd.DataFrame(brain_results)
##title = 'resPrPSc vs senPrPSc for various PDs'
##maxval, markers = 1700, 100

df = pd.DataFrame(brain_results)
title = 'resPrPSc vs senPrPSc for before and after PMCA'
maxval, markers = 2100, 100
print(df)
N = len(df)
print(N)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence
p1 = plt.bar(ind, df["resPrPSc"], width, yerr=df["resStd"])
p2 = plt.bar(ind, df["senPrPSc"], width,
             bottom = df["resPrPSc"], yerr = df["senStd"])

plt.ylabel(chr(956)+"gPrPSc/gram brain")
#plt.title(title)
plt.xticks(ind, df["labels"])
plt.yticks(np.arange(0, maxval, markers))
plt.legend((p2[0], p1[0]), ('senPrPSc', 'resPrPSc'), loc = "upper left")
plt.show()
