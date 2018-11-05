# Milestone 1
## What is the problem?
Analize the routine of an iranian citizen via movile phone ir order to learn about how to perform unsupervised learning

![alt text](https://github.com/RoberPlaza/MachineLearningLAB/blob/master/resources/img/problem.png)

We have divided the work into three .py files so we describe them below

## 1. Dataset Description
The dataset represents the value of the sensors of the smartphone of one man over a period of time.
The lectures are taken once every 20 seconds.
## 2. Preprocessing
At this stage we filter the rows and characteristics, and erase the null values, all the work is here:
[1_preprocessing.py](https://github.com/RoberPlaza/MachineLearningLAB/blob/master/milestone1/1_preprocessing.py)
## 3. Normalize
In the normalizing stage we have to eliminate categorical variables and apply a normalized type. In our case it will be minMaxScaler and we also do the correlation tests and the similarity matrix here:
[2_normalize.py](https://github.com/RoberPlaza/MachineLearningLAB/blob/master/milestone1/2_normalize.py)
### 3.1 Correlations
#### Similarity matrix
![alt text](https://github.com/RoberPlaza/MachineLearningLAB/blob/master/milestone1/plots/correlation.png "Logo Title Text")
#### Heat map
![alt text](https://github.com/RoberPlaza/MachineLearningLAB/blob/master/milestone1/plots/heat_map.png "Logo Title Textt")
## 4. Clustering
And finally in clustering, we use different unsupervised learning techniques which are KMeans, DBSCAN, KMeans++, for the creation of groups, we also calculate the PCA. You can see a more detailed description in the Lab book, and here is the code:
[3_clustering.py](https://github.com/RoberPlaza/MachineLearningLAB/blob/master/milestone1/3_clustering.py)
### 4.1 PCA
![alt_text](https://github.com/RoberPlaza/MachineLearningLAB/blob/master/milestone1/plots/pca.png)
### 4.2 KMeans
![alt_text](https://github.com/RoberPlaza/MachineLearningLAB/blob/master/milestone1/plots/clustering_kmeans_pca.png)
### 4.3 KMeans++
![alt_text](https://github.com/RoberPlaza/MachineLearningLAB/blob/master/milestone1/plots/clustering_kmeans%2B%2B_pca.png)
### 4.4 DBSCAN
![alt_text](https://github.com/RoberPlaza/MachineLearningLAB/blob/master/milestone1/plots/clustering_dbscan_pca.png)
## Conclusions
Given that the linear acceleration in the Z axis is the variable that influences the dataset the most we can guess that the 5 clusters means 5 displacement patterns over the transcourse of the time period the project took place.
