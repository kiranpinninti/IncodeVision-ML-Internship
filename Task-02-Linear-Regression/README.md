# Task 02 - Linear Regression Model

## Objective

The objective of this project is to build a Linear Regression Machine Learning model in Python to predict house prices based on different property features.

## Dataset

The project uses a house price dataset containing information about residential properties.

The dataset includes features such as:

- Area
- Bedrooms
- Bathrooms
- Stories
- Parking
- Main Road
- Guest Room
- Basement
- Hot Water Heating
- Air Conditioning
- Preferred Area
- Furnishing Status

The target variable is the house price.

## Technologies Used

- Python
- Pandas
- Matplotlib
- Scikit-learn

## Machine Learning Workflow

The following steps were performed:

1. Loaded the housing dataset using Pandas.
2. Checked the dataset structure and shape.
3. Checked for missing values.
4. Removed duplicate records.
5. Converted categorical variables into numerical values using one-hot encoding.
6. Separated input features and target variable.
7. Split the dataset into training and testing sets.
8. Trained a Linear Regression model.
9. Generated house price predictions.
10. Evaluated the model using Mean Squared Error and R2 Score.
11. Visualized actual prices versus predicted prices.

## Model

The Linear Regression algorithm from Scikit-learn was used.

The dataset was divided into:

- 80% Training Data
- 20% Testing Data

## Model Evaluation

The model achieved the following results:

- Mean Squared Error: 1754318687330.6643
- R2 Score: 0.6529

The R2 score indicates that the model explains approximately 65.3% of the variation in house prices on the test data.

## Visualization

An Actual vs Predicted House Prices scatter plot was created to compare the model predictions with the actual house prices.

## Project Structure

Task 02/
│
├── Housing.csv
├── task2.py
├── prediction_results.csv
├── actual_vs_predicted.png
└── README.md

## How to Run

Install the required libraries:

```bash
pip install pandas matplotlib scikit-learn