"""
YuvaIntern Week 4 – Predictive Modeling and Optimization in Logistics
Target: Delivery_Time_Min
Dataset: week2_logistics_cleaned_dataset_verified.csv (synthetic educational data)

Run from the repository folder:
    python -m pip install pandas numpy matplotlib scikit-learn
    python week4_predictive_modeling.py
"""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.tree import DecisionTreeRegressor

BASE = Path(__file__).resolve().parent
DATA_FILE = BASE / "week2_logistics_cleaned_dataset_verified.csv"
TARGET = "Delivery_Time_Min"
FEATURES = ["Distance_KM", "Delivery_Zone", "Traffic_Level",
            "Vehicle_Type", "Weather"]
NUMERIC = ["Distance_KM"]
CATEGORICAL = ["Delivery_Zone", "Traffic_Level", "Vehicle_Type", "Weather"]

def main():
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Dataset not found: {DATA_FILE}. Keep the Week 2 verified CSV "
            "in the same folder as this script."
        )

    df = pd.read_csv(DATA_FILE)
    required = FEATURES + [TARGET]
    missing = [col for col in required if col not in df.columns]
    if missing:
        raise ValueError(f"Dataset is missing required columns: {missing}")

    # Use original operational input columns only. Do not use target-derived
    # columns, outlier flags, scaled target columns, or Delivery_Status.
    X = df[FEATURES].copy()
    y = pd.to_numeric(df[TARGET], errors="coerce")
    valid = y.notna()
    X, y = X.loc[valid], y.loc[valid]

    preprocessor = ColumnTransformer([
        ("numeric", Pipeline([
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler())
        ]), NUMERIC),
        ("categorical", Pipeline([
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore"))
        ]), CATEGORICAL)
    ])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42
    )

    models = {
        "Linear Regression": LinearRegression(),
        "Decision Tree": DecisionTreeRegressor(random_state=42),
        "Random Forest": RandomForestRegressor(
            n_estimators=200, random_state=42, n_jobs=-1
        )
    }

    results = []
    fitted_models = {}
    for name, estimator in models.items():
        pipeline = Pipeline([
            ("preprocessing", preprocessor),
            ("model", estimator)
        ])
        cv_mae = -cross_val_score(
            pipeline, X_train, y_train, cv=5,
            scoring="neg_mean_absolute_error"
        ).mean()
        pipeline.fit(X_train, y_train)
        predictions = pipeline.predict(X_test)

        results.append({
            "Model": name,
            "5-fold CV MAE (min)": cv_mae,
            "Test MAE (min)": mean_absolute_error(y_test, predictions),
            "Test RMSE (min)": mean_squared_error(
                y_test, predictions
            ) ** 0.5,
            "Test R2": r2_score(y_test, predictions)
        })
        fitted_models[name] = pipeline

    results_df = pd.DataFrame(results).sort_values(
        ["Test MAE (min)", "Test RMSE (min)"]
    )
    print("\\nMODEL COMPARISON")
    print(results_df.to_string(index=False))

    # Select using training-only cross-validation MAE. The held-out test set
    # remains an unbiased final evaluation and is not used for model selection.
    selected_name = results_df.sort_values(
        "5-fold CV MAE (min)"
    ).iloc[0]["Model"]
    selected_model = fitted_models[selected_name]
    final_predictions = selected_model.predict(X_test)

    output = X_test.copy()
    output["Actual_Delivery_Time_Min"] = y_test
    output["Predicted_Delivery_Time_Min"] = final_predictions
    output["Absolute_Error_Min"] = np.abs(
        y_test.to_numpy() - final_predictions
    )
    output.to_csv(BASE / "week4_test_predictions.csv", index=True)

    plt.figure(figsize=(7, 5))
    plt.scatter(y_test, final_predictions)
    low = min(y_test.min(), final_predictions.min())
    high = max(y_test.max(), final_predictions.max())
    plt.plot([low, high], [low, high], linestyle="--")
    plt.xlabel("Actual delivery time (minutes)")
    plt.ylabel("Predicted delivery time (minutes)")
    plt.title(f"Actual vs Predicted – {selected_name}")
    plt.tight_layout()
    plt.savefig(BASE / "week4_actual_vs_predicted.png", dpi=180)
    plt.close()

    residuals = y_test.to_numpy() - final_predictions
    plt.figure(figsize=(7, 5))
    plt.hist(residuals, bins=20)
    plt.xlabel("Prediction error: actual - predicted (minutes)")
    plt.ylabel("Number of orders")
    plt.title("Prediction Error Distribution")
    plt.tight_layout()
    plt.savefig(BASE / "week4_prediction_error_distribution.png", dpi=180)
    plt.close()

    print(f"\\nSelected demonstration model: {selected_name}")
    print("Outputs: week4_test_predictions.csv and two PNG charts.")
    print("Caution: this is synthetic data; validate before operational use.")

if __name__ == "__main__":
    main()
