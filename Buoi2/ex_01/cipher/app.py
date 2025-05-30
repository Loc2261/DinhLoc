import os
import sys
from flask import Flask, render_template, request, jsonify

# Thêm thư mục cha vào sys.path để có thể import các module mã hóa
# Điều này là cần thiết nếu bạn đặt các thư mục cipher/vigenere/v.v. cùng cấp với app.py
# và muốn import theo kiểu 'from caesar.caesar_cipher import CaesarCipher'
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir) # Lấy thư mục cha của thư mục hiện tại
sys.path.append(current_dir) # Đảm bảo thư mục hiện tại có thể tìm thấy các sub-folder

# Import các lớp mã hóa từ các module riêng lẻ
from caesar.caesar_cipher import CaesarCipher
from railfence.railfence_cipher import RailFenceCipher
from vigenere.vigenere_cipher import VigenereCipher
from playfair.playfair_cipher import PlayfairCipher
from transposition.transposition_cipher import TranspositionCipher

app = Flask(__name__)

# Khởi tạo các đối tượng Cipher
caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher()
playfair_cipher = PlayfairCipher()
transposition_cipher = TranspositionCipher()
railfence_cipher = RailFenceCipher()

# --- Định tuyến cho trang chủ ---
@app.route('/')
def index():
    return render_template('index.html')

# --- Định tuyến cho Caesar Cipher ---
@app.route('/caesar')
def caesar_page():
    return render_template('caesar.html')

# API cho Caesar Cipher (dùng request.get_json và jsonify giống Playfair/Transposition)
@app.route('/api/caesar/encrypt', methods=['POST'])
def caesar_encrypt_api():
    data = request.get_json()
    plain_text = data.get('plain_text', '')
    key = data.get('key', 0)
    try:
        encrypted_text = caesar_cipher.encrypt(plain_text, int(key))
        return jsonify({'encrypted_text': encrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/caesar/decrypt', methods=['POST'])
def caesar_decrypt_api():
    data = request.get_json()
    cipher_text = data.get('cipher_text', '')
    key = data.get('key', 0)
    try:
        decrypted_text = caesar_cipher.decrypt(cipher_text, int(key))
        return jsonify({'decrypted_text': decrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# --- Định tuyến cho Vigenere Cipher ---
@app.route('/vigenere')
def vigenere_page():
    return render_template('vigenere.html')

# API cho Vigenere Cipher
@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt_api():
    data = request.get_json()
    plain_text = data.get('plain_text', '')
    key = data.get('key', '')
    try:
        encrypted_text = vigenere_cipher.encrypt(plain_text, key)
        return jsonify({'encrypted_text': encrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt_api():
    data = request.get_json()
    cipher_text = data.get('cipher_text', '')
    key = data.get('key', '')
    try:
        decrypted_text = vigenere_cipher.decrypt(cipher_text, key)
        return jsonify({'decrypted_text': decrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# --- Định tuyến cho Playfair Cipher ---
@app.route('/playfair')
def playfair_page():
    return render_template('playfair.html')

# API cho Playfair Cipher
@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt_api():
    data = request.get_json()
    plain_text = data.get('plain_text', '')
    key = data.get('key', '')
    try:
        playfair_matrix = playfair_cipher.create_playfair_matrix(key)
        encrypted_text = playfair_cipher.playfair_encrypt(plain_text, playfair_matrix)
        return jsonify({'encrypted_text': encrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt_api():
    data = request.get_json()
    cipher_text = data.get('cipher_text', '')
    key = data.get('key', '')
    try:
        playfair_matrix = playfair_cipher.create_playfair_matrix(key)
        decrypted_text = playfair_cipher.playfair_decrypt(cipher_text, playfair_matrix)
        return jsonify({'decrypted_text': decrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# --- Định tuyến cho Transposition Cipher ---
@app.route('/transposition')
def transposition_page():
    return render_template('transposition.html')

# API cho Transposition Cipher
@app.route('/api/transposition/encrypt', methods=['POST'])
def transposition_encrypt_api():
    data = request.get_json()
    plain_text = data.get('plain_text', '')
    key = data.get('key', 0)
    try:
        encrypted_text = transposition_cipher.encrypt(plain_text, int(key))
        return jsonify({'encrypted_text': encrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/transposition/decrypt', methods=['POST'])
def transposition_decrypt_api():
    data = request.get_json()
    cipher_text = data.get('cipher_text', '')
    key = data.get('key', 0)
    try:
        decrypted_text = transposition_cipher.decrypt(cipher_text, int(key))
        return jsonify({'decrypted_text': decrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# --- Định tuyến cho Rail Fence Cipher ---
@app.route('/railfence')
def railfence_page():
    return render_template('railfence.html')

# API cho Rail Fence Cipher
@app.route('/api/railfence/encrypt', methods=['POST'])
def railfence_encrypt_api():
    data = request.get_json()
    plain_text = data.get('plain_text', '')
    key = data.get('key', 0)
    try:
        encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, int(key))
        return jsonify({'encrypted_text': encrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/railfence/decrypt', methods=['POST'])
def railfence_decrypt_api():
    data = request.get_json()
    cipher_text = data.get('cipher_text', '')
    key = data.get('key', 0)
    try:
        decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, int(key))
        return jsonify({'decrypted_text': decrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


# --- Hàm chính để chạy ứng dụng ---
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5020, debug=True)