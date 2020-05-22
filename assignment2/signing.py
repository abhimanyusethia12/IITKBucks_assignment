print("Welcome to Abhimanyu's RSA signer! \n *******************")

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

#retrieving and deserialising private key from a .pem file
private_key_path = input("Enter path to private key file (.pem): ")
with open(private_key_path, "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()
    )

#asking user for message and signing the message using the private key obtained above
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

message = input("Enter message to be signed: ")
message_in_bytes = message.encode()
signature = private_key.sign(
    message_in_bytes,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

print(signature.hex())