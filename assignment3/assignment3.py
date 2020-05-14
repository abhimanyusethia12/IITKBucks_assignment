
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

#converting transaction to Byte Array
import sys
def transactionToByteArray(transaction_obj):
    no_of_inputs = transaction_obj.no_of_inputs
    array_of_inputs = transaction_obj.array_of_inputs
    no_of_outputs = transaction_obj.no_of_outputs
    array_of_outputs = transaction_obj.array_of_outputs
    finalbytes = bytearray()
    
    #no of inputs- 4 bytes
    finalbytes.extend(no_of_inputs.to_bytes(4, sys.byteorder))
    
    #adding input data
    for i in range(0,no_of_inputs):
        input_obj = array_of_inputs[i]
        finalbytes.extend((input_obj.transID).encode())
        finalbytes.extend((input_obj.index).to_bytes(4,sys.byteorder))
        finalbytes.extend((input_obj.len_of_sign).to_bytes(4,sys.byteorder))
        finalbytes.extend((input_obj.sign).encode())
    
    #no of outputs- 4 bytes
    finalbytes.extend(no_of_outputs.to_bytes(4, sys.byteorder))

    #adding output data 
    for i in range(0,no_of_outputs):
        output_obj = array_of_outputs[i]
        finalbytes.extend((output_obj.no_of_coins).to_bytes(8,sys.byteorder))
        finalbytes.extend((output_obj.len_of_pubkey).to_bytes(4,sys.byteorder))
        finalbytes.extend((output_obj.public_key).encode())
    
    return finalbytes

#taking input
def take_input(i):
    transID = input("For input no. %d, please enter transaction ID in hex format: "%(i+1))
    index = int (input("For input no. %d, please enter index (integer): "%(i+1)))
    sign = input("For input no. %d, please enter signature in hex format: "%(i+1))
    input_obj = input_class(transID,index,sign)
    return input_obj

#taking output
def take_output(i):
    no_of_coins = int(input("For output no. %d, please enter number of coins (integer): "%(i+1)))
    path_pem = input("For output no. %d, please enter path to public key file (.pem): "%(i+1))
    with open(path_pem,'r') as f:
        public_key = f.read()

    output_obj = output_class(no_of_coins, public_key)
    return output_obj

#prints input
def print_input(transaction_obj):
    no_of_inputs = transaction_obj.no_of_inputs
    array_of_inputs = transaction_obj.array_of_inputs
    print("Number of inputs: %d"%no_of_inputs)
    for i in range(0,no_of_inputs):
        print("\tInput %d:"%(i+1))
        print("\t\tTransaction ID: %s"%(array_of_inputs[i]).transID)
        print("\t\tindex: %d"%(array_of_inputs[i]).index)
        print("\t\tsignature: %s"%(array_of_inputs[i]).sign)

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
    
    #no of inputs
    no_of_inputs = int (input("Please enter the number of inputs: "))
    
    #taking inputs
    array_of_inputs = []
    for i in range(0,no_of_inputs):
        array_of_inputs.append(take_input(i))
    
    #no of outputs
    no_of_outputs = int (input("Please enter the number of outputs: "))

    #taking outputs
    array_of_outputs = []
    for i in range(0,no_of_outputs):
        array_of_outputs.append(take_output(i))
    
    #making transaction object
    transaction_obj = transaction_class(no_of_inputs,array_of_inputs, no_of_outputs, array_of_outputs)

    #converting to binary 
    finalbytes = transactionToByteArray(transaction_obj)
    
    #getting Transaction ID 
    transID = findingHash(finalbytes)
    print("Transaction ID: %s"% transID)

    
    #writing to binary file
    f = open(transID + '.dat', 'w+b')
    f.write(finalbytes)
    f.close()

    #printing inputs
    print_input(transaction_obj)

    #printing outputs
    print_output(transaction_obj)


# Standard boilerplate 
if __name__ == '__main__':
    main()