# Milestone 2
## What is the problem?

The main problem with this milestone is a model, and we will try to teach you so that you will be able to predict Moriarty's attacks.

![alt text](https://github.com/RoberPlaza/MachineLearningLAB/blob/development/resources/img/problem2.png)

We have divided the work into six .py files so we describe them below

## 1. Dataset description
The description of the dataset and the features are the same as in milestone 2, we will use data from T2.csv.
## 2. Labeling Moriarty
So we try, by an advice, to make a more efficient method than Hadoop and Pig, based on a route about the 187 elements, and via pandas accesing to the dataset, changing an adding row called "attack" from 0 to 1 if its verified that the UUID from moriarty falls in a range between the element's UUID from the dataset to label - the time that tooks sherlock to make a lecture  and the element's UUID itself. We also need to prepossess a little bit moriarty, because it has some columns with the character "," and can be troubled.
  * [1_moriarty_labelling.py](https://github.com/RoberPlaza/MachineLearningLAB/blob/development/milestone2/1_moriarty_labeling.py)
## 3. Cleaning data
To build the model, we have to combine data from Moriarty and Sherlock, we have followed a process by which we perform a general cleaning of Moriarty data, following a preprocessed, a normalized and running a clustering to group the non-attacks in 36 groups, to catch each centroid. All this process is done to correspond the 36 attacks with the non-attacks.

<p align="center">
  <img width="400" height="300" src="https://github.com/RoberPlaza/MachineLearningLAB/blob/development/milestone2/plots/clustering_kmeans%2B%2B_pca.png">
</p>

This whole process will be executed in the following scripts:
  * [2_preprocessing_data.py](https://github.com/RoberPlaza/MachineLearningLAB/blob/development/milestone2/2_preprocessing_data.py)
  * [3_normalize_data.py](https://github.com/RoberPlaza/MachineLearningLAB/blob/development/milestone2/3_normalize_data.py)
  * [4_clustering_data.py](https://github.com/RoberPlaza/MachineLearningLAB/blob/development/milestone2/4_clustering_data.py)

## 4. Building model
First we mix well the dataset of the centroids with that of the attacks, and we make the rows to be random.
Now we have a completely balance dataset in order to start looking for a model with differ-
ent algorithms.
The selected distribution for this dataframe was a 33/66 distribution between testing-training.
The algorithm we chose to apply was a random forest search after a few minutes of discussion.

  * [5_build_model.py](https://github.com/RoberPlaza/MachineLearningLAB/blob/development/milestone2/5_build_model.py)
  * [6_random_forest.py](https://github.com/RoberPlaza/MachineLearningLAB/blob/development/milestone2/6_random_forest.py)
  
After several attempts to parameterize, we do not know why spyder did not leave us and we
would see enough bugs, so simply for this milestone we decided to implement the model as it is
and train it.
## Conclusions
With quite good results, but we do not rule out that when facing a real environment, our model is
quite weak, although in principle remain faithful to our first preprocess in this subject, keeping
much of the decisions we make, this model is quite good.
And in the case,  that it isn’t a good model for our porpouse,  we can use it to make a better
feature selection for future models and solutions.
