decimal = int(input("Enter a decimal number: "))
result = str(decimal % 2)

while decimal > 0: 
    print(f"{decimal} / 2 = {decimal // 2} -> remainder: {decimal % 2}")
    decimal = decimal // 2
    result += str(decimal % 2)

print(f"\nBinary number: {int(result[::-1])}")