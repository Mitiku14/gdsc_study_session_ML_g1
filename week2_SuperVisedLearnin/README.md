# Week 2: House Price Prediction

## Project Overview
This project implements a simple machine learning model to predict house prices based on various features using Linear Regression from scikit-learn.

## Dataset
The dataset contains information about houses including:
- `price`: House price (target variable)
- `area`: Area in square feet
- `bedrooms`: Number of bedrooms
- `bathrooms`: Number of bathrooms
- `stories`: Number of stories
- `mainroad`: Proximity to main road
- `guestroom`: Guest room availability
- `basement`: Basement availability
- `hotwater`: Hot water heating
- `airconditioning`: Air conditioning
- `parking`: Number of parking spaces
- `prefarea`: Preferred area
- `furnishingstatus`: Furnishing status

## Project Structure

## Implementation Steps

### 1. Data Loading and Exploration
- Load the dataset using pandas
- Explore data structure and statistics
- Check for missing values

### 2. Data Preparation
- Select features and target variable
- Split data into training (80%) and testing (20%) sets

### 3. Model Training
- Initialize Linear Regression model
- Train on training data
- Learn relationship between area and price

### 4. Model Evaluation
- Make predictions on test set
- Calculate MSE, MAE, and RMSE
- Compute R-squared score
- Visualize results with plots

### 5. Model Extension
- Implement multiple linear regression with more features
- Compare performance with single-feature model

## Key Results
- Linear relationship between house area and price
- Model performance metrics (MSE, MAE, R-squared)
- Visualizations showing regression line and residuals

## How to Run
1. Open `house_price_prediction.ipynb` in Google Colab
2. Upload the dataset when prompted
3. Run all cells sequentially
4. View results and visualizations

## Dependencies
pandas==1.5.3
numpy==1.23.5
scikit-learn==1.2.0
matplotlib==3.7.0
seaborn==0.12.2
pandas==1.5.3
numpy==1.23.5
scikit-learn==1.2.0
matplotlib==3.7.0
seaborn==0.12.2
