# Block Header Creator

The program `block_header.py` creates a block header for a block in a blockchain

## Input
1. index of a block (integer)
2. Hash of parent block (hex string)
3. Target (hex string)
4. Path to a binary file (.dat) consisting of Block body data

## Output
1. Total time taken by program to calculate a nonce value
2. The nonce value found 
3. SHA256 hash of the block header (for the nonce and timestamp found)

## Test
I ran the program for the following inputs: 

```
Index: 5 
Hash of parent block: 2b21ef8ab698e7daf03ccf0110acb4d844fabb5b9513221285f96593d4d4a573 
Target: 0000000f00000000000000000000000000000000000000000000000000000000 
Block body: 015.dat (this file has been pushed in the repo as well)
```

### First Execution- Output:
```
Time taken by program to find a nonce value = 314
nonce found = 65424914
hash of block header = 00000005daa3fcb330c51112ed1d235ab9b05a209d864e216de6caa74b159b97
```
