import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QComboBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Algorithm Comparison")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Main layout
        main_layout = QVBoxLayout()
        dropdown_layout = QHBoxLayout()
        button_layout = QHBoxLayout()

        # Line edit
        self.lineedit = QLineEdit()
        self.lineedit.setPlaceholderText("Enter your input here...")
        self.lineedit.setStyleSheet("""
            QLineEdit {
                font-size: 16px;
                padding: 8px;
                border: 2px solid #4CAF50;
                border-radius: 8px;
                background-color: #f0f0f0;
            }
        """)

        # Dropdowns
        self.combo1 = QComboBox()
        self.combo1.addItem("Select an algorithm...")
        self.combo1.addItems(["Binary search", "Quick sort", "Linear search"])
        self.combo1.setStyleSheet("""
            QComboBox {
                font-size: 16px;
                padding: 6px;
                border: 2px solid #4CAF50;
                border-radius: 8px;
                background-color: #f0f0f0;
            }
        """)

        self.combo2 = QComboBox()
        self.combo2.addItem("Select an algorithm...")
        self.combo2.addItems(["Bubble sort", "Insertion sort", "Exp sort"])
        self.combo2.setStyleSheet("""
            QComboBox {
                font-size: 16px;
                padding: 6px;
                border: 2px solid #4CAF50;
                border-radius: 8px;
                background-color: #f0f0f0;
            }
        """)

        # Label
        self.label = QLabel("Make a selection...")
        self.label.setFont(QFont("Arial", 18))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("""
            QLabel {
                color: #238636;
                font-size: 18px;
                font-weight: bold;
            }
        """)

        # Button
        self.button = QPushButton("Start")
        self.button.setFixedSize(150, 50)
        self.button.setStyleSheet("""
            QPushButton {
                font-size: 16px;
                font-weight: bold;
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)

        # Styling the central widget
        self.central_widget.setStyleSheet("""
            QWidget {
                background-color: #1e1e2f;
            }
        """)

        # Adding widgets to layouts
        dropdown_layout.addWidget(self.combo1)
        dropdown_layout.addWidget(self.combo2)

        button_layout.addStretch()
        button_layout.addWidget(self.button)
        button_layout.addStretch()

        main_layout.addWidget(self.lineedit)
        main_layout.addLayout(dropdown_layout)
        main_layout.addWidget(self.label)
        main_layout.addLayout(button_layout)

        self.central_widget.setLayout(main_layout)

        # Connect signals
        self.combo1.currentTextChanged.connect(self.update_label)
        self.combo2.currentTextChanged.connect(self.update_label)

    def update_label(self):
        first_dropdown = self.combo1.currentText()
        second_dropdown = self.combo2.currentText()
        self.label.setText(f"Selected: {first_dropdown} & {second_dropdown}")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()