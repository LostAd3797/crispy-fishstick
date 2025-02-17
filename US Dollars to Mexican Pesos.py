exchange_rate = float(input("Enter the exchange rate from dollars to Pesos: "))
conversion = int(input("Enter 0 to convert dollars to Pesos and 1 to convert Pesos to dollars: "))
amount = float(input("Enter the amount: "))

# Check conversion type
if conversion == 0:
    amountPesos = amount * exchange_rate
    print(f"{amount} dollars is {amountPesos:.2f} pesos")
elif conversion == 1:
    amountDollar = amount / exchange_rate
    print(f"{amount} pesos is {amountDollar:.2f} dollars")
else:
    print("Invalid Conversion")
