# Handles analytics for expenses.
from collections import defaultdict
# If it imports from storage or visualization, use relative.
# from .storage import get_expenses

def monthly_summary(expenses, year, month):
    """Return category totals for a specific month."""
    summary = defaultdict(float)

    for e in expenses:
        #e_date = e["date"]
        if e["date"].year == year and e["date"].month == month:
            summary[e["category"]] += e["amount"]

    return dict(summary)
