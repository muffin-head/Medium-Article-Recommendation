Certainly! Here's a refined version of the README/wiki for your repository:

---

# Project Title: Large-Scale Pairwise Article Comparison with Cosine Similarity

## Overview

This project aims to perform large-scale pairwise comparisons of articles (or files) to compute various features and labels based on specific thresholds. The main focus is on calculating the cosine similarity between the content of the files and other related features. Given the computational intensity of comparing a large number of files, the project was initially designed to run on a local environment but includes considerations for scaling the process using PySpark.

### Key Features:
- **Cosine Similarity Calculation:** Directly compute the cosine similarity between pairs of files.
- **Custom Labeling Based on Thresholds:** Generate labels for pairs of articles based on user-defined thresholds for claps and responses.
- **User Interaction for Labeling:** The code also includes features for interactive labeling, which can be used for machine learning tasks, though this part is commented out due to computational constraints.

## Problem Statement

Given a dataset of 5,000 articles, the goal is to perform pairwise comparisons to generate features and labels that can be used for further analysis or machine learning tasks. The main challenge is the quadratic scaling of the comparisons, which results in approximately 12.5 million pairwise operations for 5,000 files.

## Dataset

- **Number of Files:** 5,000
- **Number of Columns per File:** 10
- **Key Features:**
  - `claps`: Number of claps an article received.
  - `responses`: Number of responses an article received.
  - `medium rating` and `response rating`: Ratings associated with the article.

## Methodology

### 1. Thresholds for Labeling
- **Claps Threshold:** 250
- **Responses Threshold:** 10

These thresholds are used to determine whether a pair of articles receives a label of `1` (positive pair) or `0` (negative pair).

### 2. Pairwise Comparison
The core of the project involves comparing each article with every other article using cosine similarity. This results in a large number of comparisons, given by the formula:

\[
\text{Number of comparisons} = \frac{n \times (n - 1)}{2}
\]

For 5,000 files, this results in approximately 12.5 million comparisons.

### 3. Code Overview
The code iterates over each pair of articles, computing cosine similarity and other features, and appending these to a list, which is eventually converted into a DataFrame. The labeling is based on the predefined thresholds for claps and responses.

#### Sample Code Snippet:
```python
claps_threshold = 250 
responses_threshold = 10  

n_articles = train_df.shape[0]
features = []
labels = []

# Iterate over each pair of articles
for i in range(n_articles):
    for j in range(i + 1, n_articles):
        # Compute the label for each pair
        label = 1 if (train_df.iloc[i]['claps'] >= claps_threshold and train_df.iloc[j]['claps'] >= claps_threshold) and \
                      (train_df.iloc[i]['responses'] >= responses_threshold and train_df.iloc[j]['responses'] >= responses_threshold) else 0
        
        # Append features and label
        features.append({
            'cosine_similarity': cosine_sim_train[i, j],
            'medium_rating_i': train_df.iloc[i]['medium rating'],
            'response_rating_i': train_df.iloc[i]['response_rating'],
            'medium_rating_j': train_df.iloc[j]['medium rating'],
            'response_rating_j': train_df.iloc[j]['response_rating']
        })
        labels.append(label)

# Convert list to DataFrame
feature_df = pd.DataFrame(features)
label_df = pd.DataFrame(labels, columns=['label'])

# Optionally combine features and labels into one DataFrame
feature_label_df = pd.concat([feature_df, label_df], axis=1)

print(feature_label_df.head())
```

### 4. User Interaction for Labeling (Commented Out)
The project also includes code for interactive user labeling, which could be useful for refining the model. However, due to computational constraints, this part of the code is commented out. Users with access to more powerful computational resources (e.g., a distributed computing environment) can uncomment and utilize this section.

### 5. Computational Constraints
Due to the computationally intensive nature of the task, running the complete comparison process on a local machine with limited resources (e.g., a typical desktop) may take an extended period (potentially 20-24 hours or more for 5,000 files). Thus, the code is designed with scalability in mind, with placeholders for parallel processing techniques, though these are not implemented in the default version.

## Future Work
- **Parallelization:** Implementing parallel processing using PySpark or Dask to handle larger datasets efficiently.
- **Optimization:** Further optimization of memory usage and computational efficiency.
- **Interactive Labeling:** Expanding the user interaction features once computational resources permit.

## Conclusion
This project demonstrates the challenges and methodologies involved in large-scale pairwise file comparison, providing a foundation for more advanced data processing and machine learning tasks. The current implementation is suitable for smaller datasets or educational purposes, with potential for scaling in a more resource-rich environment.
