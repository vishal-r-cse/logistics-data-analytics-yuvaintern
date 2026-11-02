"""
YuvaIntern Week 2: Logistics Data Collection, Cleaning and Preprocessing
Dataset used for execution: week2_logistics_raw_dataset.csv
Important: this is a synthetic educational dataset, not real company data.
Install: pip install pandas numpy scikit-learn
Run: python week2_preprocessing_detailed.py
Place this script and the raw CSV in the same folder.
"""
from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler

INPUT_FILE = "week2_logistics_raw_dataset.csv"
OUTPUT_FILE = "week2_logistics_cleaned_dataset_verified.csv"
SUMMARY_FILE = "week2_detailed_execution_summary.txt"

NUMERIC = ["Distance_KM", "Delivery_Time_Min", "Shipping_Cost_INR"]
CATEGORICAL = ["Delivery_Zone", "Traffic_Level", "Vehicle_Type",
               "Weather", "Delivery_Status"]

def main():
    df = pd.read_csv(INPUT_FILE)
    initial_rows, initial_cols = df.shape
    missing_by_column = df.isna().sum()
    duplicates = int(df.duplicated().sum())

    print("STEP 1 - INITIAL AUDIT")
    print("Shape:", df.shape)
    print("Missing values by column:\\n", missing_by_column)
    print("Exact duplicate rows:", duplicates)

    # Remove exact duplicate records; preserve different orders even if values look similar.
    df = df.drop_duplicates().copy()
    rows_after_dedup = len(df)

    # Convert numeric fields and impute using medians.
    median_values = {}
    for col in NUMERIC:
        df[col] = pd.to_numeric(df[col], errors="coerce")
        median_values[col] = float(df[col].median())
        df[col] = df[col].fillna(median_values[col])

    # Fill categorical missing values with the most frequent category (mode).
    mode_values = {}
    for col in CATEGORICAL:
        if df[col].isna().any():
            mode_values[col] = df[col].mode(dropna=True).iloc[0]
            df[col] = df[col].fillna(mode_values[col])

    # Calculate IQR limits on the deduplicated, median-imputed measurements.
    # Flag unusual values for review; do not automatically delete them.
    outlier_summary = {}
    for col in NUMERIC:
        q1, q3 = df[col].quantile([0.25, 0.75])
        iqr = q3 - q1
        lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
        flag = (df[col] < lower) | (df[col] > upper)
        df[f"{col}_Outlier_Flag"] = flag
        outlier_summary[col] = (float(q1), float(q3), float(iqr),
                                float(lower), float(upper), int(flag.sum()))

    # Create scaled copies; original units remain available for interpretation.
    mm = MinMaxScaler()
    ss = StandardScaler()
    df[[f"{c}_MinMax" for c in NUMERIC]] = mm.fit_transform(df[NUMERIC])
    df[[f"{c}_ZScore" for c in NUMERIC]] = ss.fit_transform(df[NUMERIC])

    # Final quality checks and export.
    missing_after = int(df.isna().sum().sum())
    duplicate_after = int(df.duplicated().sum())
    assert missing_after == 0, "Missing values remain after preprocessing"
    assert duplicate_after == 0, "Duplicate rows remain after preprocessing"
    df.to_csv(OUTPUT_FILE, index=False)

    lines = [
        "WEEK 2 DETAILED EXECUTION SUMMARY",
        f"Initial rows: {initial_rows}",
        f"Columns: {initial_cols}",
        f"Exact duplicate rows removed: {duplicates}",
        f"Rows after duplicate removal: {rows_after_dedup}",
        f"Missing cells before cleaning: {int(missing_by_column.sum())}",
        f"Missing cells after cleaning: {missing_after}",
        f"Duplicate rows after cleaning: {duplicate_after}",
        "",
        "Missing values by column:",
        missing_by_column.to_string(),
        "",
        "Numeric medians used:",
    ]
    lines += [f"{k}: {v:.3f}" for k, v in median_values.items()]
    lines += ["", "Categorical modes used (where imputation was needed):"]
    lines += [f"{k}: {v}" for k, v in mode_values.items()]
    lines += ["", "IQR calculations and flags:"]
    for col, vals in outlier_summary.items():
        q1, q3, iqr, lower, upper, count = vals
        lines.append(f"{col}: Q1={q1:.3f}, Q3={q3:.3f}, IQR={iqr:.3f}, "
                     f"lower={lower:.3f}, upper={upper:.3f}, flags={count}")
    lines += ["", f"Output saved: {OUTPUT_FILE}",
              "Outlier flags are review indicators; flagged records were retained."]
    Path(SUMMARY_FILE).write_text("\\n".join(lines), encoding="utf-8")
    print("\\n".join(lines))
    print("\\nCleaned preview:\\n", df.head(5).to_string(index=False))

if __name__ == "__main__":
    main()
