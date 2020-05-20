
#input class
class input_class:
    def __init__(self, transID, index, sign):
        self.transID = transID
        self.index = index
        self.len_of_sign = len(sign)
        self.sign = sign

#output class
class output_class:
    def __init__(self, no_of_coins, public_key):
        self.no_of_coins = no_of_coins
        self.len_of_pubkey = len(public_key)
        self.public_key = public_key
        
#transaction class
class transaction_class:
    def __init__(self, no_of_inputs, array_of_inputs, no_of_outputs, array_of_outputs):
        self.no_of_inputs = no_of_inputs
        self.array_of_inputs = array_of_inputs
        self.no_of_outputs = no_of_outputs
        self.array_of_outputs = array_of_outputs

#returning SHA256 hash of binary data in hex form
import hashlib
def findingHash(finalbytes):
    result = hashlib.sha256(finalbytes)
    return result.hexdigest()

#converting bytearray into transaction object
import sys
def transactionFromByteArray(binary_file):
    
    
    #no of inputs
    binary_file.seek(0)  # Go to beginning of the file
    no_of_inputs = int.from_bytes(binary_file.read(4), "big")
    
    #input data
    array_of_inputs = []
    for i in range(0,no_of_inputs):
        transID = hex(int.from_bytes(binary_file.read(32),'big'))
        index = int.from_bytes(binary_file.read(4), "big")
        len_of_sign = int.from_bytes(binary_file.read(4), "big")
        sign = hex(int.from_bytes(binary_file.read(len_of_sign),'big'))
        array_of_inputs.append(input_class(transID,index,sign))
    
    #no. of outputs
    no_of_outputs = int.from_bytes(binary_file.read(4), "big")

    #output data
    array_of_outputs = []
    for i in range(0,no_of_outputs):
        no_of_coins = int.from_bytes(binary_file.read(8), "big")
        len_of_pubkey = int.from_bytes(binary_file.read(4), "big")
        public_key = (binary_file.read(len_of_pubkey)).decode('utf-8')
        array_of_outputs.append(output_class(no_of_coins,public_key))
    
    transaction_obj = transaction_class(no_of_inputs,array_of_inputs, no_of_outputs, array_of_outputs)
    return transaction_obj    


#prints input
def print_input(transaction_obj):
    no_of_inputs = transaction_obj.no_of_inputs
    array_of_inputs = transaction_obj.array_of_inputs
    print("Number of inputs: %d"%no_of_inputs)
    for i in range(0,no_of_inputs):
        print("\tInput %d:"%(i+1))
        print("\t\tTransaction ID: %s"%(array_of_inputs[i]).transID[2:])
        print("\t\tindex: %d"%(array_of_inputs[i]).index)
        print("\t\tsignature: %s"%(array_of_inputs[i]).sign[2:])

#print output
def print_output(transaction_obj):
    no_of_outputs = transaction_obj.no_of_outputs
    array_of_outputs = transaction_obj.array_of_outputs
    print("Number of outputs: %d"%no_of_outputs)
    for i in range(0,no_of_outputs):
        print("\tOutput %d"%(i+1))
        print("\t\tNumber of coins: %d"%(array_of_outputs[i]).no_of_coins)
        print("\t\tLength of public key: %d"%(array_of_outputs[i]).len_of_pubkey)
        print("\t\tPublic Key: %s"%(array_of_outputs[i]).public_key)
        

#main function
def main():
    print("WELCOME TO ABHIMANYU'S CRYPTOCURRENCY MODEL!")
    print("This programme makes sense of your binary transaction file")
    
    #taking input as path to .dat file
    file_path = input("Please enter the path to your binary file (.dat): ")
    
    #finding transaction ID
    #transID = file_path[-260:-3]
    binary_file = open(file_path, 'rb')
    transID = findingHash(binary_file.read())
    print("Transaction ID: %s"% transID)
    
    #retrieveing data from binary file
    
    transaction_obj = transactionFromByteArray(binary_file)
    binary_file.close()

    #printing inputs
    print_input(transaction_obj)

    #printing outputs
    print_output(transaction_obj)


# Standard boilerplate 
if __name__ == '__main__':
    main()