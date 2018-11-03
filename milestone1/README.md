# Milestone 1

## 1. Preprocessing
At this stage we filter the rows and characteristics, and erase the null values, all the work is here:
[1_preprocessing.py](https://github.com/RoberPlaza/MachineLearningLAB/blob/master/milestone1/1_preprocessing.py)
## 2. Normalize
In the normalizing stage we have to eliminate categorical variables and apply a normalized type. In our case it will be minMaxScaler and we also do the correlation tests and the similarity matrix here:
[2_normalize.py](https://github.com/RoberPlaza/MachineLearningLAB/blob/master/milestone1/2_normalize.py)
### 2.1 Correlations
#### Similarity matrix
![alt text](https://github.com/RoberPlaza/MachineLearningLAB/blob/master/milestone1/plots/correlation.png "Logo Title Text")
#### Heat map
![alt text](https://github.com/RoberPlaza/MachineLearningLAB/blob/master/milestone1/plots/heat_map.png "Logo Title Textt")
## 3. Clustering
And finally in clustering, we use different unsupervised learning techniques which are KMeans, DBSCAN, KMeans++, for the creation of groups, we also calculate the PCA. You can see a more detailed description in the Lab book, and here is the code:
[3_clustering.py](https://github.com/RoberPlaza/MachineLearningLAB/blob/master/milestone1/3_clustering.py)
### 3.1 PCA

## Conclusions

