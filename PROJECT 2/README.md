# AI Project 2 - Data Classification Using AI

## Overview
This project demonstrates a basic Machine Learning classification system using the Iris Dataset. The goal is to train and evaluate different classification algorithms and compare their performance.

## Objective
The objective of this project is to:

- Load and understand a dataset
- Split data into training and testing sets
- Train multiple classification models
- Evaluate model performance
- Compare classification algorithms
- Visualize results using graphs

## Dataset
The project uses the Iris Dataset provided by Scikit-Learn.

Features:
- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

Classes:
- Setosa
- Versicolor
- Virginica

## Technologies Used

- Python
- Scikit-Learn
- Matplotlib

## Algorithms Used

1. Decision Tree Classifier
2. K-Nearest Neighbors (KNN)
3. Logistic Regression

## Project Workflow

### Step 1: Load Dataset
The Iris dataset is loaded using Scikit-Learn.

### Step 2: Data Exploration
Basic information about the dataset is displayed:
- Dataset shape
- Feature names
- Target classes

### Step 3: Data Splitting
The dataset is divided into:
- 80% Training Data
- 20% Testing Data

### Step 4: Model Training
Three classification models are trained using the training dataset.

### Step 5: Model Evaluation
Each model is evaluated using:
- Accuracy Score
- Classification Report
- Confusion Matrix

### Step 6: Model Comparison
The accuracy of all models is compared.

### Step 7: Visualization
A bar chart is generated to visualize algorithm performance.

## Installation

Install required libraries:

```bash
pip install scikit-learn matplotlib