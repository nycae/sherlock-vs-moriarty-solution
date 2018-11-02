import pandas as pd
import matplotlib.pyplot as plt
import numpy
import sklearn.neighbors

from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.decomposition import PCA
from sklearn.neighbors import kneighbors_graph

"""
## 3. Clustering

Let's then run a hierarchical clustering algorithm (it will take a while) to see how the data is distributed.
Since the data is so concentrated and the rest seems outlier it is best not to use Single-Link.
The options would range from Complete-Link to Ward.
The Complete-Link will allow us to break up the big groups.
"""

path_in     = "data/data_norm.csv"
path_copy   = "data/data_norm_copy.csv"

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
    numbers = numpy.arange(len(X_pca))
    fig, ax = plt.subplots()

    for i in range(len(X_pca)):
        plt.text(X_pca[i][0], X_pca[i][1], numbers[i])

    plt.xlim(-1, 1.5)
    plt.ylim(-1, 1.5)
    ax.grid(True)
    fig.tight_layout()
    #plt.show()
    return X_pca


def plot_pca(X_pca, labels):

    colors      = numpy.array([x for x in 'bgrcmykbgrcmykbgrcmykbgrcmyk'])
    colors      = numpy.hstack([colors] * 20)
    numbers     = numpy.arange(len(X_pca))
    fig, ax     = plt.subplots()

    for i in range(len(X_pca)):
        plt.text(X_pca[i][0], X_pca[i][1], numbers[i], color=colors[labels[i]])

    plt.xlim(-1, 4)
    plt.ylim(-0.2, 1)
    ax.grid(True)
    fig.tight_layout()
    plt.show()

# 2.1 Setting parameters metrics
def clustering(data_norm, X_pca):
    from sklearn import metrics
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
    plt.show()

    # Plot Silhouette
    plt.subplot(212)
    plt.plot(range(2,11), silhouettes , marker='o')
    plt.xlabel('Number of clusters')
    plt.ylabel('Silohouette')
    plt.show()

    # 2.2 Clustering execution
    k = 6 # from previous pictures but it is not easy to choose
    # 2.1 random inicialization
    centroids, labels, z =  sklearn.cluster.k_means(data_norm, k, init="random" )
    plot_pca(X_pca,labels)

    # 2.2 k-means ++
    centroidsplus, labelsplus, zplus =  sklearn.cluster.k_means(X_pca, k, init="k-means++" )
    plot_pca(X_pca, labelsplus)

    # 6. characterization
    n_clusters_ = len(set(labels)) #- (1 if -1 in labels else 0)
    print('Estimated number of clusters: %d' % n_clusters_)
    print("Silhouette Coefficient: %0.3f"
          % metrics.silhouette_score(data_norm, labels))
    df['group'] = labels
    df.groupby(('group')).mean()

def calculate_clustering_db_scan(data):
    # 1. Compute de similarity/ distance matrix
    dist = sklearn.neighbors.DistanceMetric.getmetric('euclidean')
    matsim = dist.pairwise(data)
    
    minPts = 10
    
    # 2. Compute the k-nearest neightbors
    A = kneighbors_graph(data, minPts, include_self=False)
    Ar = A.toarray()

    seq = []
    for i,s in enumerate(data):
        for j in range(len(data)):
            if Ar[i][j] != 0:
                seq.append(matsim[i][j])
            
    seq.sort()
    plt.plot(seq)
    plt.show()
            
    
    # 3. Execute clustering
    labels = DBSCAN(eps= 0.08, min_samples = minPts).fit_predict(data)
    
    # 4. Plot the results
    plotdata(data, labels, 'dbscan')
    
    # 5. Validation
    print ("Silhouette Coefficient : %0.3f" % metrics.silhouette_score(numpy.asarray(data),labels))
    
    
def plotdata(data, labels, name):
    fig, ax = plt.subplots()
    plt.scatter([row[0] for row in data], [row[1] for row in data], c = labels)
    ax.grid(True)
    fig.tight_layout()
    plt.title(name)
    plt.show()

if __name__ == '__main__':

    df = read_dataset(path_copy)
    X_pca = calculatePCA(df)
    clustering(df, X_pca)
    
    calculate_clustering_db_scan(df)
    