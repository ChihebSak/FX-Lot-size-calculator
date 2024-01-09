import tkinter as tk
from tkinter import ttk
import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'
def calculate_lot_size():
    try:
        risk_percentage = float(entry_risk.get())
        account_balance = float(entry_balance.get())
        market_spread = float(entry_spread.get())
        entry_price = float(entry_entry_price.get())
        stop_loss_price = float(entry_stop_loss.get())

        risk_amount = (account_balance * risk_percentage) / 100
        trade_size = risk_amount / (entry_price - stop_loss_price - market_spread)

        result_label.config(text=f"Lot Size: {trade_size:.2f}")
    except ValueError:
        result_label.config(text="Please enter valid numeric values.")

# Create main window
window = tk.Tk()
window.title("Lot Size Calculator")
style = ttk.Style()
style.theme_use('default')
# Create and place widgets
label_risk = ttk.Label(window, text="Risk Percentage:")
label_risk.grid(row=0, column=0, padx=10, pady=10)
entry_risk = ttk.Entry(window)
entry_risk.grid(row=0, column=1, padx=10, pady=10)

label_balance = ttk.Label(window, text="Account Balance:")
label_balance.grid(row=1, column=0, padx=10, pady=10)
entry_balance = ttk.Entry(window)
entry_balance.grid(row=1, column=1, padx=10, pady=10)

label_spread = ttk.Label(window, text="Market Spread:")
label_spread.grid(row=2, column=0, padx=10, pady=10)
entry_spread = ttk.Entry(window)
entry_spread.grid(row=2, column=1, padx=10, pady=10)

label_entry_price = ttk.Label(window, text="Entry Price:")
label_entry_price.grid(row=3, column=0, padx=10, pady=10)
entry_entry_price = ttk.Entry(window)
entry_entry_price.grid(row=3, column=1, padx=10, pady=10)

label_stop_loss = ttk.Label(window, text="Stop Loss Price:")
label_stop_loss.grid(row=4, column=0, padx=10, pady=10)
entry_stop_loss = ttk.Entry(window)
entry_stop_loss.grid(row=4, column=1, padx=10, pady=10)

calculate_button = ttk.Button(window, text="Calculate Lot Size", command=calculate_lot_size)
calculate_button.grid(row=5, column=0, columnspan=2, pady=20)

result_label = ttk.Label(window, text="")
result_label.grid(row=6, column=0, columnspan=2, pady=10)

# Start the main loop
window.mainloop()
