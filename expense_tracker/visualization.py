# Handles visualization for expenses.

import matplotlib.pyplot as plt

# If it imports from analytics, use relative.
# from .analytics import monthly_summary

def plot_expenses(summary):
    """Generate a bar chart of expenses by category."""
    
    categories = list(summary.keys())
    amounts = list(summary.values())

    fig, ax = plt.subplots(figsize=(10, 6))

    if not amounts:
        ax.text(0.5, 0.5, 'No expenses found for this month', 
                ha='center', va='center', fontsize=14, transform=ax.transAxes)
        ax.set_title("Monthly Spending by Category", fontsize=16, fontweight='bold')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')
    else:
        bars = ax.bar(categories, amounts, color='skyblue', edgecolor='navy', linewidth=1)
        ax.set_title("Monthly Spending by Category", fontsize=16, fontweight='bold')
        ax.set_ylabel("Amount (Ksh)", fontsize=12)
        ax.set_xlabel("Category", fontsize=12)
        
        # Add value labels on bars
        max_amount = max(amounts)
        for bar, amount in zip(bars, amounts):
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + max_amount*0.01, 
                    f'Ksh{amount:.2f}', ha='center', va='bottom', fontsize=10, fontweight='bold')
        
        # Rotate x labels if many categories
        if len(categories) > 5:
            plt.xticks(rotation=45, ha='right')
    
    plt.tight_layout()

    return fig
