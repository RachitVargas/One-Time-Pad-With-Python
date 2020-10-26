
def encrypt (message, key):
    message = bytes(message, encoding='utf-8')
    key = bytes(key, encoding='utf-8')
 
    ciphertext = int.from_bytes(message, byteorder="big") ^ \
        int.from_bytes(key, byteorder="big")
    return ciphertext.to_bytes(max(len(message), len(key)), byteorder="big")    

    
def decrypt(ciphertext, key):
    key = bytes(key, encoding="utf-8")
    
    message = int.from_bytes(ciphertext, byteorder="big") ^ \
        int.from_bytes(key, byteorder="big")
    return message.to_bytes(max(len(ciphertext), len(key)), byteorder="big")    


def main():
    
    message = input("Enter Message: ")
    key = input("Enter Key: ")
    
    if len(message) == len(key):
       ciphertext = encrypt(message, key)
       print("This is the ciphertext: " + str(ciphertext))
       
       message = decrypt(ciphertext, key)
       print("This is the message: " + message.decode(encoding = 'utf-8'))
    
    else:
        print("Sorry, the message and the key must be the same length")


if __name__ == "__main__":
    main()
