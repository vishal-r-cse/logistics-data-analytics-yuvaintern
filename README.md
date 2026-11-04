# E-Commerce Last-Mile Delivery Optimization

**YuvaIntern – Logistics Data Analyst Internship Project**

## Project Overview

This project focuses on analyzing and improving the efficiency of e-commerce last-mile delivery operations using Python and data analytics.

Developed as part of the **YuvaIntern Logistics Data Analyst Internship**, the project demonstrates a complete learning workflow across four weekly activities:

1. Introduction to logistics data analysis.
2. Data collection, cleaning and preprocessing.
3. Exploratory Data Analysis (EDA) and visualization.
4. Predictive modeling and logistics optimization recommendations.

The project progresses from basic Python demonstrations to data preprocessing, statistical analysis, visualization and machine learning.

**Dataset disclaimer:** The logistics records used in this project are synthetic educational data. They do not represent actual company, customer or delivery records. The results are intended for learning and demonstration, not as evidence of real-world operational performance.

---

## Technologies and Tools

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Git and GitHub
- Jupyter Notebook / Python environment

---

# Week 1 – Introduction to Logistics Data Analysis

## Overview

Week 1 introduces basic Python programming and data analysis concepts through a hypothetical logistics provider.

## Activities

- Performed basic data-quality checks using Pandas.
- Calculated average delivery time.
- Demonstrated geographic K-Means clustering.
- Implemented baseline linear regression using delivery distance.

## Week 1 File

| File | Description |
|---|---|
| `last_mile_delivery_optimization_week1.py` | Python demonstration script |

## Limitations

The Week 1 demonstration uses only five synthetic sample records to illustrate Python concepts. These records are insufficient for reliable predictions or claims of operational cost savings.

A real-world implementation would require a larger representative dataset, testing on held-out data, road-network constraints and a practical pilot.

---

# Week 2 – Data Collection, Cleaning and Preprocessing

## Overview

Week 2 focuses on preparing logistics data for further analysis using Python, Pandas, NumPy and Scikit-learn.

## Dataset

The project uses a synthetic educational dataset containing 300 unique simulated delivery orders and nine original attributes.

The raw dataset includes missing values and duplicate records to demonstrate data-cleaning and preprocessing techniques.

The public research dataset **LaDe – Last-mile Delivery Dataset** is included as a reference for real-world last-mile delivery research. It was not used as the dataset processed in this project.

## Activities

- Inspected dataset structure and data quality.
- Identified and removed exact duplicate records.
- Handled missing numerical values using median imputation.
- Handled missing categorical values using mode imputation.
- Detected potential outliers using the Interquartile Range (IQR) method.
- Applied Min-Max normalization.
- Applied Z-score standardization.
- Exported cleaned datasets and execution summaries.

## Week 2 Files

| File | Description |
|---|---|
| `week2_logistics_raw_dataset.csv` | Original synthetic dataset |
| `week2_logistics_cleaned_dataset.csv` | Initial cleaned dataset |
| `week2_logistics_cleaned_dataset_verified.csv` | Verified processed dataset |
| `week2_preprocessing.py` | Initial preprocessing script |
| `week2_preprocessing_detailed.py` | Detailed preprocessing implementation |
| `week2_preprocessing_summary.txt` | Preprocessing summary |
| `week2_preprocessing_summary_readable.txt` | Readable preprocessing summary |
| `week2_detailed_execution_summary.txt` | Detailed execution results |
| `YuvaIntern_Week2_Complete_Enhanced_Report.docx` | Enhanced Week 2 report |

## Data Cleaning Methods

- **Duplicate removal:** Removes repeated records that could distort counts and statistical calculations.
- **Median imputation:** Fills missing numerical values using the median, which is less sensitive to extreme values than the mean.
- **Mode imputation:** Fills missing categorical values using the most frequent category.
- **IQR method:** Identifies potential outliers for further investigation. Flagged records are not automatically removed.
- **Min-Max scaling:** Transforms numerical values to a common 0–1 range.
- **Z-score standardization:** Expresses numerical values in terms of standard deviations from the mean.

## Limitations

- The dataset is synthetic and intended for educational demonstration.
- Imputation can influence statistical distributions and subsequent analysis.
- IQR identifies potential outliers; it does not establish that a record is erroneous.
- Synthetic results should not be interpreted as actual logistics performance.
- Further validation using representative real-world data is necessary before operational use.

---

# Week 3 – Advanced Data Analysis and Visualization

## Overview

Week 3 focuses on Exploratory Data Analysis (EDA) and visualization using the cleaned synthetic logistics dataset.

Python, Pandas, NumPy and Matplotlib are used to identify patterns, compare delivery performance and understand relationships between logistics variables.

## Activities

- Calculated descriptive statistics, including mean, median and standard deviation.
- Analyzed delivery-time and shipping-cost distributions.
- Compared delivery performance across delivery zones.
- Examined delivery times under different traffic conditions.
- Compared logistics performance across vehicle types.
- Analyzed the relationship between delivery distance and delivery time.
- Generated a correlation heatmap to examine relationships between numerical variables.
- Visualized delivery-status counts.
- Identified potential operational bottlenecks.
- Prepared data-based recommendations.

## Week 3 Files

| File | Description |
|---|---|
| `YuvaIntern_Week3_Advanced_Logistics_Data_Analysis_Report.docx` | Detailed Week 3 analysis report |
| `week3_logistics_eda_visualization.py` | Python EDA and visualization script |
| `week3_eda_summary.txt` | Analysis summary and key findings |

## Key Findings

The analysis of 300 synthetic delivery records produced the following results:

| Metric | Result |
|---|---:|
| Total records analyzed | 300 |
| Average delivery time | 49.76 minutes |
| Average shipping cost | ₹82.83 |
| Average delivery distance | 16.22 km |
| On-time deliveries | 217 (72.3%) |
| Delayed deliveries | 83 (27.7%) |
| Distance and delivery-time correlation | 0.596 |

### Important Observations

- Delivery distance showed a moderate positive correlation with delivery time.
- Rural deliveries had a higher average delivery time than urban deliveries in this dataset.
- High-traffic deliveries had a higher average delivery time than other traffic categories.
- Delivery-status analysis showed that 72.3% of the simulated orders were classified as on time.

These observations are descriptive findings from synthetic data. They do not establish causal relationships or represent actual company performance.

## Visualizations

The Week 3 analysis includes:

1. Delivery-time distribution.
2. Average delivery time by delivery zone.
3. Delivery time by traffic level.
4. Distance versus delivery time scatter plot.
5. Logistics numerical correlation heatmap.
6. Delivery-status count chart.
7. Average shipping cost by vehicle type.

Each visualization examines a specific aspect of logistics operations and supports the interpretation of the dataset.

## Limitations

- The analysis uses synthetic educational data.
- Correlation does not imply causation.
- Group averages may be influenced by distance, zone, vehicle type and sample size.
- No actual company service-level agreement (SLA) threshold or lateness duration is available.
- Real operational decisions require validation with representative delivery records.

---

# Week 4 – Predictive Modeling and Optimization in Logistics Systems

## Overview

Week 4 focuses on developing predictive models to estimate delivery times and proposing optimization strategies for e-commerce last-mile delivery operations.

The analysis uses the verified synthetic logistics dataset prepared during Week 2. Python and Scikit-learn are used for data preprocessing, model training, validation and performance evaluation.

## Prediction Problem

The objective is to predict delivery time in minutes based on the following input features:

- `Distance_KM`
- `Delivery_Zone`
- `Traffic_Level`
- `Vehicle_Type`
- `Weather`

**Target variable:** `Delivery_Time_Min`

## Models Implemented

Three regression models were developed and evaluated:

- **Linear Regression:** Used as a baseline predictive model.
- **Decision Tree Regressor:** Used to capture nonlinear patterns.
- **Random Forest Regressor:** Combines multiple decision trees to generate predictions.

## Model Training and Evaluation

The modeling workflow includes:

- 80:20 training and testing split.
- Five-fold cross-validation on the training data.
- Model comparison using Mean Absolute Error (MAE).
- Final test-set evaluation using MAE, RMSE and R².
- Comparison of actual and predicted delivery times.
- Analysis of prediction errors.

The model-selection process uses training-only cross-validation MAE rather than selecting a model based on test-set results. The test set is retained for final evaluation.

## Week 4 Files

| File | Description |
|---|---|
| `YuvaIntern_Week4_Predictive_Modeling_Optimization_Report.docx` | Detailed predictive modeling and optimization report |
| `week4_predictive_modeling.py` | Python model training and evaluation script |
| `week4_test_predictions.csv` | Actual and predicted test-set results |
| `week4_actual_vs_predicted.png` | Actual versus predicted visualization |
| `week4_prediction_error_distribution.png` | Prediction error distribution visualization |

## Model Evaluation Results

The following results were obtained during the evaluation run:

| Model | Test MAE | Test RMSE | R² |
|---|---:|---:|---:|
| Linear Regression | 10.97 | 48.46 | 0.105 |
| Decision Tree Regressor | 12.88 | 49.23 | 0.077 |
| Random Forest Regressor | 11.46 | 48.11 | 0.118 |

### Interpretation

- Linear Regression achieved the lowest test MAE in this evaluation run.
- Random Forest achieved the lowest test RMSE and the highest R².
- The model-selection process uses five-fold cross-validation MAE on training data.
- The relatively low R² values indicate that the models explain only a limited proportion of the variation in delivery time.
- The comparatively high RMSE indicates that some prediction errors are substantially larger than the typical absolute error.

The results show that model performance depends on the evaluation metric. These models should not be considered production-ready.

## Optimization Recommendations

Based on the modeling workflow and EDA findings, the following strategies are proposed:

1. **Delay-risk identification:** Use predicted delivery times to identify orders that may require attention.
2. **Route planning:** Consider delivery distance and traffic conditions when planning routes.
3. **Delivery-zone grouping:** Explore grouping deliveries by geographical zones, particularly for rural and long-distance routes.
4. **Vehicle allocation:** Consider route requirements and operating costs when assigning vehicles.
5. **Performance monitoring:** Compare actual and predicted delivery times to identify prediction errors and monitor model performance.

These recommendations are proposals for further investigation. They have not been validated through a real-world logistics deployment.

## Limitations

- The dataset contains only 300 synthetic educational records.
- An extreme delivery-time value affects RMSE.
- The model does not use live traffic, GPS or road-network information.
- The model's performance is limited and requires further improvement.
- Larger real-world datasets and additional validation are required before operational use.
- Predictions do not guarantee actual delivery times.

---

# Overall Project Structure

```text
logistics-data-analytics-yuvaintern/
│
├── README.md
├── .gitignore
│
├── last_mile_delivery_optimization_week1.py
│
├── YuvaIntern_Week2_Complete_Enhanced_Report.docx
├── week2_logistics_raw_dataset.csv
├── week2_logistics_cleaned_dataset.csv
├── week2_logistics_cleaned_dataset_verified.csv
├── week2_preprocessing.py
├── week2_preprocessing_detailed.py
├── week2_preprocessing_summary.txt
├── week2_preprocessing_summary_readable.txt
├── week2_detailed_execution_summary.txt
│
├── YuvaIntern_Week3_Advanced_Logistics_Data_Analysis_Report.docx
├── week3_logistics_eda_visualization.py
├── week3_eda_summary.txt
│
├── YuvaIntern_Week4_Predictive_Modeling_Optimization_Report.docx
├── week4_predictive_modeling.py
├── week4_test_predictions.csv
├── week4_actual_vs_predicted.png
└── week4_prediction_error_distribution.png
```

---

# How to Run the Project

## Step 1 – Clone the Repository

```bash
git clone https://github.com/vishal-r-cse/logistics-data-analytics-yuvaintern.git
```

## Step 2 – Open the Project Folder

```bash
cd logistics-data-analytics-yuvaintern
```

## Step 3 – Install Dependencies

```bash
python -m pip install pandas numpy matplotlib scikit-learn
```

## Step 4 – Run the Python Scripts

**Week 1**

```bash
python last_mile_delivery_optimization_week1.py
```

**Week 2**

```bash
python week2_preprocessing.py
```

**Week 3**

```bash
python week3_logistics_eda_visualization.py
```

**Week 4**

```bash
python week4_predictive_modeling.py
```

### Execution Notes

- Run the scripts from the repository's root folder.
- Run the Week 2 preprocessing workflow before Week 3 if you need to regenerate the processed dataset.
- Week 4 uses the verified Week 2 dataset. Ensure that `week2_logistics_cleaned_dataset_verified.csv` is available in the expected location.
- Check the input and output paths inside each script before execution.
- The Python scripts may generate or overwrite output files depending on their implementation.

---

# Learning Outcomes

Through this project, the following skills and concepts are demonstrated:

- Python programming for data analysis.
- Data inspection and quality assessment.
- Data cleaning and missing-value treatment.
- Duplicate detection and removal.
- Outlier identification using IQR.
- Feature scaling and standardization.
- Descriptive statistical analysis.
- Exploratory Data Analysis (EDA).
- Data visualization using Matplotlib.
- Correlation analysis.
- Regression modeling.
- Model training and validation.
- Model evaluation using MAE, RMSE and R².
- Interpretation of logistics performance indicators.
- Development of data-based optimization recommendations.
- Documentation and version control using GitHub.

---

# Public Dataset Reference

**LaDe – Last-mile Delivery Dataset**

https://huggingface.co/datasets/Cainiao-AI/LaDe

LaDe is included as a public research reference. It was not used as the processed dataset in this educational project.

---

# References and Documentation

- World Bank Logistics Performance Index (LPI): https://lpi.worldbank.org/en/home
- Pandas Documentation: https://pandas.pydata.org/docs/
- NumPy Documentation: https://numpy.org/doc/
- Matplotlib Documentation: https://matplotlib.org/stable/
- Scikit-learn Clustering: https://scikit-learn.org/stable/modules/clustering.html
- Scikit-learn Linear Regression: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
- Scikit-learn Model Evaluation: https://scikit-learn.org/stable/modules/model_evaluation.html
- Scikit-learn Cross-Validation: https://scikit-learn.org/stable/modules/cross_validation.html

---

# Project Disclaimer

This repository is an educational project developed as part of the **YuvaIntern Logistics Data Analyst Internship**.

All logistics records and numerical findings used in this project are based on synthetic data created for learning and demonstration purposes. They are not actual company, customer or delivery records.

The project demonstrates data analytics, preprocessing, exploratory analysis, visualization, predictive modeling and optimization recommendations. The results should not be interpreted as validated real-world logistics performance or as a production-ready optimization system.

---

## Project Information

**Project:** E-Commerce Last-Mile Delivery Optimization  
**Internship:** YuvaIntern – Logistics Data Analyst  
**Repository:** https://github.com/vishal-r-cse/logistics-data-analytics-yuvaintern  
**Tools:** Python, Pandas, NumPy, Matplotlib and Scikit-learn

