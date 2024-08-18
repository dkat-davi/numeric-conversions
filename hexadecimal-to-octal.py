hexadecimal = str(input("Enter a hexadecimal number: ").upper())
binary = ""
result = ""

for i in hexadecimal:
    binary_number = bin(int(i, 16))
    binary += binary_number[2:].zfill(4)
    print(f"{i} = {binary_number[2:].zfill(4)}")

print(f"\nHexadecimal to binary: {binary}\n")

binary = binary[::-1]
position = 0
for i in range(0, len(binary), 3):
    number_binary = binary[i:i+3][::-1]
    decimal = int(number_binary, 2)
    octal = oct(decimal)
    print(f"Octal[{position}]: {number_binary.zfill(3)} -> {octal[2:]}")
    result += octal[2:]
    position += 1

print(f"\nOctal number: {result[::-1]}")