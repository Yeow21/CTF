input_file = "flag.lc"
output_file = "decrypted_output"

with open(input_file, "rb") as file:
    encrypted_data = file.read()
decrypted_bytes = b''

# initialise the first byte to decrypt to length of encrypted data
currentByte = len(encrypted_data) - 1

decrypted_bytes += bytes([encrypted_data[currentByte] ^ 0x1a])

currentByte = currentByte - 1
i = 0

while currentByte > -1:
    decrypted_bytes += bytes([decrypted_bytes[i] ^ encrypted_data[currentByte]])
    currentByte = currentByte - 1
    i += 1

decrypted_bytes_final = b''
# Reversed bytes object
decrypted_bytes_final = decrypted_bytes[::-1]

print(decrypted_bytes_final[0:100])
print(decrypted_bytes[-1:-100])

# Output file name
output_file = "decrypted_file"

# Write the PNG signature to the output file
with open(output_file, "wb") as file:
    file.write(decrypted_bytes_final)
