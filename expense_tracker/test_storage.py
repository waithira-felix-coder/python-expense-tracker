from storage import add_expense, get_expenses, init_storage

# initialize storage and add a sample expense
init_storage()
add_expense(12.5, 'food', '2026-03-05')
print(get_expenses())
