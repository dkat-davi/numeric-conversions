binary = str(input("Enter a binary number: "))
result = 0

binary = binary[::-1]

for i in range(0, len(binary)):
    number_to_decimal = int(binary[i]) * 2**i
    result += int(number_to_decimal)
    print(f"{binary[i]} = {binary[i]} x 2^{i} = {number_to_decimal}")

print(f"\nDecimal number: {result}")