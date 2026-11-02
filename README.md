# E-Commerce Last-Mile Delivery Optimization — YuvaIntern Week 1

## Overview
A beginner Python demonstration for a hypothetical logistics provider. All sample records are synthetic and are not actual company data.

## Files
- `last_mile_delivery_optimization_week1.py`: runnable demonstration script.

## Demonstrations
- Data-quality check using pandas
- Average delivery-time calculation
- Geographic K-Means clustering
- Baseline linear regression using distance

## Run
Install dependencies:
```bash
python -m pip install pandas scikit-learn
```
Then run:
```bash
python last_mile_delivery_optimization_week1.py
```

## Limitation
Five synthetic rows demonstrate code syntax only. They cannot support reliable predictions or claims of cost savings. Real deployment requires a larger representative dataset, evaluation on held-out data, road-network constraints, and a pilot.

## Week 2 – Data Collection, Cleaning and Preprocessing

This phase extends the E-Commerce Last-Mile Delivery Optimization project by preparing logistics data for analysis using Python, pandas, NumPy and scikit-learn.

### Dataset

The project uses a synthetic educational dataset containing 300 unique simulated delivery orders and nine original attributes. The raw dataset includes missing values and duplicate records to demonstrate data-cleaning techniques.

A public research dataset, LaDe, is included as a reference for real-world last-mile delivery data. It was not used as the dataset processed in this exercise.

### Week 2 Activities

- Inspected dataset structure and data quality.
- Identified and removed exact duplicate records.
- Handled missing numerical values using median imputation.
- Handled missing categorical values using mode imputation.
- Detected potential outliers using the IQR method.
- Applied Min-Max normalization and Z-score standardization.
- Exported cleaned data and execution summaries.

## Week 2 Files
- `week2_logistics_raw_dataset.csv` – Original synthetic dataset.
- `week2_logistics_cleaned_dataset.csv` – Initial cleaned dataset.
- `week2_logistics_cleaned_dataset_verified.csv` – Verified processed dataset.
- `week2_preprocessing.py` – Initial preprocessing script.
- `week2_preprocessing_detailed.py` – Detailed preprocessing implementation.
- `week2_preprocessing_summary.txt` – Preprocessing summary.
- `week2_preprocessing_summary_readable.txt` – Readable preprocessing summary.
- `week2_detailed_execution_summary.txt` – Detailed execution results.
- `YuvaIntern_Week2_Complete_Enhanced_Report.docx` – Enhanced Week 2 report.

### Limitations
- The dataset is synthetic and intended for educational demonstration.
- IQR identifies potential outliers; these records are not automatically removed.
- Results from simulated data should not be treated as real-world delivery performance.
- Further validation using a larger real-world dataset is required before operational use.

### Public Reference

LaDe – Last-mile Delivery Dataset: https://huggingface.co/datasets/Cainiao-AI/LaDe

**Note:** All processed project records are synthetic and are not actual company or customer data.

## References
- World Bank LPI 2.0: https://lpi.worldbank.org/en/home
- pandas: https://pandas.pydata.org/docs/
- scikit-learn clustering: https://scikit-learn.org/stable/modules/clustering.html
- scikit-learn LinearRegression: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
- Matplotlib: https://matplotlib.org/stable/
