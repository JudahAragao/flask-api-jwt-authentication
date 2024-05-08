import hashlib
import binascii

def verify_password(password, hash):
    parts = hash.split('$')
    if len(parts) == 3:
        algorithm, salt, stored_hash = parts
        iterations = 260000  # Defina um valor padrão para iterações se não estiver presente
    elif len(parts) == 4:
        algorithm, iterations, salt, stored_hash = parts
        iterations = int(iterations)
    else:
        raise ValueError("Formato de hash inválido")
    
    new_hash = hashlib.pbkdf2_hmac(algorithm.split(':')[1], password.encode('utf-8'), salt.encode('utf-8'), iterations)

    return new_hash == binascii.unhexlify(stored_hash)

password = "judah.bem.hur"
stored_password = "pbkdf2:sha256:260000$GzMkSHhuUAKtWZ0n$99c44f68f7e4116d4910d8e4d8a629ffe63213d0454b9354082332ee8cfe79fc"
print(verify_password(password, stored_password))
