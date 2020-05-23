
import hashlib
import time


class block_header:
    def __init__(self, index, parent_block_hash, block_body_hash, target_value, timestamp, nonce):
        self.index = index
        self.parent_block_hash = parent_block_hash
        self.block_body_hash = block_body_hash
        self.target_value = target_value
        self.timestamp = timestamp
        self.nonce = nonce
    
    def calc_hash(self):
        finalbytes = bytearray()
        
        #creating bytearray 
        finalbytes.extend((self.index).to_bytes(4,'big'))
        finalbytes.extend(bytearray.fromhex(self.parent_block_hash))
        finalbytes.extend(bytearray.fromhex(self.block_body_hash))
        finalbytes.extend(bytearray.fromhex(self.target_value))
        finalbytes.extend((self.timestamp).to_bytes(8,'big'))
        finalbytes.extend((self.nonce).to_bytes(8,'big'))
        
        #taking SHA256 hash of the bytearray
        result = hashlib.sha256(finalbytes)
        return result.hexdigest()

#finding hash of block body from binary file
def binary_to_hash(binary_file_path):
    binary_file = open(binary_file_path,"rb")
    binary_file_bytes = binary_file.read()
    binary_file.close()
    hash_bytes = hashlib.sha256(binary_file_bytes)
    return hash_bytes.hexdigest()


def main():
    print("Welcome to Abhimanyu's block header creator!")

    #taking input
    index = int(input("Please enter the index of the block (integer): "))
    parent_block_hash = input("Please enter the hash of parent block: ")
    target_value = input("Please enter the target value (hex string): ")
    binary_file_path = input("Please enter the path to binary file containing block body data (.dat): ")

    #Calculating block body hash
    block_body_hash = binary_to_hash(binary_file_path)

    
    nonce = -1
    while True:
        nonce +=1
        timestamp = int(time.time())
        block_header_obj = block_header(index, parent_block_hash,block_body_hash,target_value,timestamp,nonce)
        block_header_hash = block_header_obj.calc_hash()
        if nonce == 0:
            initial_timestamp = timestamp
        if int(block_header_hash,16)<int(target_value,16) :
            break
    print("Time taken by program to find nonce value = %d"%(timestamp-initial_timestamp))
    print("nonce found = %d"%nonce)
    print("hash of block header = %s"%block_header_hash)

# Standard boilerplate 
if __name__ == '__main__':
    main()