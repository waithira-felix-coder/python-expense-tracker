#Handles saving and retrieval of expenses using a CSV file.

import csv
import os
from datetime import datetime

FILE_PATH = "data/expenses.csv"

HEADERS = ["amount", "category", "date"]

def init_storage():
    """Create CSV file if it does not exist."""
    os.makedirs("data", exist_ok=True)
    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(HEADERS)

def add_expense(amount, category, date):
    """Add expense to CSV."""
    with open(FILE_PATH, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([amount, category, date])

def get_expenses():
    """Retrieve all expenses."""
    expenses = []
    with open(FILE_PATH, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["amount"] = float(row["amount"])
            row["date"] = datetime.strptime(row["date"], "%Y-%m-%d")
            expenses.append(row)
    return expenses
