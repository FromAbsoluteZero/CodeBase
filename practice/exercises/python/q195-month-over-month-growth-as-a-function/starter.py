import csv

def monthly_revenue(path):
    """{'YYYY-MM': total revenue that month}."""
    raise NotImplementedError

def mom_growth(monthly):
    """{'YYYY-MM': growth over the previous month as a fraction, None for the first month}."""
    raise NotImplementedError
