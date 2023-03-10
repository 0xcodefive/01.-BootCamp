from Crypto.Cipher import AES
import hashlib
import base64

def keyBySHA256(key):
    return '0x' + hashlib.sha256(key.encode()).hexdigest()

def pad(data):
        while len(data) % AES.block_size != 0:
            data = data + ' '
        return data.encode('utf8')

def encryptAES256(message, hex_key):
    if hex_key.startswith('0x'):
        hex_key = hex_key[2:]
    key = bytes.fromhex(hex_key)
    cipher = AES.new(key, AES.MODE_ECB)
    raw = base64.b64encode(pad(message))
    return base64.b64encode(cipher.encrypt(plaintext=raw))

def decryptAES256(encoded_message, hex_key):
    if hex_key.startswith('0x'):
        hex_key = hex_key[2:]
    key = bytes.fromhex(hex_key)
    cipher = AES.new(key, AES.MODE_ECB)
    enc = base64.b64decode(encoded_message)
    return base64.b64decode(cipher.decrypt(enc)).decode('utf8')

message = 'Я уверен, что в процессе обучения ты получишь не только ценные знания и навыки, но и найдешь единомышленников, которые помогут в реализации твоих планов и идей. Не стоит бояться трудностей и неудач, ведь именно на них мы получаем ценный опыт и знания. Продолжай двигаться вперед и не сдавайся, ведь успех ждет тех, кто не боится трудностей и готов бороться за свои цели.'
key = '0xc0de'

hashed_key = keyBySHA256(key)
print(hashed_key)

encrypted_message = encryptAES256(message, hashed_key)
print(encrypted_message)

# encrypted_message = b'j30Vwd0yu/51iiO1kHjJgg1YAhH+yzg3I56EV4hNuVLuj99gOXYvRnGThR7d28rZf7ASUR4P7j1ZCc/y4GqadJifJRwqy6BjWSCOkkLFJn+82b+MUJLsCLYp1NM9MCUkEjozgFRGNZymkJokRCzbeAs7yQrMEes8SFOtNmF4+btNlsk6MADAcGoX3VZRzfnGQzX3d1lsz1xEaGW5/phGDTfwExjYDf5sCF8VAyPDtRiy1RYDwnXj8VrGa5coLY8uxpcZUz3TvI3mrPCKaJXd+0zyTPTDdnBmsBARIaaZFefXxriRwG/HAIb4WpUkP00HCbWSTKqrtvRPTwR5g4y6h0ZzzaN+SvlZLhyXkABbPnoc05lkctlKte2Ie4YXXLS38dFxzHA9fhFUCju34lk2weMg4y8or5EV132ebWM3kCAe2NTK8KeNlVl0RWoc4G3istUxZlAk6scZFx8JCL99cw0+REFi6aKk70Rfa2LMPMVEC7iBxhyL0bobsXSr2Xso0xP7ViWMOZVTkRwffE91z42R6USapzjaaTP/jXtrCNW8l3AZQWFdVj8ECW26Rqu6yap0A/L2o0ZRUYfCWnbiIxpJzHPbfBhj4NyMLWw4KSXdcJvQAuJ+mkcx5J5KENJNcSncsEmzIusktFg756WsartwX0ZPJiyH9xx9/O+7GaCVOm+MFswnO9v1Kfd51/ZgYCBsqYJO29iO1g0o9TZS+s1nxLlmsI6bN3/+2yYI5pczBfbDi3FeTNiu1GxhK2PeUYCRXq2weJVv4Lh+EsKvuR7Y1Mrwp42VWXRFahzgbeLvqwi2fZcf+LUH8ggRzPJSTr2Nbw/n9bLglcL3AeWWN4o/PVEXhfu3s0cYYRKrOSAafif72cBXvs57Go4+pG80'
decrypt_message = decryptAES256(encrypted_message, hashed_key)
print(decrypt_message)