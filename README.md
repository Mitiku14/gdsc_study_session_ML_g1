Ride Price Estimation System (Mini Project)
Project Overview

This project implements an end-to-end machine learning system to estimate ride prices based on trip and contextual factors. The objective is to demonstrate the complete ML workflow, including dataset design, data preprocessing, regression modeling, classification modeling, and ethical reflection. The focus is on practical understanding rather than maximizing accuracy.

Problem Statement

Given information about a trip (distance, duration, time of day, traffic, weather, and demand level), the system predicts:

The exact ride price using a regression model

Whether the ride is high-cost or low-cost using a classification model

Dataset Description

A synthetic dataset was created with 200 rows and 7 columns.

Features:

distance_km (Numerical)

duration_min (Numerical)

time_of_day (Categorical)

traffic_level (Categorical)

weather (Categorical)

demand_level (Numerical)

Target:

ride_price (Continuous)

The dataset contains both numerical and categorical variables as required.

Models Used

Linear Regression → Price prediction

Logistic Regression → High-cost vs Low-cost classification

 Data Preprocessing

Missing value handling

One-hot encoding for categorical variables

Feature scaling using StandardScaler

Outlier detection using IQR method

Evaluation Metrics

Mean Absolute Error (MAE) for regression

Accuracy and Confusion Matrix for classification

Key Findings

Distance and trip duration are the most influential features.

The regression model predicts ride prices with reasonable accuracy.

The classification model successfully separates high-cost and low-cost rides.

 How to Run the Project

Clone the repository

Open notebook/ride_price_model.ipynb

Upload data/rides.csv

Run all cells in order

📁 Repository Structure
ride-price-ml/
│── data/
│   └── rides.csv
│── notebook/
│   └── ride_price_model.ipynb
│── README.md
