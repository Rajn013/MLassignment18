#!/usr/bin/env python
# coding: utf-8

# 1. What is the difference between supervised and unsupervised learning? Give some examples to illustrate your point.
# 

# The main difference between supervised and unsupervised learning: Labeled data. The main distinction between the two approaches is the use of labeled datasets. To put it simply, supervised learning uses labeled input and output data, while an unsupervised learning algorithm does not

# 2. Mention a few unsupervised learning applications.
# 

# Products Segmentation.
# Customer Segmentation.
# Similarity Detection.
# Recommendation Systems.
# Labelling unlabelled datasets.

# 3. What are the three main types of clustering methods? Briefly describe the characteristics of each.
# 

# Connectivity-based Clustering (Hierarchical clustering)
# Centroids-based Clustering (Partitioning methods)     
# Distribution-based Clustering
# 
# Connectivity-based Clustering (Hierarchical clustering)
# Hierarchical clustering, also known as connectivity-based clustering, is based on the principle that every object is connected to its neighbors depending on their proximity distance (degree of relationship). The clusters are represented in extensive hierarchical structures separated by a maximum distance required to connect the cluster parts. 
# 
# Centroids-based Clustering (Partitioning methods)     
# Centroid-based clustering is the easiest of all the clustering types in data mining. It works on the closeness of the data points to the chosen central value. The datasets are divided into a given number of clusters, and a vector of values references every cluster
# 
# 
# Distribution-based Clustering
# Density-based clustering method considers density ahead of distance. Data is clustered by regions of high concentrations of data objects bounded by areas of low concentrations of data objects. The clusters formed are grouped as a maximal set of connected data points.

# 4. Explain how the k-means algorithm determines the consistency of clustering.
# 

# K-means is a centroid-based clustering algorithm, where we calculate the distance between each data point and a centroid to assign it to a cluster. The goal is to identify the K number of groups in the dataset.

# 5. With a simple illustration, explain the key difference between the k-means and k-medoids algorithms.
# 

# K-means attempts to minimize the total squared error, while k-medoids minimizes the sum of dissimilarities between points labeled to be in a cluster and a point designated as the center of that cluster. In contrast to the k -means algorithm, k -medoids chooses datapoints as centers ( medoids or exemplars).

# 6. What is a dendrogram, and how does it work? Explain how to do it.
# 

# A dendrogramis a diagram representing a tree. The figure factory called create_dendrogram performs hierarchical clustering on data and represents the resulting tree. Values on the tree depth axis correspond to distances between clusters.
# 
# Dendrogram plots are commonly used in computational biology to show the clustering of genes or samples, sometimes in the margin of heatmaps.

# 7. What exactly is SSE? What role does it play in the k-means algorithm?
# 

# Sum of Squared Errors (SSE): This measures the sum of the squared distances between each data point and its assigned centroid. Silhouette Coefficient: This measures the similarity of a data point to its own cluster compared to other clusters

# 8. With a step-by-step algorithm, explain the k-means procedure.
# 

# Decide how many clusters you want, i.e. choose k
# Randomly assign a centroid to each of the k clusters
# Calculate the distance of all observation to each of the k centroids
# Assign observations to the closest centroid
# Find the new location of the centroid by taking the mean of all the observations in each cluster
# Repeat steps 3-5 until the centroids do not change position

# 9. In the sense of hierarchical clustering, define the terms single link and complete link.
# 

# Single linkage: computes the minimum distance between clusters before merging them. Complete linkage: computes the maximum distance between clusters before merging them.

# 10. How does the apriori concept aid in the reduction of measurement overhead in a business basket analysis? Give an example to demonstrate your point.
# 

# The Apriori concept aids in the reduction of measurement overhead in business basket analysis by efficiently pruning and eliminating infrequent itemsets based on the Apriori property. This property states that if an itemset is infrequent, all of its supersets will also be infrequent. By leveraging this property, the algorithm avoids unnecessary computations and focuses only on potentially frequent itemsets, reducing the measurement overhead. As a result, Apriori allows for more efficient analysis of large datasets in market basket analysis.
# 
# 
# for example:
# The provided Python code demonstrates how the Apriori algorithm can be implemented to find frequent itemsets in a set of transactions. By applying the Apriori property, the code efficiently generates and prunes candidate itemsets, reducing the measurement overhead involved in examining all possible itemsets.

# In[ ]:




