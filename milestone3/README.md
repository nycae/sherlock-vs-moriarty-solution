# Milestone 3
## What is the problem?

The main problem with this milestone is to finalize the model and draw the appropriate conclusions from the project.

![alt text](https://github.com/RoberPlaza/MachineLearningLAB/blob/development/resources/img/problem2.png)

We have divided the work into six .py files so we describe them below

## 1. Dataset description
The description of the dataset and the features are the same as in milestone 2, we will use data from T2.csv.

## 2. Pre-processing, cleaning and clustering
In this section we follow the same line that we took in the previous milestone, it should be noted that they have learned from the errors of the previous code, the presentation has been improved and the code has become more efficient.

## Random forest
This is the file where we use the random forest:
  * [5_random_forest.py](https://github.com/RoberPlaza/MachineLearningLAB/blob/development/milestone3/5_random_forest.py)

## Decision tree
This is the file where we use decision trees:
  * [6_decision_tree.py](https://github.com/RoberPlaza/MachineLearningLAB/blob/development/milestone3/6_decision_tree.py)
  
## Decision Birch 
<p align="center">
  <img width="400" height="300" src="https://github.com/RoberPlaza/MachineLearningLAB/blob/master/milestone3/trees/decision_birch.png">
</p>

## Conclusions
Giroscope rotation and Magnetic field is oddly important, is the most weighted one in order to predict attacks. Perhaps it's due to high resource consumption, or perhaps it's because the virus attacks when the user is in a phone call. Thinking it carefully we could study if the virus attack is ordered using low wave spectrum as the main channel, sounds like an interesting idea.
