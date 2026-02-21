#Royce Daniel 2/19/2026. "Kilometer to mile calculator"
def conversion(Kilos, Miles):
    result = Kilos * 0.6214
    return result

kilometers = float(input("Enter a distance in kilometers: "))
rate = 0.6214
result = conversion(kilometers, rate)

print(kilometers, "In kilometers is", result, "in miles")