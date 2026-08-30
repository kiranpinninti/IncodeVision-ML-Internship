import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("Housing.csv")

print("----- DATASET -----")
print(df.head())

print("\n----- DATASET SHAPE -----")
print(df.shape)

print("\n----- MISSING VALUES -----")
print(df.isnull().sum())

df = df.drop_duplicates()

categorical_columns = df.select_dtypes(include=["object"]).columns

df = pd.get_dummies(
    df,
    columns=categorical_columns,
    drop_first=True
)

X = df.drop("price", axis=1)
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n----- MODEL RESULTS -----")
print("Mean Squared Error:", mse)
print("R2 Score:", r2)

results = pd.DataFrame({
    "Actual Price": y_test.values,
    "Predicted Price": y_pred
})

print("\n----- ACTUAL VS PREDICTED -----")
print(results.head(10))

results.to_csv("prediction_results.csv", index=False)

plt.figure(figsize=(8, 5))

plt.scatter(y_test, y_pred)

plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted House Prices")

plt.savefig("actual_vs_predicted.png")

plt.show()

print("\nTask 02 completed successfully!")