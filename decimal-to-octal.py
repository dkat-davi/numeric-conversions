decimal = int(input("Enter a decimal number: "))
result = str(decimal % 8)

while decimal > 0: 
    print(f"{decimal} / 8 = {decimal // 8} -> remainder: {result}")
    decimal = decimal // 8
    result += str(decimal % 8)

print(f"\nOctal number: {int(result[::-1])}")