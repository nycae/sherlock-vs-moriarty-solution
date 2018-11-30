#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import numpy
import sklearn.neighbors

from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

path_plot        = "plots/"
path_normalized  = "data/data_no_attack_normalized.csv"

def read_dataset(path):
    return pd.read_csv(path)


def calculatePCA(dataframe):
    #file = pd.read_csv(path, low_memory=False)
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

# 2.1 Setting parameters metrics
def clustering(data_norm, X_pca):
    # kmeans parameters
    init            = 'random' # initialization method

    iterations      = 10    # to run 10 times with different random centroids to choose the final model as the one with the lowest SSE
    max_iter        = 300   # maximum number of iterations for each single run
    tol             = 1e-04 # controls the tolerance with regard to the changes in the within-cluster sum-squared-error to declare convergence
    random_state    = 0     # random


    distortions     = []
    silhouettes     = []

    for i in range(2, 11):
        km = KMeans(i, init, n_init = iterations ,max_iter= max_iter, tol = tol,random_state = random_state)
        labels = km.fit_predict(data_norm)
        distortions.append(km.inertia_)
        silhouettes.append(metrics.silhouette_score(data_norm, labels))

    # Plot distoritions
    plt.subplot(211)
    plt.plot(range(2,11), distortions, marker='o')
    plt.xlabel('Number of clusters')
    plt.ylabel('Distortion')

    # Plot Silhouette
    plt.subplot(212)
    plt.plot(range(2,11), silhouettes , marker='o')
    plt.xlabel('Number of clusters')
    plt.ylabel('Silohouette')
    plt.savefig("plots/silohouette.png")
    
    # 2.2 Clustering execution
    k = 32 # from previous pictures but it is not easy to choose
    # 2.1 random inicialization
    centroids, labels, z =  sklearn.cluster.k_means(data_norm, k, init="random" )
    plot_pca(X_pca,labels, "kmeans")

    # 2.2 k-means ++
    centroidsplus, labelsplus, zplus =  sklearn.cluster.k_means(X_pca, k, init="k-means++" )
    plot_pca(X_pca, labelsplus, "kmeans++")

    # 6. characterization
    n_clusters_ = len(set(labels)) #- (1 if -1 in labels else 0)
    print('Estimated number of clusters: %d' % n_clusters_)
    print("Silhouette Coefficient: %0.3f"
          % metrics.silhouette_score(data_norm, labels))
    df['group'] = labels
    df.groupby(('group')).mean()
    
    return labels,labelsplus

if __name__ == '__main__':
    df            = read_dataset(path_normalized)
    X_pca         = calculatePCA(df)
    grupos_kmeans = clustering(df, X_pca)