class PlayfairCipher:
    def __init__(self) -> None:
        pass

    def create_playfair_matrix(self, key):
        key = key.replace("J", "I")  # Chuyển "J" thành "I" trong khóa
        key = key.upper()
        key_set = set(key)
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        remaining_letters = [
            letter for letter in alphabet if letter not in key_set
        ]
        matrix = list(key)

        for letter in remaining_letters:
            matrix.append(letter)
            if len(matrix) == 25:
                break

        playfair_matrix = [matrix[i:i+5] for i in range(0, len(matrix), 5)]
        return playfair_matrix

    def find_letter_coords(self, matrix, letter):
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == letter:
                    return row, col
        return -1, -1 # Điều này không nên xảy ra nếu ma trận được tạo đúng và chữ cái nằm trong bảng chữ cái

    def playfair_encrypt(self, plain_text, matrix):
        # Chuyển "J" thành "I" trong văn bản đầu vào
        plain_text = plain_text.replace("J", "I")
        plain_text = plain_text.upper()
        encrypted_text = ""

        # Logic để xử lý các cặp chữ cái trùng lặp và thêm 'X' nếu độ dài lẻ
        processed_plain_text = ""
        i = 0
        while i < len(plain_text):
            processed_plain_text += plain_text[i]
            if i + 1 < len(plain_text):
                if plain_text[i] == plain_text[i+1]:
                    processed_plain_text += "X"
                else:
                    processed_plain_text += plain_text[i+1]
                    i += 1 # Only increment if we actually processed the next character
            i += 1 # Always increment for the current character

        if len(processed_plain_text) % 2 != 0:
            processed_plain_text += "X"

        for i in range(0, len(processed_plain_text), 2):
            pair = processed_plain_text[i:i+2]
            # Xử lý nếu số lượng ký tự lẻ (đoạn này đã được xử lý ở trên)
            # if len(pair) == 1:
            #     pair += "X"

            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])

            if row1 == row2:
                encrypted_text += matrix[row1][(col1 + 1) % 5]
                encrypted_text += matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                encrypted_text += matrix[(row1 + 1) % 5][col1]
                encrypted_text += matrix[(row2 + 1) % 5][col2]
            else: # Đây là trường hợp row1 != row2 và col1 != col2
                encrypted_text += matrix[row1][col2]
                encrypted_text += matrix[row2][col1]
        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = cipher_text.upper()
        decrypted_text = ""
        decrypted_text1 = "" # Biến này được khai báo trong ảnh nhưng không được sử dụng

        for i in range(0, len(cipher_text), 2):
            pair = cipher_text[i:i+2]
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])

            if row1 == row2:
                decrypted_text += matrix[row1][(col1 - 1) % 5]
                decrypted_text += matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                # Đoạn này được tách làm 2 dòng trong ảnh
                decrypted_text += matrix[(row1 - 1) % 5][col1]
                decrypted_text += matrix[(row2 - 1) % 5][col2]
            else: # Trường hợp còn lại: row1 != row2 và col1 != col2
                decrypted_text += matrix[row1][col2]
                decrypted_text += matrix[row2][col1]

        banro = ""
    
        if len(decrypted_text) >= 2: # Đảm bảo có đủ ký tự để xử lý theo logic của ảnh
            for i in range(0, len(decrypted_text) - 2, 2):
                if decrypted_text[i] == decrypted_text[i+2]:
                    banro += decrypted_text[i]
                else:
                    banro += decrypted_text[i] + decrypted_text[i+1]
            
            # Xử lý 2 ký tự cuối cùng theo logic ảnh
            if decrypted_text[-1] == "X":
                banro += decrypted_text[-2]
            else:
                banro += decrypted_text[-2]
            banro += decrypted_text[-1]
        else: # Trường hợp decrypted_text có 0 hoặc 1 ký tự
            banro = decrypted_text # Nếu không đủ dài để vào vòng lặp hoặc điều kiện trên

        return banro