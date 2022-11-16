from cryptography.hazmat.primitives import hashes
from os import path
import base64
from cryptography.fernet import Fernet


def hash(input):
    if not isinstance(input, bytes):
        input = input.encode()

    digest = hashes.Hash(hashes.SHA256())
    digest.update(input)
    hash = digest.finalize()

    return hash.hex()


def test_png(header):
    if header.startswith(b"\211PNG\r\n\032\n"):
        return True
    return False


def brute_force(ciphertext):
    ctr = 0
    while True:
        key_bytes = ctr.to_bytes(32, "big")
        key = base64.urlsafe_b64encode(key_bytes)

        # Now initialize the Fernet system with the given key
        # and try to decrypt your challenge.
        # Think, how do you know that the key tested is the correct key
        # (i.e., how do you break out of this infinite loop)?
        try:
            plaintext = Fernet(key).decrypt(ciphertext)
            header = plaintext[:32]
            if test_png(header):

                print(f"Key: {key}")
                with open("BINGO.png", "wb") as file:
                    file.write(plaintext)
                break
        except Exception:
            pass
        ctr += 1
        if not ctr % 1000:
            print(f"[*] Keys tested:{ctr:,}", end="\r")


if __name__ == "__main__":
    filename = hash('pleic_iva') + ".encrypted"
    if not path.exists(filename):
        with open(filename, "wb") as file:
            file.write(b"")
    with open(filename, "rb") as file:
        ciphertext = file.read()
    brute_force(ciphertext)
