import hashlib

prefix = 'zero2hero'
nonce = 0
twoZero = False

while True:
    input_str = prefix + str(nonce)
    hash_str = hashlib.sha256(input_str.encode()).hexdigest()
 
    if hash_str.startswith('00000'):
        print(f"Found nonce: {nonce}")
        print(f"Hash value: {hash_str}")
        break   
    elif hash_str.startswith('00') and not twoZero:
        print(f"Found nonce: {nonce}")
        print(f"Hash value: {hash_str}")
        twoZero = True

    nonce += 1