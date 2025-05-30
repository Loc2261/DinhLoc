from flask import Flask, request, jsonify
from caesar.caesar_cipher import CaesarCipher
from railfence.railfence_cipher import RailFenceCipher
from vigenere.vigenere_cipher import VigenereCipher  
from playfair.playfair_cipher import PlayfairCipher
from transposition.transposition_cipher import TranspositionCipher
app = Flask(__name__)

# CAESAR CIPHER ALGORITHM
caesar_cipher = CaesarCipher()

@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})



# Thêm đoạn sau vào trước hàm main (nếu có hàm main)
# VIGENERE CIPHER ALGORITHM
vigenere_cipher = VigenereCipher()

@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})





# RAILFENCE CIPHER ALGORITHM
railfence_cipher = RailFenceCipher()

@app.route('/api/railfence/encrypt', methods=['POST'])
def encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/railfence/decrypt', methods=['POST'])
def decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

#playfair_cipher
playfair_cipher = PlayfairCipher()

@app.route('/api/playfair/creatematrix', methods=['POST'])
def playfair_creatrix():
    data = request.json
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({"playfair_matrix": playfair_matrix})
@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    
    # Tạo ma trận Playfair từ khóa
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    
    # Mã hóa văn bản
    encrypted_text = playfair_cipher.playfair_encrypt(plain_text, playfair_matrix)
    
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    
    # Tạo ma trận Playfair từ khóa
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    
    # Giải mã văn bản
    decrypted_text = playfair_cipher.playfair_decrypt(cipher_text, playfair_matrix)
    
    return jsonify({'decrypted_text': decrypted_text})

#Tranpher
transposition_cipher = TranspositionCipher()

@app.route('/api/transposition/encrypt', methods=['POST'])
def transposition_encrypt():
    data = request.get_json() # Sử dụng request.get_json() thay vì request.json như trong hình
    plain_text = data.get('plain_text')
    key = int(data.get('key')) # Chuyển đổi key sang kiểu int
    encrypted_text = transposition_cipher.encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/transposition/decrypt', methods=['POST'])
def transposition_decrypt():
    data = request.get_json() # Sử dụng request.get_json() thay vì request.json như trong hình
    cipher_text = data.get('cipher_text')
    key = int(data.get('key')) # Chuyển đổi key sang kiểu int
    decrypted_text = transposition_cipher.decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

# main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)