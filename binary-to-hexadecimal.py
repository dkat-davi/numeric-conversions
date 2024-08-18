binary = str(input("Enter a binary number: "))
result = ""

binary = binary[::-1]
position = 0
for i in range(0, len(binary), 4):
    number_binary = binary[i:i+4][::-1]
    decimal = int(number_binary, 2)
    hexadecimal = hex(decimal)
    print(f"Hexadecimal[{position}]: {number_binary.zfill(4)} -> {hexadecimal[2:].upper()}")
    result += hexadecimal[2:]
    position += 1

print(f"\nHexadecimal number: {result[::-1].upper()}")