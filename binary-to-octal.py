binary = str(input("Enter a binary number: "))
result = ""

binary = binary[::-1]
position = 0
for i in range(0, len(binary), 3):
    number_binary = binary[i:i+3][::-1]
    decimal = int(number_binary, 2)
    octal = oct(decimal)
    print(f"\nOctal[{position}]: {number_binary} -> {octal[2:]}")
    result += octal[2:]
    position += 1

print(f"\nOctal number: {result[::-1]}")