decimal = int(input("Enter a decimal number: "))
result = ""

while decimal > 0: 
    remainder = decimal % 16
    print(f"{decimal} / 16 = {decimal // 16} -> remainder: {remainder}")
    decimal = decimal // 16
    result += str(hex(remainder)).upper()[2:]

print(f"\nHexadecimal number: {result[::-1]}")