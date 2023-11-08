import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("HTTP Request")
        self.setGeometry(100, 100, 400, 200)

        self.url_input = QTextEdit(self)
        self.url_input.setPlaceholderText("Введите URL")

        self.status_output = QTextEdit(self)
        self.status_output.setPlaceholderText("Статус запроса будет выведен здесь")
        self.status_output.setReadOnly(True)

        self.request_button = QPushButton("Выполнить запрос", self)
        self.request_button.clicked.connect(self.make_request)

        layout = QVBoxLayout()
        layout.addWidget(self.url_input)
        layout.addWidget(self.request_button)
        layout.addWidget(self.status_output)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def make_request(self):
        url = self.url_input.toPlainText()
        if url:
            try:
                response = requests.get(url)
                self.status_output.setText(f"Статус запроса: {response.status_code} - {response.reason}")
            except requests.exceptions.RequestException as e:
                self.status_output.setText(f"Ошибка запроса: {e}")
        else:
            self.status_output.setText("Пожалуйста, введите URL")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
