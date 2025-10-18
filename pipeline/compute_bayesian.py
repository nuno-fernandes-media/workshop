import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from collections import defaultdict
import calendar
from pathlib import Path
import argparse
import requests
import json

def fetch_sensor_events(api_url: str = "http://localhost:8000/api/sensors"):
    """Fetch sensor data from the API and return list of datetime objects"""
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        sensors = response.json()
        return [datetime.fromisoformat(sensor["sent_at"]) for sensor in sensors]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching sensor data from API: {e}")
        print("Falling back to mock data...")
        # Fallback to mock data if API is not available
        dates = [
            "2025-01-05T10:00:00",
            "2025-01-07T12:30:00",
            "2025-02-02T09:15:00",
            "2025-02-11T18:45:00",
            "2025-03-21T14:10:00",
            "2025-03-22T08:05:00",
            "2025-03-25T17:20:00",
        ]
        return [datetime.fromisoformat(d) for d in dates]

def bayesian_monthly(m: int = 7, api_url: str = "http://localhost:8000/api/sensors"):
    daily = defaultdict(int)
    for dt in fetch_sensor_events(api_url):
        daily[dt.date()] += 1
    if not daily:
        return pd.DataFrame()
    C = sum(daily.values()) / len(daily)
    by_month = defaultdict(list)
    for day, cnt in daily.items():
        key = f"{day.year}-{day.month:02d}"
        by_month[key].append(cnt)
    rows = []
    for key, counts in sorted(by_month.items()):
        v = len(counts)
        R = sum(counts) / v
        ba = (v/(v+m))*R + (m/(v+m))*C
        y, mo = key.split("-")
        rows.append({
            "year": int(y),
            "month": int(mo),
            "month_name": calendar.month_name[int(mo)],
            "days_with_data": v,
            "avg_per_day": R,
            "global_avg_per_day": C,
            "bayesian_avg_per_day": ba,
            "total_month_sensors": sum(counts),
        })
    return pd.DataFrame(rows)

def save_chart(df: pd.DataFrame, out_png: str = "../charts/bayesian_monthly.png"):
    if df.empty:
        print("No data to chart"); return
    df = df.sort_values(["year","month"])
    plt.figure()
    ax = df.plot(x="month_name", y=["total_month_sensors", "bayesian_avg_per_day"])
    plt.title("Sensors per Month & Bayesian Avg/Day")
    plt.xlabel("Month")
    plt.ylabel("Count / Avg per Day")
    plt.tight_layout()
    Path(out_png).parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(out_png)
    print(f"Chart saved to {out_png}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--month", help="Filter by YYYY-MM", default=None)
    parser.add_argument("--m", type=int, default=7, help="Prior weight (days)")
    parser.add_argument("--api-url", default="http://localhost:8000/api/sensors", help="API URL for sensor data")
    args = parser.parse_args()
    df = bayesian_monthly(m=args.m, api_url=args.api_url)
    if args.month:
        df = df[df["month"].map(lambda x: f"{x:02d}") == args.month.split("-")[1]]
    print(df.to_string(index=False))
    save_chart(df)
