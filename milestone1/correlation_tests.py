#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 17:05:54 2018

@author: lajotadeladerrota
"""

from numpy import corrcoef, transpose, arange
from pylab import pcolor, show, colorbar, xticks, yticks
import numpy as np
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt


# 0. Load Data
df = pd.read_csv("data_norm.csv")



# plotting the correlation matrix
#http://glowingpython.blogspot.com.es/2012/10/visualizing-correlation-matrices.html
R = corrcoef(transpose(df))
pcolor(R)
colorbar()
yticks(arange(0,40),range(0,40))
xticks(arange(0,40),range(0,40))
show()


sns.set(style="white")
mask = np.zeros_like(R, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True
