import string
alphabet = " " + string.ascii_lowercase

positions={}
for i in alphabet:
    positions[i]=alphabet.index(i)

message = "hi my name is caesar"

def encode(msg,key):
    encoded_message=""    
    for char in msg:
        result = (positions[char]+key ) % 27
        encoded_message += alphabet[result]
    return encoded_message
        
decoded_message=encode(message,3)

def decode(msg,key):
    original_message=""
    for char in msg:
        result = (positions[char]-key )  % 27
        original_message += alphabet[result]
    return original_message

decode(decoded_message,3)
