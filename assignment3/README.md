# A Cryptocurrency Transaction Model

The program assignment3_updated.py asks for transaction data and creates a binary file for that transaction. 

The program first asks for the number of inputs (to be entered as an integer), and for each input, it asks for- 

> a transaction ID (to be entered in hex format), 

> the index (to be entered as an integer), and 

> a signature (to be entered in hex format). 

Then it asks for the number of outputs (to be entered as an integer), and for each output, it asks for-

> the number of coins (to be entered as a 64-bit integer)

> and the path of a public key (.pem) file.

NOTE: An example .pem file is also provided in this folder (public_key.pem)

Then it creates the transaction data in binary format, calculates its hash (the transaction ID) and then saves this binary data into a file named <the calculated transaction ID in hex format>.dat.

P.S. Currently the program doesn't verify the transaction data. Just accepts whatever the user gives.
P.S.S. the program was run with some random data and using public_key1.pem file for the public key. The .dat file created has also been pushed in this folder

## Output printed


Transaction ID: <in hex format>

Number of inputs: <an integer>

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
Number of outputs: <an integer>
  
    Output 1:
    
        Number of coins: <an integer>
        
        Length of public key: <an integer>
        
        Public key: <in PEM format>
        
    Output 2:
    
        Number of coins: <an integer>
        
        Length of public key: <an integer>
        
        Public key: <in PEM format>
        
    ...
  
 
