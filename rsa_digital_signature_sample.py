import hashlib
import rsa


public_key, private_key = rsa.newkeys(2048)


def create_signature(message, private_key):
    hashed_message = hashlib.sha256(message.encode()).digest()
    signature = rsa.sign(hashed_message, private_key, 'SHA-256')
    return signature


def verify_signature(message, signature, public_key):
    hashed_message = hashlib.sha256(message.encode()).digest()
    try:
        rsa.verify(hashed_message, signature, public_key)
        print("Signature is valid.")
    except rsa.VerificationError:
        print("Signature is invalid.")


message = "Hello, World!"
signature = create_signature(message, private_key)
print("Digital Signature:", signature)

verify_signature(message, signature, public_key)
