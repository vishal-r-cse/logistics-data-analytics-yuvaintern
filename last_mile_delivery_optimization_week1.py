"""YuvaIntern Week 1: Last-mile delivery optimization demo.
All records are synthetic, for learning only.
Install: python -m pip install pandas scikit-learn
Run: python last_mile_delivery_optimization_week1.py
"""
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression

def main():
    data = pd.DataFrame({
        "order_id": [101, 102, 103, 104, 105],
        "latitude": [12.9716, 12.9352, 12.9279, 12.9698, 12.9141],
        "longitude": [77.5946, 77.6245, 77.6271, 77.7499, 77.6101],
        "distance_km": [2.5, 5.0, 6.2, 8.0, 3.1],
        "delivery_time_mins": [25, 40, 45, 60, 30],
    })
    print("SYNTHETIC SAMPLE DATA")
    print(data.to_string(index=False))
    print("\nMissing values by column:")
    print(data.isna().sum())
    print("\nAverage delivery time:", round(data["delivery_time_mins"].mean(), 2), "minutes")

    clusterer = KMeans(n_clusters=2, random_state=42, n_init=10)
    data["delivery_cluster"] = clusterer.fit_predict(data[["latitude", "longitude"]])
    print("\nIllustrative geographic clusters:")
    print(data[["order_id", "delivery_cluster"]].to_string(index=False))

    model = LinearRegression()
    model.fit(data[["distance_km"]], data["delivery_time_mins"])
    prediction = model.predict(pd.DataFrame({"distance_km": [4.0]}))[0]
    print(f"\nIllustrative predicted time for 4 km: {prediction:.1f} minutes")
    print("\nLIMITATION: Five synthetic records are not enough to validate a predictive model.")

if __name__ == "__main__":
    main()
