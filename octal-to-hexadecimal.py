octal = str(input("Enter a octal number: "))
binary = ""
result = ""

for i in octal:
    binary_number = bin(int(i, 8))
    binary += binary_number[2:].zfill(3)
    print(f"{i} = {binary_number[2:].zfill(3)}")

print(f"\nOctal to binary: {binary}\n")

binary = binary[::-1]
position = 0
for i in range(0, len(binary), 4):
    number_binary = binary[i:i+4][::-1]
    decimal = int(number_binary, 2)
    hexadecimal = hex(decimal)
    print(f"Hexadecimal[{position}]: {number_binary.zfill(4)} -> {hexadecimal[2:].upper()}")
    result += hexadecimal[2:]
    position += 1

result = result.rstrip('0')

print(f"\nHexadecimal number: {result.upper()[::-1]}")