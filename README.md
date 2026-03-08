# Expense Tracker

A modern, web-based expense tracking application built with Python Flask and Bootstrap. Track your daily expenses, categorize spending, and visualize your financial data with interactive charts.

##  Features

- **Web-Based Interface**: Clean, responsive web application with Bootstrap styling
- **Expense Management**: Add, view, and categorize expenses with date tracking
- **Data Visualization**: Interactive bar charts showing spending by category
- **Monthly Summary**: View expenses for the current month with detailed breakdowns
- **CSV Data Storage**: Persistent data storage in CSV format
- **Real-time Updates**: Automatic chart updates when adding new expenses
- **Responsive Design**: Works seamlessly on desktop and mobile devices

##  Requirements

- Python 3.8 or higher
- pip (Python package installer)
- Modern web browser

##  Installation

### 1. Clone or Download the Project

```bash
git clone <repository-url>
cd expense-tracker
```

### 2. Create Virtual Environment

```bash
# On Windows
python -m venv .venv
.venv\Scripts\activate

# On macOS/Linux
python -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install flask matplotlib
```

### 4. Run the Application

```bash
python -m expense_tracker.main
```

The application will start at `http://127.0.0.1:5000/`

##  Usage

### Adding Expenses

1. Open your web browser and navigate to `http://127.0.0.1:5000/`
2. Fill in the expense form:
   - **Amount**: Enter the expense amount (supports decimals)
   - **Category**: Choose or enter a category (e.g., Food, Travel, Entertainment)
   - **Date**: Select the date of the expense
3. Click "Add Expense" to save

### Viewing Summary

1. Click the "Show Summary" button on the main page
2. View your monthly expense breakdown:
   - **Category List**: Detailed list with amounts for each category
   - **Visual Chart**: Bar chart showing spending distribution
   - **Total Overview**: Quick glance at your spending patterns

##  Project Structure

```
expense-tracker/
├── expense_tracker/
│   ├── __init__.py
│   ├── main.py          # Flask application and routes
│   ├── storage.py       # CSV data handling
│   ├── analytics.py     # Expense analysis functions
│   ├── visualization.py # Chart generation
│   ├── ui.py           # (Legacy Tkinter UI - not used in web version)
│   ├── test_storage.py
│   ├── templates/      # HTML templates
│   │   ├── index.html
│   │   └── summary.html
│   └── static/         # Static files (CSS, JS, images)
├── data/
│   └── expenses.csv    # Expense data storage
├── pyproject.toml      # Project configuration
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## 🛠️ Technologies Used

- **Backend**: Python Flask
- **Frontend**: HTML5, Bootstrap 5
- **Data Visualization**: Matplotlib
- **Data Storage**: CSV files
- **Styling**: Bootstrap CSS Framework

## 🔧 Configuration

### Data Storage Location

Expenses are stored in `data/expenses.csv` in the project root directory. The file is automatically created when you first run the application.

### Port Configuration

The application runs on `http://127.0.0.1:5000/` by default. To change the port, modify the `app.run()` call in `main.py`.

##  Troubleshooting

### Common Issues

1. **"Module not found" errors**:
   - Ensure you're in the virtual environment: `.venv\Scripts\activate` (Windows)
   - Install dependencies: `pip install -r requirements.txt`

2. **Application won't start**:
   - Check if port 5000 is available
   - Ensure all dependencies are installed
   - Check for Python version compatibility

3. **Charts not displaying**:
   - Ensure matplotlib is installed
   - Check that the `static/` directory exists
   - Clear browser cache

4. **Data not saving**:
   - Check write permissions for the `data/` directory
   - Ensure the CSV file is not open in another application

### Debug Mode

For development, the app runs in debug mode which provides detailed error messages. In production, set `debug=False` in `main.py`.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and test thoroughly
4. Commit your changes: `git commit -am 'Add new feature'`
5. Push to the branch: `git push origin feature-name`
6. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙋 Support

If you encounter any issues or have questions:

1. Check the troubleshooting section above
2. Review the code comments for implementation details
3. Open an issue on the project repository

## 📈 Future Enhancements

- [ ] User authentication and multiple user support
- [ ] Expense categories management
- [ ] Budget setting and tracking
- [ ] Export functionality (PDF, Excel)
- [ ] Advanced analytics and trends
- [ ] Mobile app version
- [ ] API endpoints for integrations

---

**Happy expense tracking!** 💰📊
