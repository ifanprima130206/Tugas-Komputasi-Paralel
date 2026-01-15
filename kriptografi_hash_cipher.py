import hashlib
import binascii


def derive_keystream(key: bytes, length: int) -> bytes:
    keystream = b""
    counter = 0

    while len(keystream) < length:
        counter_bytes = counter.to_bytes(4, "big")
        block = hashlib.sha256(key + counter_bytes).digest()
        keystream += block
        counter += 1

    return keystream[:length]


def xor_bytes(a: bytes, b: bytes) -> bytes:
    return bytes(x ^ y for x, y in zip(a, b))


def encrypt(message: str, password: str) -> str:
    msg_bytes = message.encode("utf-8")
    key_bytes = password.encode("utf-8")

    keystream = derive_keystream(key_bytes, len(msg_bytes))
    cipher_bytes = xor_bytes(msg_bytes, keystream)

    return binascii.hexlify(cipher_bytes).decode("ascii")


def decrypt(cipher_hex: str, password: str) -> str:
    cipher_bytes = binascii.unhexlify(cipher_hex)
    key_bytes = password.encode("utf-8")

    keystream = derive_keystream(key_bytes, len(cipher_bytes))
    plain_bytes = xor_bytes(cipher_bytes, keystream)

    return plain_bytes.decode("utf-8")


if __name__ == "__main__":
    pesan = input("Masukkan pesan: ")
    kunci = input("Masukkan password: ")

    cipher = encrypt(pesan, kunci)
    print("\nCipher (hex):", cipher)

    recovered = decrypt(cipher, kunci)
    print("Hasil dekripsi:", recovered)
