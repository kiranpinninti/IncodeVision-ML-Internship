# Task 01 - Data Cleaning and Visualization

## Objective
The objective of this project is to perform data cleaning and data visualization on a house price dataset using Python.

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

## Dataset
The dataset contains information about houses with the following features:

- Area
- Bedrooms
- Bathrooms
- Stories
- Parking
- Price

## Data Cleaning
The following data cleaning operations were performed:

1. Checked the dataset information.
2. Checked for missing values.
3. Checked for duplicate records.
4. Removed duplicate records.
5. Generated a statistical summary.
6. Saved the cleaned dataset as `cleaned_house_data.csv`.

## Data Visualization
The following visualizations were created:

1. House Price Distribution
2. Bedrooms vs Price
3. Price Box Plot
4. Correlation Heatmap

## Project Structure

Task 01/
├── house_data.csv
├── cleaned_house_data.csv
├── task1.py
├── README.md
└── outputs/
    ├── house_price_distribution.png
    ├── bedrooms_vs_price.png
    ├── price_boxplot.png
    └── correlation_heatmap.png

## How to Run

Install the required libraries:

```bash
pip install pandas numpy matplotlib seaborn