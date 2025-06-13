from Crypto.Hash import SHA3_256

def sha3(message):
    # Create a SHA3-256 hash object
    sha3_256 = SHA3_256.new()
    
    # Update the hash object with the message
    sha3_256.update(message)
    
    # Return the hexadecimal digest of the hash
    return sha3_256.digest()

def main():
    text = input("nhập chuỗi văn bản:").encode('utf-8')
    hashed_text = sha3(text)
    print("Chuỗi văn bản đã nhập:", text.decode('utf-8'))
    print("SHA3-256 hash:", hashed_text.hex())

if __name__ == "__main__":
    main()