# Rendering Transaction Details from its Binary file

## Input
The program assignment4-updated.py asks for the path to a .dat file consisting of a transaction's details in binary format (with its name as <transaction ID in hex format>.dat)

The file must have binary data as mentioned in assignment 3 

> For testing, I created 0ab9c878d6661f9fc7f4f70035bf96054ecd7fed01e9850c6493edd4bf19c518.dat file (by running ../assignment3/assignment3.py program) and pushed it to this folder

## Output

The program prints the details of the transaction in the follwoing format

Transaction ID: in hex format

Number of inputs: an integer

    Input 1:
    
        Transaction ID: <in hex format>
        Index: <an integer>
        Length of the signature: <an integer>
        Signature: <in hex format>
    Input 2:
        Transaction ID: <in hex format>
        Index: <an integer>
        Length of the signature: <an integer>
        Signature: <in hex format>
    ...
Number of outputs: an integer

    Output 1:
        Number of coins: <an integer>
        Length of public key: <an integer>
        Public key: <in PEM format>
    Output 2:
        Number of coins: <an integer>
        Length of public key: <an integer>
        Public key: <in PEM format>
    ...
