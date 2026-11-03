# E-Commerce Last-Mile Delivery Optimization — YuvaIntern Internship Project

## Project Overview

This project focuses on analyzing and improving the efficiency of e-commerce last-mile delivery operations using Python and data analytics.

The project is developed as part of the **YuvaIntern Logistics Data Analyst Internship**. It demonstrates data analysis techniques, data cleaning, preprocessing, exploratory data analysis (EDA), statistical analysis and visualization.

The project is organized into weekly activities, progressing from basic Python demonstrations to advanced logistics data analysis.

**Important:** All processed logistics records used in Weeks 2 and 3 are synthetic educational data. They do not represent actual company, customer or delivery records.

---

## Technologies and Tools

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Jupyter Notebook / Python environment
- Git and GitHub

---

# Week 1 – Introduction to Logistics Data Analysis

## Overview

Week 1 introduces basic Python programming and data analysis concepts through a hypothetical logistics provider.

## Activities

- Performed basic data-quality checks using Pandas.
- Calculated average delivery time.
- Demonstrated geographic K-Means clustering.
- Implemented baseline linear regression using delivery distance.

## Week 1 Files

- `last_mile_delivery_optimization_week1.py` – Python demonstration script.

## Execution

Install the required dependencies:

```bash
python -m pip install pandas scikit-learn
```

Run the Python script:

```bash
python last_mile_delivery_optimization_week1.py
```

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

A public research dataset, LaDe, is included as a reference for real-world last-mile delivery data. It was not used as the dataset processed in this project.

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

The Week 3 analysis includes the following visualizations:

1. Delivery-time distribution.
2. Average delivery time by delivery zone.
3. Delivery time by traffic level.
4. Distance versus delivery time scatter plot.
5. Logistics numerical correlation heatmap.
6. Delivery-status count chart.
7. Average shipping cost by vehicle type.

Each visualization is used to examine a specific aspect of logistics operations and support the interpretation of the dataset.

## Limitations

- The analysis uses synthetic educational data.
- Correlation does not imply causation.
- Group averages may be influenced by distance, zone, vehicle type and sample size.
- No actual company service-level agreement (SLA) threshold or lateness duration is available.
- Real operational decisions require validation with representative delivery records.

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
└── week3_eda_summary.txt
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

Week 1:

```bash
python last_mile_delivery_optimization_week1.py
```

Week 2:

```bash
python week2_preprocessing.py
```

Week 3:

```bash
python week3_logistics_eda_visualization.py
```

**Note:** Run the Week 2 preprocessing workflow before Week 3 if you need to regenerate the processed dataset. Check the script's input and output paths before running it.

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
- Interpretation of logistics performance indicators.
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
- Scikit-learn Clustering: https://scikit-learn.org/stable/modules/clustering.html
- Scikit-learn Linear Regression: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
- NumPy Documentation: https://numpy.org/doc/
- Matplotlib Documentation: https://matplotlib.org/stable/

---

# Project Disclaimer

This repository is an educational project developed as part of the YuvaIntern Logistics Data Analyst Internship.

All processed logistics records and numerical findings in Weeks 2 and 3 are based on synthetic data created for learning and demonstration purposes. They are not actual company, customer or delivery records.

The analysis demonstrates data analytics workflows and should not be interpreted as a validated production logistics optimization system.

---

**Repository:** https://github.com/vishal-r-cse/logistics-data-analytics-yuvaintern

**Project:** E-Commerce Last-Mile Delivery Optimization

**Internship:** YuvaIntern – Logistics Data Analyst
