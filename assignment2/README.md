# Digital Signature 
## Generating Keys

The program `keygen.py` generates a pair of RSA public and private key, prints them in PEM format and stores them in files `public_key.pem` and `private_key.pem` respectively

## Signing

The program `signing.py` takes  
Input form the user:
1. path to a .pem file in which private key is stored
2. a message (that the user wants to sign on)

Output:
prints the signature in hex format

## Verifying 

The program `verification.py` takes
Input:
1. path to a .pem file in which public key is stored
2. signature in hex format
3. the unencrypted message

Output:
If the signature is verified (i.e. the public key can decrypt the encrypted signature and the decrypted message is equal to the unencrypted message)
then prints "Signature Verified!" 

Else it prints "Verification Failed"

## Testing

I have generated a pair of keys by running `keygen.py` and pushed them to this repo in files `public_key.pem` and `private_key.pem`
Then I run `signing.py` on `private_key.pem` to generate a signature for the message "abhimanyu sethia is the best"
The signature generated was (in hex format):  

> 848229c10937179425b250f9b663d274e36bae285812fc44c3ef67d9968fc530720fdf8d5119acae5605be1ac4fef49357b80d1bd27e616de6df9f9fa2a2c01ef1dbad091e8a0daa3f203d188aaa56e2fedd65ad1e63bc78cc2746281a2231f19a53e601453c9f60dbd22f242fdcbd933936ee80a0a4a16b3fb8056693f33cbcc53ef0048d6b00d366c829f9474258dc92b714fb50d1b210dbf4256e8e070ca001bbce0a8350d6d0a1dcc57203f07aeb03bedd3c8e37add7edbf3f297298115508ca0b094bb57c9b6cb23f456d6c256804de74961bb76dbcc6a49467f59edf2ec331f1d95dda62a7b020b2c8da2c6f3d2a37647a2bdb158323d91701252cf361

Then I ran the program `verification.py` with the inputs as above to successfully attain "Signature Verified!"
I also ran the program, by simply altering a few characters of the signature above and/or altering the unencrypted message and attained "Verification Failed!" (as expected)
