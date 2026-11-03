"""
YuvaIntern Week 3 - Advanced Data Analysis and Visualization in Logistics
Dataset: synthetic educational logistics data from Week 2.
Run from the folder containing week2_logistics_cleaned_dataset_verified.csv.
Install: python -m pip install pandas matplotlib
"""
import pandas as pd
import matplotlib.pyplot as plt

INPUT = "week2_logistics_cleaned_dataset_verified.csv"
df = pd.read_csv(INPUT)

# Select original operational fields only. Engineered scaling/outlier columns are not
# treated as additional observations or duplicated business metrics.
cols = ["Order_ID", "Delivery_Zone", "Distance_KM", "Traffic_Level", "Vehicle_Type",
        "Weather", "Delivery_Time_Min", "Shipping_Cost_INR", "Delivery_Status"]
data = df[cols].copy()

numeric = ["Distance_KM", "Delivery_Time_Min", "Shipping_Cost_INR"]
data[numeric] = data[numeric].apply(pd.to_numeric, errors="coerce")
data = data.dropna(subset=numeric)

print("\\nDATASET OVERVIEW")
print(data.info())
print("\\nDESCRIPTIVE STATISTICS")
print(data[numeric].describe().round(2))
print("\\nCORRELATION MATRIX")
print(data[numeric].corr().round(3))

print("\\nAVERAGE DELIVERY TIME BY ZONE")
print(data.groupby("Delivery_Zone")["Delivery_Time_Min"].agg(["count","mean","median"]).round(2))
print("\\nAVERAGE DELIVERY TIME BY TRAFFIC")
print(data.groupby("Traffic_Level")["Delivery_Time_Min"].agg(["count","mean","median"]).round(2))
print("\\nDELIVERY STATUS")
print(data["Delivery_Status"].value_counts())

# 1. Delivery time distribution: histogram shows spread, skew and common ranges.
plt.figure(figsize=(8, 5))
plt.hist(data["Delivery_Time_Min"], bins=18, edgecolor="black")
plt.title("Distribution of Delivery Time")
plt.xlabel("Delivery time (minutes)")
plt.ylabel("Number of orders")
plt.tight_layout()
plt.savefig("week3_delivery_time_distribution.png", dpi=180)
plt.close()

# 2. Zone comparison: bar chart compares group means for operational planning.
zone_mean = data.groupby("Delivery_Zone")["Delivery_Time_Min"].mean().sort_values()
plt.figure(figsize=(8, 5))
plt.bar(zone_mean.index, zone_mean.values)
plt.title("Average Delivery Time by Delivery Zone")
plt.xlabel("Delivery zone")
plt.ylabel("Average delivery time (minutes)")
plt.tight_layout()
plt.savefig("week3_avg_delivery_by_zone.png", dpi=180)
plt.close()

# 3. Traffic comparison: compares delivery times across traffic categories.
traffic_order = [x for x in ["Low", "Medium", "High"] if x in data["Traffic_Level"].unique()]
traffic_mean = data.groupby("Traffic_Level")["Delivery_Time_Min"].mean().reindex(traffic_order)
plt.figure(figsize=(8, 5))
plt.bar(traffic_mean.index, traffic_mean.values)
plt.title("Average Delivery Time by Traffic Level")
plt.xlabel("Traffic level")
plt.ylabel("Average delivery time (minutes)")
plt.tight_layout()
plt.savefig("week3_delivery_by_traffic.png", dpi=180)
plt.close()

# 4. Scatter plot: checks whether longer routes tend to require more time.
plt.figure(figsize=(8, 5))
for status, group in data.groupby("Delivery_Status"):
    plt.scatter(group["Distance_KM"], group["Delivery_Time_Min"], alpha=0.65, label=status)
plt.title("Distance vs Delivery Time")
plt.xlabel("Distance (km)")
plt.ylabel("Delivery time (minutes)")
plt.legend()
plt.tight_layout()
plt.savefig("week3_distance_vs_delivery_time.png", dpi=180)
plt.close()

# 5. Correlation heatmap: numeric correlation is descriptive, not proof of causation.
corr = data[numeric].corr()
plt.figure(figsize=(7, 5))
plt.imshow(corr, vmin=-1, vmax=1, aspect="auto")
plt.colorbar(label="Pearson correlation")
plt.xticks(range(len(numeric)), numeric, rotation=20)
plt.yticks(range(len(numeric)), numeric)
for i in range(len(numeric)):
    for j in range(len(numeric)):
        plt.text(j, i, f"{corr.iloc[i, j]:.2f}", ha="center", va="center")
plt.title("Correlation Among Logistics Metrics")
plt.tight_layout()
plt.savefig("week3_logistics_correlation_heatmap.png", dpi=180)
plt.close()

# 6. Status counts: shows the balance of on-time and delayed orders.
status_counts = data["Delivery_Status"].value_counts()
plt.figure(figsize=(7, 5))
plt.bar(status_counts.index.astype(str), status_counts.values)
plt.title("Delivery Status Counts")
plt.xlabel("Delivery status")
plt.ylabel("Number of orders")
plt.tight_layout()
plt.savefig("week3_delivery_status_counts.png", dpi=180)
plt.close()

# 7. Cost by vehicle: compares average simulated shipping cost by vehicle type.
vehicle_cost = data.groupby("Vehicle_Type")["Shipping_Cost_INR"].mean().sort_values()
plt.figure(figsize=(8, 5))
plt.bar(vehicle_cost.index.astype(str), vehicle_cost.values)
plt.title("Average Shipping Cost by Vehicle Type")
plt.xlabel("Vehicle type")
plt.ylabel("Average shipping cost (INR)")
plt.tight_layout()
plt.savefig("week3_avg_cost_by_vehicle.png", dpi=180)
plt.close()

print("\\nCharts saved. All findings describe synthetic educational data only.")
