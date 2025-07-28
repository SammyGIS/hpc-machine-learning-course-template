# Machine Learning in an HPC environment
## Machine Learning with Random Forest and CNN (Image Classification)

## 1. Introduction to Machine Learning
- Brief overview of Machine Learning (ML) and its applications
- Types of ML:
  - Supervised learning
  - Unsupervised learning
  - Reinforcement learning (just a mention)
- Focus on supervised learning using Random Forest

## 2. Data Exploration & Analysis
- Understanding the structure of the dataset
- Basic cleaning and preprocessing
- Visualization and key insights

## 3. Feature Engineering
- Selecting and transforming key features
- Handling missing values
- Encoding categorical variables
- Scaling features

## 4. Random Forest for Prediction
- Introduction to Random Forest: Why and how it works
- Feature importance and its role in prediction
- Building a prediction model with Scikit-learn

## 5. Model Validation & Tuning
- Splitting the data: Train/Test
- Evaluating performance:
  - Accuracy
  - Precision
  - Recall
- Hyperparameter tuning:
  - GridSearchCV
  - RandomizedSearchCV

## 6. Introduction to CNN with Keras & TensorFlow
- Basic understanding of Convolutional Neural Networks (CNNs) for image classification
- Building a simple CNN model for classification
- Comparing CNN results with Random Forest

## 7. Accuracy and Evaluation
- Accuracy comparison: Random Forest vs CNN
- Confusion matrix and validation scores
- Final thoughts and ideas for model improvement


<!-- markdownlint-disable MD013 --><!-- Badges cannot be split up over lines, hence will break 80 characters per line -->

[![Check links](https://github.com/UPPMAX/HPC-python/actions/workflows/check_links.yaml/badge.svg?branch=main)](https://github.com/UPPMAX/HPC-python/actions/workflows/check_links.yaml)
[![Check spelling](https://github.com/UPPMAX/HPC-python/actions/workflows/check_spelling.yaml/badge.svg?branch=main)](https://github.com/UPPMAX/HPC-python/actions/workflows/check_spelling.yaml)

<!-- markdownlint-enable MD013 -->

This course aims to give a brief, but comprehensive introduction to using Machine Learning in an HPC environment. You will learn how to use modules to load Python, how to find site installed Python packages, as well as how to install packages yourself. In addition, you will learn how to use virtual environments, write a batch script for running Python, use Python in parallel, and how to use Python for ML and on GPU:s. 

The course is a cooperation between UPPMAX (Rackham, Snowy, Bianca), LUNARC (Cosmos), and HPC2N (Kebnekaise) and will focus on the compute systems at all 3 centres. For the site-specific part of the course you will be divided into groups depending on which center you will be running your code, as the approach is somewhat different. 

# Build locally  

Navigate to the root directory of your Sphinx project (where the conf.py file is located, ie. in `docs`) and run:

```cmd
make html
```

You can preview the generated HTML files locally by opening the _build/html/index.html file in your browser:

```cmd
xdg-open _build/html/index.html  # On Linux
open _build/html/index.html      # On macOS
```


# Rendered material

- https://uppmax.github.io/HPC-python/index.html

# Others

- [Evaluations](evaluations/README.md)
- [Meeting notes](meeting_notes/README.md)

