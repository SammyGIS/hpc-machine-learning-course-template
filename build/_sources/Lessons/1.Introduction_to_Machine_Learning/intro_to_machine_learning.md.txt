## Applications of Machine Learning

ML is used in many real-life situations, such as:

- Predicting house prices based on features like size, location, etc.
- Classifying emails as spam or not spam.
- Recognizing faces in images.
- Recommending products or content based on user behavior.
- Predicting whether a patient has a disease based on medical data.


## Types of Machine Learning

There are three main types of machine learning:

### 1. Supervised Learning

This is the most common type of machine learning.

In supervised learning:

- The dataset includes **input features** and **labels** (the correct answers).
- The goal is to train a model to learn the relationship between the features and the label.

**Example:**  
You have data on student performance (hours studied, attendance, assignments) and whether they passed or failed. You train a model using this data to predict whether a new student will pass or fail.

### 2. Unsupervised Learning

In unsupervised learning:

- The dataset includes only **input features**, without any labels.
- The goal is to find patterns or structures in the data.

**Example:**  
Grouping customers into segments based on their shopping behavior, without knowing who they are.

### 3. Reinforcement Learning (brief mention)

In reinforcement learning:

- The model learns by interacting with an environment.
- It receives **rewards** or **penalties** based on its actions and tries to maximize the total reward over time.

This is used in areas like robotics, game playing, and self-driving cars.

## Focus: Supervised Learning with Random Forest

Let’s focus more on supervised learning using a model called **Random Forest**.

## What is Random Forest?

Random Forest is a type of machine learning model used for both **classification** and **regression** tasks.

It is based on a group of models called **decision trees**. A decision tree makes predictions by asking a series of questions and moving through branches based on the answers.

Random Forest builds **many decision trees**, each trained on a slightly different sample of the data. It then combines the results of all the trees to make a final prediction.

This process is known as **ensemble learning**, and it helps improve accuracy and reduce overfitting.


## Why Use Random Forest?

- It works well with both small and large datasets.
- It handles missing or unbalanced data better than single models.
- It is less likely to overfit compared to a single decision tree.
- It can give you the **importance of each feature**, helping to understand which variables are most useful for prediction.

## Example: Predicting Student Success

Suppose we want to build a model that predicts if a student will pass or fail.

We collect data like:

- Number of study hours per week
- Attendance percentage
- Whether homework is submitted

We also know the outcome: Pass or Fail.

We use this labeled data to train a Random Forest model. The model learns from the patterns and relationships in the data. Once trained, it can predict the outcome for new students based on their input features.

## Summary Table

| Concept | Explanation |
|--------|-------------|
| Machine Learning | Computers learning from data instead of fixed rules |
| Supervised Learning | Model learns from labeled data (with answers) |
| Unsupervised Learning | Model finds patterns in data without labels |
| Reinforcement Learning | Model learns by interacting and getting feedback |
| Random Forest | A model that uses many decision trees and averages the results for better predictions |