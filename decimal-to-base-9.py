decimal = int(input("Enter a decimal number: "))
result = str(decimal % 9)

while decimal > 0: 
    print(f"{decimal} / 9 = {decimal // 9} -> remainder: {decimal % 9}")
    decimal = decimal // 9
    result += str(decimal % 9)

print(f"\nBase 9 number: {int(result[::-1])}")