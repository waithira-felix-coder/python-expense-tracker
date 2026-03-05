#Generates visualizations of expense data, such as pie charts for category breakdowns with matplotlib.

import matplotlib.pyplot as plt

def plot_expenses(summary):
    """Generate a pie chart of expenses by category."""
    
    categories = list(summary.keys())
    amounts = list(summary.values())

    fig, ax = plt.subplots()

    ax.pie(amounts, labels=categories, autopct='%1.1f%%')
    ax.set_title("Monthly Spending by Category")

    return fig
