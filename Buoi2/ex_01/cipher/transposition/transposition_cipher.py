class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, text, key):
        encrypted_text = ''
        for col in range(key):
            pointer = col
            while pointer < len(text):
                encrypted_text += text[pointer]
                pointer += key
        return encrypted_text

    def decrypt(self, text, key):
        decrypted_text = [''] * key
        row, col = 0, 0
        for symbol in text:
            decrypted_text[col] += symbol
            col += 1
            # Điều kiện để chuyển hàng và reset cột
            # if col == key or (col == key - 1 and row >= len(text) % key):
            # Điều kiện được sửa lại để khớp chính xác với ảnh hơn (col == key - 1 AND row >= len(text) % key)
            # Hình ảnh có vẻ như đang kiểm tra nếu cột đã đạt đến key (tức là đã đi hết một hàng logic),
            # HOẶC nếu nó là cột cuối cùng (key - 1) VÀ đã đạt đến số hàng đầy đủ của cột đó
            # (dựa trên len(text) % key để xử lý các cột cuối cùng có ít ký tự hơn).
            # Logic này hơi phức tạp, nhưng tôi sẽ giữ nguyên theo ảnh.
            if col == key or (col == key - 1 and row >= len(text) % key):
                col = 0
                row += 1
        return ''.join(decrypted_text)