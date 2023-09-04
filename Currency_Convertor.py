import tkinter as tk
import requests

# Function to fetch exchange rate data from the API
def get_exchange_rates():
    response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")

    if response.status_code == 200:
        data = response.json()
        rates = data.get('rates', {})
        return rates
    else:
        return None

# Function to perform currency conversion
def convert_currency():
    amount = float(amount_entry.get())
    from_currency = from_currency_entry.get().upper()
    to_currency = to_currency_entry.get().upper()

    exchange_rates = get_exchange_rates()

    if exchange_rates:
        if from_currency == to_currency:
            converted_amount_label.config(text=f"{amount} {from_currency} = {amount} {to_currency}")
        else:
            rate_from = exchange_rates.get(from_currency)
            rate_to = exchange_rates.get(to_currency)
            if rate_from and rate_to:
                converted_amount = (amount / rate_from) * rate_to
                converted_amount_label.config(text=f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
            else:
                converted_amount_label.config(text="Invalid currency code")
    else:
        converted_amount_label.config(text="Failed to fetch exchange rates")

# Create the main window
window = tk.Tk()
window.title("Currency Converter")

# Labels and entry fields
tk.Label(window, text="Amount:").grid(row=0, column=0)
amount_entry = tk.Entry(window)
amount_entry.grid(row=0, column=1)

tk.Label(window, text="From Currency (e.g., USD):").grid(row=1, column=0)
from_currency_entry = tk.Entry(window)
from_currency_entry.grid(row=1, column=1)

tk.Label(window, text="To Currency (e.g., EUR):").grid(row=2, column=0)
to_currency_entry = tk.Entry(window)
to_currency_entry.grid(row=2, column=1)

# Convert button
convert_button = tk.Button(window, text="Convert", command=convert_currency)
convert_button.grid(row=3, columnspan=2)

# Converted amount label
converted_amount_label = tk.Label(window, text="")
converted_amount_label.grid(row=4, columnspan=2)

# Run the main loop
window.mainloop()
