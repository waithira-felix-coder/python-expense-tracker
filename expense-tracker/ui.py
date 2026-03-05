# Main UI for the Expense Tracker application using Tkinter.

import tkinter as tk
from tkinter import messagebox
from datetime import date
from storage import add_expense, get_expenses
from analytics import monthly_summary
from visualization import plot_expenses
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ExpenseApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        self.root.geometry("600x500")

        self.build_form()
        self.build_buttons()

    def build_form(self):

        tk.Label(self.root, text="Amount").pack()
        self.amount = tk.Entry(self.root)
        self.amount.pack()

        tk.Label(self.root, text="Category").pack()
        self.category = tk.Entry(self.root)
        self.category.pack()

        tk.Label(self.root, text="Date (YYYY-MM-DD)").pack()
        self.date = tk.Entry(self.root)
        self.date.insert(0, str(date.today()))
        self.date.pack()

    def build_buttons(self):

        tk.Button(self.root, text="Add Expense", command=self.add).pack(pady=5)
        tk.Button(self.root, text="Show Summary", command=self.show_summary).pack(pady=5)

    def add(self):

        try:
            amount = float(self.amount.get())
            category = self.category.get()
            date_val = self.date.get()

            add_expense(amount, category, date_val)

            messagebox.showinfo("Success", "Expense added")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def show_summary(self):

        from datetime import datetime

        expenses = get_expenses()
        now = datetime.now()

        summary = monthly_summary(expenses, now.year, now.month)

        fig = plot_expenses(summary)

        window = tk.Toplevel(self.root)

        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().pack()
