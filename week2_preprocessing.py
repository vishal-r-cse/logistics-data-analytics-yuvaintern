"""
Week 2: Logistics data cleaning and preprocessing
Dataset: week2_logistics_raw_dataset.csv
Note: The dataset is synthetic and intended for educational demonstration.
"""

from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler

INPUT_FILE = "week2_logistics_raw_dataset.csv"
OUTPUT_FILE = "week2_logistics_cleaned_dataset.csv"
SUMMARY_FILE = "week2_preprocessing_summary.txt"

def main():
    df = pd.read_csv(INPUT_FILE)
    original_rows = len(df)

    # 1. Inspect missing values and exact duplicate records.
    missing_before = df.isna().sum()
    duplicates_before = int(df.duplicated().sum())

    # 2. Remove exact duplicate rows.
    df = df.drop_duplicates().copy()
    rows_after_dedup = len(df)

    # 3. Convert numeric columns safely and impute missing values with medians.
    numeric_cols = ["Distance_KM", "Delivery_Time_Min", "Shipping_Cost_INR"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")
        df[col] = df[col].fillna(df[col].median())

    # 4. Impute missing categorical values using each column's mode.
    categorical_cols = ["Delivery_Zone", "Traffic_Level", "Vehicle_Type",
                        "Weather", "Delivery_Status"]
    for col in categorical_cols:
        if df[col].isna().any():
            df[col] = df[col].fillna(df[col].mode(dropna=True)[0])

    # 5. Flag IQR outliers. Keep them for investigation; do not silently delete.
    outlier_counts = {}
    for col in numeric_cols:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr
        flag_col = f"{col}_Outlier_Flag"
        df[flag_col] = (df[col] < lower) | (df[col] > upper)
        outlier_counts[col] = int(df[flag_col].sum())

    # 6. Add normalized/scaled copies while retaining interpretable original units.
    minmax = MinMaxScaler()
    standard = StandardScaler()
    df[[f"{c}_MinMax" for c in numeric_cols]] = minmax.fit_transform(df[numeric_cols])
    df[[f"{c}_ZScore" for c in numeric_cols]] = standard.fit_transform(df[numeric_cols])

    # 7. Basic validation.
    missing_after = int(df.isna().sum().sum())
    duplicate_after = int(df.duplicated().sum())
    df.to_csv(OUTPUT_FILE, index=False)

    lines = [
        "WEEK 2 LOGISTICS DATA PREPROCESSING SUMMARY",
        "Dataset is synthetic and for educational demonstration only.",
        f"Rows initially loaded: {original_rows}",
        f"Exact duplicate rows detected and removed: {duplicates_before}",
        f"Rows after duplicate removal: {rows_after_dedup}",
        f"Missing values before cleaning: {int(missing_before.sum())}",
        f"Missing values after cleaning: {missing_after}",
        f"Duplicate rows after cleaning: {duplicate_after}",
        "",
        "Missing values by column before cleaning:",
        missing_before.to_string(),
        "",
        "IQR outlier flags (records retained for review):",
    ]
    lines.extend([f"{col}: {count}" for col, count in outlier_counts.items()])
    lines.extend([
        "",
        "Numeric preprocessing:",
        "Median imputation was used for missing numeric values.",
        "Mode imputation was used for missing categorical values.",
        "Min-Max scaled and Z-score standardized copies were added.",
        "Original measurement columns were retained.",
        f"Cleaned dataset saved to: {OUTPUT_FILE}",
    ])
    Path(SUMMARY_FILE).write_text("\n".join(lines), encoding="utf-8")

    print("\n".join(lines))
    print("\nCleaned dataset preview:")
    print(df.head(5).to_string(index=False))

if __name__ == "__main__":
    main()
