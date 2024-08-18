base3 = str(input("Enter a base3 number: "))
result = 0

base3 = base3[::-1]

for i in range(0, len(base3)):
    number_to_decimal = int(base3[i]) * 3**i
    result += int(number_to_decimal)
    print(f"{base3[i]} = {base3[i]} x 3^{i} = {number_to_decimal}")

print(f"\nDecimal number: {result}")