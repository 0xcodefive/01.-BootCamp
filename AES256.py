from Crypto.Cipher import AES
import hashlib
import binascii
import base64

def keyBySHA256(key):
    return '0x' + hashlib.sha256(key.encode()).hexdigest()

# def encryptAES256(message, hex_key):
#     if hex_key.startswith('0x'):
#         hex_key = hex_key[2:]
#     key = binascii.unhexlify(hex_key)
#     hash_key = hashlib.sha256(key).digest()
#     aes = AES.new(hash_key, AES.MODE_ECB)
#     message = message.encode('utf-8')
#     message += b"\0" * (AES.block_size - len(message) % AES.block_size)
#     encrypted_message = aes.encrypt(message)
#     return base64.b64encode(encrypted_message).decode('utf-8')

# def decryptAES256(encoded_message, hex_key):
#     if hex_key.startswith('0x'):
#         hex_key = hex_key[2:]
#     key = binascii.unhexlify(hex_key)
#     hash_key = hashlib.sha256(key).digest()
#     cipher = AES.new(hash_key, AES.MODE_ECB)
#     decoded_message = base64.b64decode(encoded_message)
#     decrypted_message = cipher.decrypt(decoded_message)
#     return decrypted_message.rstrip(b"\0").decode('utf-8')

def encryptAES256(message, hex_key):
    if hex_key.startswith('0x'):
        hex_key = hex_key[2:]
    key = binascii.unhexlify(hex_key)
    hash_key = hashlib.sha256(key).digest()
    cipher = AES.new(hash_key, AES.MODE_ECB)
    BS = AES.block_size
    pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
    raw = base64.b64encode(pad(message).encode('utf8'))
    return base64.b64encode(cipher.encrypt(raw))

def decryptAES256(encoded_message, hex_key):
    if hex_key.startswith('0x'):
        hex_key = hex_key[2:]
    key = binascii.unhexlify(hex_key)
    hash_key = hashlib.sha256(key).digest()
    cipher = AES.new(hash_key, AES.MODE_ECB)
    unpad = lambda s: s[:-ord(s[-1:])]
    enc = base64.b64decode(encoded_message)
    cipher = AES.new(hash_key, AES.MODE_ECB)
    return unpad(base64.b64decode(cipher.decrypt(enc)).decode('utf8'))

message = 'Я уверен, что в процессе обучения ты получишь не только ценные знания и навыки, но и найдешь единомышленников, которые помогут в реализации твоих планов и идей. Не стоит бояться трудностей и неудач, ведь именно на них мы получаем ценный опыт и знания. Продолжай двигаться вперед и не сдавайся, ведь успех ждет тех, кто не боится трудностей и готов бороться за свои цели.'
key = '0xc0de'

hashed_key = keyBySHA256(key)
print(hashed_key)

encrypted_message = encryptAES256(message, hashed_key)
print(encrypted_message)

decrypt_message = decryptAES256(encrypted_message, hashed_key)
print(decrypt_message)