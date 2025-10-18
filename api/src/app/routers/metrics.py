from fastapi import APIRouter, Query
from typing import List, Dict
from .sensors import _SENSORS
from collections import defaultdict
import calendar

router = APIRouter(tags=["metrics"], prefix="/metrics")

def _group_daily_counts():
    daily = defaultdict(int)
    for s in _SENSORS:
        day = s.sent_at.date()
        daily[day] += 1
    return daily

def _bayesian_average_per_month(m: int = 7):
    daily = _group_daily_counts()
    if not daily:
        return []
    C = sum(daily.values()) / len(daily)
    by_month_days = defaultdict(list)
    for day, cnt in daily.items():
        key = f"{day.year}-{day.month:02d}"
        by_month_days[key].append(cnt)

    stats = []
    for key, counts in sorted(by_month_days.items()):
        v = len(counts)
        R = sum(counts) / v
        ba = (v/(v+m))*R + (m/(v+m))*C
        y, mo = key.split("-")
        stats.append({
            "year": int(y),
            "month": int(mo),
            "month_name": calendar.month_name[int(mo)],
            "days_with_data": v,
            "avg_per_day": R,
            "global_avg_per_day": C,
            "bayesian_avg_per_day": ba,
            "total_month_sensors": sum(counts),
        })
    return stats

@router.get("/bayesian-monthly")
def bayesian_monthly(m: int = Query(7, ge=1, le=90)) -> List[Dict]:
    return _bayesian_average_per_month(m=m)
