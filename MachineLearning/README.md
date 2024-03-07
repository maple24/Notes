# Table of contens

- [Table of contens](#table-of-contens)
  - [Supervised and Unsupervised learning](#supervised-and-unsupervised-learning)
  - [K means Clustering](#k-means-clustering)
  - [K-Nearest Neighbors](#k-nearest-neighbors)

## Supervised and Unsupervised learning

Supervised learning is classified into two categories of algorithms:

- Classification: A classification problem is when the output variable is a category, such as “Red” or “blue” , “disease” or “no disease”.
- Regression: A regression problem is when the output variable is a real value, such as “dollars” or “weight”.

Types:

- Regression
- Logistic Regression
- Classification
- Naive Bayes Classifiers
- K-NN (k nearest neighbors)
- Decision Trees
- Support Vector Machine

## K means Clustering

We are given a data set of items, with certain features, and values for these features (like a vector). The task is to categorize those items into groups. To achieve this, we will use the kMeans algorithm; an unsupervised learning algorithm. ‘K’ in the name of the algorithm represents the number of groups/clusters we want to classify our items into.

```
Initialize k means with random values

--> For a given number of iterations:
    
    --> Iterate through items:
    
        --> Find the mean closest to the item by calculating 
        the euclidean distance of the item with each of the means
        
        --> Assign item to mean
        
        --> Update mean by shifting it to the average of the items in that cluster
```

## K-Nearest Neighbors

The k-nearest neighbors algorithm, also known as KNN or k-NN, is a non-parametric, supervised learning classifier, which uses proximity to make classifications or predictions about the grouping of an individual data point. While it can be used for either regression or classification problems, it is typically used as a classification algorithm, working off the assumption that similar points can be found near one another.

```
# in a word, find the k-th nearest neighbours, and return the majority group

Store the training samples in an array of data points arr[]. This means each element of this array represents a tuple (x, y).

for i=0 to m:
  Calculate Euclidean distance d(arr[i], p).

Make set S of K smallest distances obtained. Each of these distances corresponds to an already classified data point.

Return the majority label among S.
```
