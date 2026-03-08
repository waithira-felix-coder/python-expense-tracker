#Handles saving and retrival of files data in  csv file

import csv
from datetime import datetime
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"
DATA_FILE = DATA_DIR / "expenses.csv"

def init_storage():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    if not DATA_FILE.exists():
        with DATA_FILE.open("w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["amount", "category", "date"])  # header

def add_expense(amount, category, date_val):
    # store date as ISO string
    with DATA_FILE.open("a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([amount, category, date_val])

def get_expenses():
    expenses = []
    if not DATA_FILE.exists():
        return expenses

    with DATA_FILE.open("r", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) != 3:
                continue
            try:
                amount = float(row[0])
                cat = row[1]
                dt = datetime.fromisoformat(row[2])
                expenses.append({"amount": amount, "category": cat, "date": dt})
            except Exception:
                # skip malformed rows
                continue
    return expenses