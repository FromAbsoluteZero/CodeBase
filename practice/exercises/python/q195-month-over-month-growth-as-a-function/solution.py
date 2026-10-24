import csv

def monthly_revenue(path):
    """{'YYYY-MM': total revenue that month}."""
    totals = {}
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            month = row["Date"][:7]
            totals[month] = totals.get(month, 0.0) + float(row["Revenue"])
    return totals

def mom_growth(monthly):
    """{'YYYY-MM': growth over the previous month as a fraction, None for the first month}."""
    growth = {}
    previous = None
    for month in sorted(monthly):
        growth[month] = None if previous is None else (monthly[month] - previous) / previous
        previous = monthly[month]
    return growth
