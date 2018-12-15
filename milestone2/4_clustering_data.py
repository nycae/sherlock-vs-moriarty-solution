#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import numpy
import sklearn.neighbors

import sklearn.cluster
from sklearn import metrics
from sklearn.decomposition import PCA

path_plot                 = "plots/"
path_normalized           = "data/data_no_attack_normalized.csv"
path_centroids_no_attacks = "data/data_no_attack_centroids.csv"

def read_dataset(path):
    return pd.read_csv(path)


def calculatePCA(dataframe):

    estimator = PCA (n_components = 2)
    X_pca = estimator.fit_transform(dataframe)

    #Print
    print(estimator.explained_variance_ratio_)
    pd.DataFrame(numpy.matrix.transpose(estimator.components_),
    columns=['PC-1', 'PC-2'], index=dataframe.columns)

    #Print
    fig, ax = plt.subplots()

    for i in range(len(X_pca)):
        plt.text(X_pca[i][0], X_pca[i][1], ".")

    plt.xlim(-1, 1.5)
    plt.ylim(-1, 1.5)
    ax.grid(True)
    fig.tight_layout()
    plt.savefig(path_plot+"pca.png")
    return X_pca


def plot_pca(X_pca, labels, type_clus):

    colors      = numpy.array([x for x in 'bgrcmykbgrcmykbgrcmykbgrcmyk'])
    colors      = numpy.hstack([colors] * 20)
    fig, ax     = plt.subplots()
    save_path   = path_plot+"clustering_{}_pca.png".format(type_clus)

    for i in range(len(X_pca)):
        plt.text(X_pca[i][0], X_pca[i][1], '.', color=colors[labels[i]])

    plt.xlim(-1, 1)
    plt.ylim(-0.5, 0.8)
    ax.grid(True)
    fig.tight_layout()
    
    plt.savefig(save_path)

def clustering(data_norm, X_pca):

    # 1.0 Clustering execution
    k = 36 # one attack for each no attack

    # 1.1 k-means ++
    centroidsplus, labelsplus, zplus =  sklearn.cluster.k_means(data_norm, k, init="k-means++" )
#    plot_pca(X_pca, labelsplus, "kmeans++")

    # Characterization
    n_clusters_ = len(set(labelsplus)) #- (1 if -1 in labels else 0)
    print('Estimated number of clusters: %d' % n_clusters_)
    print("Silhouette Coefficient: %0.3f"
          % metrics.silhouette_score(data_norm, labelsplus))
    df['group'] = labelsplus
    df.groupby(('group')).mean()
    
    return centroidsplus

def to_csv(path,dataframe):
    numpy.savetxt(path, dataframe, delimiter=",")
    
if __name__ == '__main__':
    
    df            = read_dataset(path_normalized)
    df.drop(df.columns[[13]], axis=1, inplace=True)

#    X_pca                   = calculatePCA(df)
    X_pca = 20
    df_centroids            = clustering(df, X_pca)

    print(df_centroids)
    to_csv(path_centroids_no_attacks,df_centroids)   
    
    