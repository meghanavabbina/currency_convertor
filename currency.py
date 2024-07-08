# Define a dictionary with exchange rates
exchange_rates = {
    'USD': 1.0,
    'EUR': 0.85,
    'GBP': 0.73,
    'JPY': 110.4,
    'IND':83.32,
}

# Function to convert from one currency to another
def convert_currency(amount, from_currency, to_currency):
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        return "Currency not supported"
    
    conversion_rate = exchange_rates[to_currency] / exchange_rates[from_currency]
    converted_amount = amount * conversion_rate
    return converted_amount

# Main program
while True:
    try:
        amount = float(input("Enter the amount: "))
        from_currency = input("Enter the currency you're converting from (e.g., USD, EUR): ").upper()
        to_currency = input("Enter the currency you want to convert to (e.g., USD, EUR): ").upper()

        result = convert_currency(amount, from_currency, to_currency)
        if result != "Currency not supported":
            print(f"{amount} {from_currency} is equal to {result} {to_currency}")
        else:
            print(result)
        
        another_conversion = input("Do you want to perform another conversion? (yes/no): ").lower()
        if another_conversion != 'yes':
            break
    except ValueError:
        print("Invalid input. Please enter a valid numeric amount.")
