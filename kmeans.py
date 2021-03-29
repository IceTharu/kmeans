min#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 13:20:13 2021

@author: thorsteinnj
"""
import os
chd = os.chdir('/home/thorsteinnj/Documents/Atvinnuleit/Alpaca/')

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from kmeans_functions import generating_random_clusters, generating_cluster, generating_centres, euclidean_distance, compute_new_centers, kmeans, figure_maker


number_of_clusters = 4
points = generating_cluster(number_of_clusters)

centres = generating_centres(points,number_of_clusters)

df = pd.DataFrame(points,columns=['x','y'])
df["cluster"] = 0

df, all_centres = kmeans(points,centres,df,100)


    
figure_maker(df,all_centres)


#%%

# With a completely randomly generated distribution

points, centres = generating_random_clusters(0,10000,100,number_of_clusters)


df = pd.DataFrame(points,columns=['x','y'])
df["cluster"] = 0

df, all_centres = kmeans(points,centres,df,100)

figure_maker(df,all_centres)