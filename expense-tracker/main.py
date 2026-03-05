# Main entry point for the Expense Tracker application. Initializes storage and launches the UI.

import tkinter as tk
from storage import init_storage
from ui import ExpenseApp

def main():

    init_storage()

    root = tk.Tk()
    app = ExpenseApp(root)

    root.mainloop()

if __name__ == "__main__":
    main()
