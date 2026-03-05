#Computes monthly expense summaries by category.
from collections import defaultdict

def monthly_summary(expenses, year, month):
    """Return category totals for a specific month."""
    summary = defaultdict(float)

    for e in expenses:
        if e["date"].year == year and e["date"].month == month:
            summary[e["category"]] += e["amount"]

    return dict(summary)
