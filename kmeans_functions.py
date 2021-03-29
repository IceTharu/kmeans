#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 14:11:26 2021

@author: thorsteinnj
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def generating_random_clusters(min_val,max_val,points,cluster):
    """Takes in a minimum and maximum value, number of points and
    number of cluster centres to initialize."""
    """Returns some randomized points and initial cluster centres."""
    rand_x = np.random.randint(min_val,max_val,points)/100
    rand_y = np.random.randint(min_val,max_val,points)/100
    
    
    random_points = np.array([rand_x,rand_y]).T
    
    clus_cx = np.random.randint(min_val,max_val,cluster)/100
    clus_cy = np.random.randint(min_val,max_val,cluster)/100
    
    
    cluster_centers = np.array([clus_cx,clus_cy]).T
    return random_points, cluster_centers

def generating_cluster(clusters):
    """Takes in a number of intended clusters, and returns randomized
    point clusters."""
    points = []
    for i in range(clusters):
        random_points = np.random.normal(loc=[np.random.randint(0,10), np.random.randint(0,10)], scale=[np.random.random(), np.random.random()], size=(np.random.randint(50,150), 2))
        points.append(random_points)
        
    return np.concatenate(points)

def generating_centres(points,clusters):
    """Takes in the generated point cluster, and the number of clusters,
    and returns initialized cluster centres which have been chosen randomly."""
    minX = min(points[:,0])
    maxX = max(points[:,0])
    minY = min(points[:,1])
    maxY = max(points[:,1])
    centres = []
    for i in range(clusters):
        centreX = np.random.uniform(minX,maxX)
        centreY = np.random.uniform(minY,maxY)
        centre = np.array([centreX,centreY])
        centres.append(centre)
    return np.concatenate(centres).reshape(clusters,2)

def euclidean_distance(point,cluster):
    """Takes in a point, and one cluster centre.
    Returns the euclidean distance between the point and the centre."""
    euclid = np.sqrt((point[0]-cluster[0])**2+(point[1]-cluster[1])**2)
    return euclid

def compute_new_centers(clusters,df,cluster_centers):
    """Takes in number of clusters, a dataframe with the points and
    assigned cluster centres; as well as the exact cluster centres,
    and returns adjusted cluster centres."""
    for i in range(clusters):
        cluster_centers[i][0] = df.x[df.cluster == i].mean()
        cluster_centers[i][1] = df.y[df.cluster == i].mean()
        
    return cluster_centers

def kmeans(points,centres,df,iterations):
    """
    Input: Randomly generated points.
            Cluster centres.
            Dataframe with randomly generated points and assigned cluster.
            And number of iterations to run it over. """
    all_centres = []
    for k in range(iterations):
        
        cluster_num = []    
        for i in range(len(points)):
            dist = 10000
            euclids = []
            for j in range(len(centres)):
                euclids.append(euclidean_distance(points[i],centres[j]))
                min_dist = min(euclids)
            cluster = [i for i, j in enumerate(euclids) if j == min_dist][0]
            cluster_num.append(cluster)
            
        df.cluster = cluster_num
        old_centres = np.copy(centres)
        """Here we want to catch all previously computed cluster centres."""
        all_centres.append(np.copy(old_centres))
        
        centres = compute_new_centers(2,df,centres)
        if np.isnan(centres).any() == True:
            """If a a cluster has no assigned point to it, we need to stop."""
            return print("A cluster was empty!")
        
        if k>0:
            print(k)
            """We stop the iterations when we have converged."""
            if (all_centres[k-1] == all_centres[k]).all():
                
                return df, all_centres
            
def figure_maker(df,all_centres):
    """
    Input: The dataframe with points and assigned clusters.
        All computed cluster centres.
        Returns a figure with the clusters colored, and the cluster centres
        (with the initial clusters shown with an opacity of 50%"""
    clusters = np.unique(df.cluster)
    
    for i in clusters:
        plt.scatter(df.x[df.cluster == i],df.y[df.cluster == i],label=i)
        
    plt.scatter(all_centres[0][:,0],all_centres[0][:,1],color='k',marker='*',alpha=0.5)
    plt.scatter(all_centres[-1][:,0],all_centres[-1][:,1],color='k',marker='*')
    plt.title('Clusters')
    plt.legend()
    plt.show()