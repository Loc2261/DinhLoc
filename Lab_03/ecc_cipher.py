import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

# --- FIX 1: Import the correct class name from the correct file ---
from ui.ecc import Ui_RSACipherWindow

API_BASE_URL = "http://127.0.0.1:5000/api/ecc"

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        # --- FIX 2: Use the correct UI class from the import ---
        self.ui = Ui_RSACipherWindow()
        self.ui.setupUi(self)

        # --- FIX 3: Use the correct widget names from the UI file ---
        self.ui.btnGenerateKeys.clicked.connect(self.call_api_gen_keys)
        self.ui.btnSign.clicked.connect(self.call_api_sign)
        self.ui.btnVerify.clicked.connect(self.call_api_verify)

    def show_message(self, text, icon=QMessageBox.Information):
        """Helper function to display a message box."""
        msg = QMessageBox()
        msg.setIcon(icon)
        msg.setText(text)
        msg.setWindowTitle("API Response")
        msg.exec_()
        
    def handle_api_error(self, response=None, exception=None):
        """Helper function to handle API errors."""
        if exception:
            error_message = f"Connection Error: {exception}"
            print(error_message)
            self.show_message(error_message, QMessageBox.Critical)
        elif response:
            error_message = f"API Error: Status {response.status_code}\n{response.text}"
            print(error_message)
            self.show_message(error_message, QMessageBox.Warning)

    def call_api_gen_keys(self):
        url = f"{API_BASE_URL}/generate_keys"
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                data = response.json()
                self.show_message(data["message"])
            else:
                self.handle_api_error(response=response)
        except requests.exceptions.RequestException as e:
            self.handle_api_error(exception=e)

    def call_api_sign(self):
        # --- FIX 4: Use the correct widget name to get text ---
        message = self.ui.txt_sign.toPlainText()
        if not message:
            self.show_message("Information to sign cannot be empty.", QMessageBox.Warning)
            return

        url = f"{API_BASE_URL}/sign"
        payload = {"message": message}

        try:
            response = requests.post(url, json=payload, timeout=5)
            if response.status_code == 200:
                data = response.json()
                # --- FIX 4: Use the correct widget name to set text ---
                self.ui.txt_sign.setText(data["signature"])
                self.show_message("Signed Successfully")
            else:
                self.handle_api_error(response=response)
        except requests.exceptions.RequestException as e:
            self.handle_api_error(exception=e)

    def call_api_verify(self):
        # --- FIX 4: Use the correct widget names to get text ---
        message = self.ui.txt_sign.toPlainText()
        signature = self.ui.txt_sign.toPlainText()

        if not message or not signature:
            self.show_message("Information and Signature cannot be empty.", QMessageBox.Warning)
            return

        url = f"{API_BASE_URL}/verify"
        payload = {"message": message, "signature": signature}

        try:
            response = requests.post(url, json=payload, timeout=5)
            if response.status_code == 200:
                data = response.json()
                if data["is_verified"]:
                    self.show_message("Signature Verified Successfully!")
                else:
                    self.show_message("Verification Failed: Signature is not valid.", QMessageBox.Warning)
            else:
                self.handle_api_error(response=response)
        except requests.exceptions.RequestException as e:
            self.handle_api_error(exception=e)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())