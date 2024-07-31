import tkinter as tk
from tkinter import ttk

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
        self.root.geometry("300x300")

        self.rates = {
            'USD': {'EUR': 0.91, 'GBP': 0.77, 'JPY': 141.42, 'INR': 87.18},
            'EUR': {'USD': 1.10, 'GBP': 0.85, 'JPY': 155.22, 'INR': 91.33},
            'GBP': {'USD': 1.30, 'EUR': 1.17, 'JPY': 181.45, 'INR': 106.77},
            'JPY': {'USD': 0.0071, 'EUR': 0.0064, 'GBP': 0.0055, 'INR': 0.59},
            'INR': {'USD': 0.012, 'EUR': 0.011, 'GBP': 0.0094, 'JPY': 1.69}
        }

        self.create_widgets()

    def create_widgets(self):
 
        self.amount_label = tk.Label(self.root, text="Amount:")
        self.amount_label.pack(pady=5)
        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.pack(pady=5)

        self.from_currency_label = tk.Label(self.root, text="From Currency:")
        self.from_currency_label.pack(pady=5)
        self.from_currency = ttk.Combobox(self.root, values=list(self.rates.keys()))
        self.from_currency.pack(pady=5)
        self.from_currency.set('USD')  

        self.to_currency_label = tk.Label(self.root, text="To Currency:")
        self.to_currency_label.pack(pady=5)
        self.to_currency = ttk.Combobox(self.root, values=list(self.rates.keys()))
        self.to_currency.pack(pady=5)
        self.to_currency.set('INR') 

        self.convert_button = tk.Button(self.root, text="Convert", command=self.convert_currency)
        self.convert_button.pack(pady=10)
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack(pady=5)

    def convert_currency(self):
        try:
            amount = float(self.amount_entry.get())
            from_currency = self.from_currency.get()
            to_currency = self.to_currency.get()

            if from_currency == to_currency:
                self.result_label.config(text="Same currency selected.")
                return

            rate = self.rates[from_currency].get(to_currency)
            if rate:
                converted_amount = amount * rate
                self.result_label.config(text=f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
            else:
                self.result_label.config(text="Conversion rate not available.")
        except ValueError:
            self.result_label.config(text="Please enter a valid number.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()
