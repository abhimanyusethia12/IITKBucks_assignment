import hashlib

input_string = input("please enter the string (to which integers will be appended):")
edited_strings = []
target_string = '0000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'
target_int = int(target_string,16)
i=1
while True:
    edited_strings += [input_string + str(i)]
    hash_bytes = hashlib.sha256(edited_strings[i-1].encode())
    hash_hexadecimal = ''
    hash_hexadecimal = hash_bytes.hexdigest()
    if(int(hash_hexadecimal,16)<target_int):
        break
    i += 1
print(edited_strings[i-1])
