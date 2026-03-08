# filepath: c:\Users\PC\Desktop\expence-tracker\expense_tracker\main.py
# Main entry point for the Expense Tracker web application. Initializes storage and launches the Flask app.

from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import date
from .storage import init_storage, add_expense, get_expenses
from .analytics import monthly_summary
from .visualization import plot_expenses
import os
import matplotlib.pyplot as plt
import time

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this to a random secret key

@app.route('/', methods=['GET', 'POST'])
def index():
    init_storage()
    today = date.today().isoformat()
    return render_template('index.html', today=today)

@app.route('/add', methods=['POST'])
def add():
    try:
        amount = float(request.form['amount'])
        category = request.form['category']
        date_val = request.form['date']

        add_expense(amount, category, date_val)

        flash('Expense added successfully!', 'success')
    except Exception as e:
        flash(f'Error: {str(e)}', 'danger')

    return redirect(url_for('index'))

@app.route('/summary')
def summary():
    from datetime import datetime

    expenses = get_expenses()
    now = datetime.now()

    summary_data = monthly_summary(expenses, now.year, now.month)

    fig = plot_expenses(summary_data)
    fig.savefig(os.path.join(app.root_path, 'static', 'summary.png'))
    plt.close(fig)  # Close to free memory

    return render_template('summary.html', summary=summary_data, timestamp=time.time())
#routes here
if __name__ == "__main__":
   # app.run(debug=True)
    app.run(host=0.0.0.0, port=5000)

