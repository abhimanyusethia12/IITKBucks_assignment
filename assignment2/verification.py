
print("Welcome to Abhimanyu's RSA Signature Verifier \n ***************************\n")

#retrieving and deserialisation of public key
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.hazmat.backends import default_backend

public_key_path = input("Please enter path to public key file (.pem): ")
public_key_file = open(public_key_path,"rb")

public_key = load_pem_public_key(
    public_key_file.read(), 
    backend=default_backend()
)

#taking user input of sign in hex form and converting to bytes for verify function
signature_hex = input("Enter signature in hex format: ")
signature = bytes.fromhex(signature_hex)

#taking input message
message = input("Enter the unencrypted message: ")

#verifying
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature
try:    
    public_key.verify(
        signature,
        message.encode(),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Signature Verified!")
except InvalidSignature:
    print("Verification Failed!")

