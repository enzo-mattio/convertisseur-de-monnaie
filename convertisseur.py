import tkinter as tk

import requests
    

# fonction pour convertir les devises
def convert_currency(amount, from_currency, to_currency):

    # utiliser l'api open exchange rates
    url = f"https://openexchangerates.org/api/latest.json?app_id=b3d9268b928840ecb1ac63cb37e0f712"
    response = requests.get(url)
    data = response.json()
    rates = data["rates"]

    # convertir la devise
    from_rate = rates[from_currency]
    to_rate = rates[to_currency]
    converted_amount = amount * (to_rate / from_rate)
    return converted_amount
def convert():
    # obtenir les valeurs des entrées
    amount = float(amount_entry.get())
    from_currency = from_var.get()
    to_currency = to_var.get()

    # effectuer la conversion
    converted_amount = convert_currency(amount, from_currency, to_currency)

    # afficher le résultat dans la zone de sortie
    output_label.config(text=str(converted_amount))
    return converted_amount

# créer une fenêtre tkinter
root = tk.Tk()
root.title("Convertisseur de devises")

# créer des entrées pour le montant à convertir et les devises
amount_label = tk.Label(root, text="Montant à convertir :")
amount_entry = tk.Entry(root)
from_label = tk.Label(root, text="De :")
from_var = tk.StringVar(root)
from_var.set("EUR")  # définit la devise par défaut
from_dropdown = tk.OptionMenu(root, from_var, "USD", "EUR", "GBP", "JPY")
to_label = tk.Label(root, text="À :")
to_var = tk.StringVar(root)
to_var.set("USD")  # définit la devise par défaut
to_dropdown = tk.OptionMenu(root, to_var, "USD", "EUR", "GBP", "JPY")

# créer un bouton de conversion
convert_button = tk.Button(root, text="Convertir", command=convert)

# créer une zone pour afficher le résultat
output_label = tk.Label(root, text="")

# positionner les éléments dans la fenêtre
amount_label.grid(row=0, column=0)
amount_entry.grid(row=0, column=1)
from_label.grid(row=1, column=0)
from_dropdown.grid(row=1, column=1)
to_label.grid(row=2, column=0)
to_dropdown.grid(row=2, column=1)
convert_button.grid(row=3, column=0, columnspan=2)
output_label.grid(row=4, column=0, columnspan=2)

root.mainloop()
