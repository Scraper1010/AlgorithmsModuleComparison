import sys, os
import random
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QComboBox, QTextEdit, QSpinBox
from PyQt5.QtGui import QFont, QPalette, QColor, QIcon, QTextCharFormat, QSyntaxHighlighter
from PyQt5.QtCore import Qt
from Algorithms import Algorithms
import threading

SD = os.path.join(os.path.dirname(__file__))
def clear():os.system('cls') if os.name == 'nt' else os.system('clear')
new_SD = os.path.join(os.path.dirname(SD), 'dump')

class SyntaxHighlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Create format objects
        time_format = QTextCharFormat()
        time_format.setForeground(QColor("#58a6ff"))  # Blue
        
        algo_format = QTextCharFormat()
        algo_format.setForeground(QColor("#7ee787"))  # Green
        
        error_format = QTextCharFormat()
        error_format.setForeground(QColor("#f85149"))  # Red
        
        success_format = QTextCharFormat()
        success_format.setForeground(QColor("#3fb950"))  # Light green
        
        algo_name_format = QTextCharFormat()
        algo_name_format.setForeground(QColor("#ffa500"))  # Orange
        algo_name_format.setFontPointSize(14)  # Larger font for algorithm names
        
        # Define highlighting rules
        self.highlighting_rules = [
            (time_format, "Time taken: [0-9.]+ ms"),
            (algo_format, "Results:"),
            (error_format, "Error:.*"),
            (success_format, "Found value.*"),
            (algo_name_format, "LinearSearch|BinarySearch|InterpolationSearch|JumpSearch|BubbleSort|InsertionSort|QuickSort|SelectionSort")
        ]

    def highlightBlock(self, text):
        for format, pattern in self.highlighting_rules:
            expression = QtCore.QRegExp(pattern)
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Algorithm Comparison")
        self.setGeometry(100, 100, 1000, 800)
        icon_path = os.path.join(os.path.dirname(__file__), "icon.png")
        self.setWindowIcon(QIcon(icon_path))
        self.set_dark_theme()
        self.setup_ui()
        self.current_list = []

    def setup_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignCenter)

        # Input section
        input_layout = self.create_input_section()
        list_buttons_layout = self.create_list_buttons()
        dropdown_layout = self.create_dropdowns()
        button_layout = self.create_start_button()
        
        # Output text area
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        self.output_text.setStyleSheet("""
            QTextEdit {
                font-size: 16px;
                padding: 10px;
                border: 2px solid #30363d;
                border-radius: 8px;
                background-color: #0d1117;
                color: #c9d1d9;
                font-family: 'Consolas', 'Courier New', monospace;
            }
            QTextEdit:hover {
                border: 2px solid #58a6ff;
                background-color: #161b22;
            }
        """)
        self.output_text.setPlaceholderText("Results will appear here...")
        self.highlighter = SyntaxHighlighter(self.output_text.document())

        # Add all layouts to main layout
        main_layout.addLayout(input_layout)
        main_layout.addLayout(list_buttons_layout)
        main_layout.addLayout(dropdown_layout)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.output_text)
        
        self.central_widget.setLayout(main_layout)

    def create_input_section(self):
        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        # Number of items input
        self.items_label = QLabel("Number of items:")
        self.items_spinbox = QSpinBox()
        self.items_spinbox.setRange(1, 1000000000)
        self.items_spinbox.setValue(100)
        self.setup_spinbox_style(self.items_spinbox)

        # Target value input
        self.target_label = QLabel("Target value:")
        self.target_spinbox = QSpinBox()
        self.target_spinbox.setRange(0, 1000000000)
        self.target_spinbox.setValue(50)
        self.setup_spinbox_style(self.target_spinbox)

        layout.addWidget(self.items_label)
        layout.addWidget(self.items_spinbox)
        layout.addWidget(self.target_label)
        layout.addWidget(self.target_spinbox)
        return layout

    def create_list_buttons(self):
        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        buttons = [
            ("Sorted List", "#1f6feb", self.create_sorted_list),
            ("Random List", "#d29922", self.create_random_list),
            ("Clear Screen", "#da3633", self.clear_screen)
        ]

        for text, color, callback in buttons:
            btn = QPushButton(text)
            btn.setFixedSize(150, 40)
            btn.setStyleSheet(f"""
                QPushButton {{
                    font-size: 14px;
                    font-weight: bold;
                    background-color: {color};
                    color: white;
                    border: none;
                    border-radius: 8px;
                }}
                QPushButton:hover {{
                    background-color: {self.adjust_color(color, 20)};
                    border: 1px solid {self.adjust_color(color, 40)};
                }}
            """)
            btn.clicked.connect(callback)
            layout.addWidget(btn)

        return layout

    def create_dropdowns(self):
        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        # Get all algorithms
        all_algorithms = [method for method in dir(Algorithms) 
                         if callable(getattr(Algorithms, method)) 
                         and not method.startswith("_")]
        
        # Create and setup combo boxes
        self.combo1 = self.create_combo_box(all_algorithms)
        self.combo2 = self.create_combo_box(all_algorithms)

        # Label for dropdowns
        self.label = QLabel("Select algorithms to compare")
        self.label.setFont(QFont("Arial", 18))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("""
            QLabel {
                color: #58a6ff;
                font-size: 18px;
                font-weight: bold;
            }
        """)

        layout.addWidget(self.combo1)
        layout.addWidget(self.combo2)
        return layout

    def create_start_button(self):
        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        
        self.button = QPushButton("Start Comparison")
        self.button.setFixedSize(200, 50)
        self.button.setStyleSheet("""
            QPushButton {
                font-size: 16px;
                font-weight: bold;
                background-color: #238636;
                color: white;
                border: none;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #2ea043;
                border: 1px solid #3fb950;
            }
        """)
        self.button.clicked.connect(self.start_comparison)
        layout.addWidget(self.button)
        return layout

    def setup_spinbox_style(self, spinbox):
        spinbox.setStyleSheet("""
            QSpinBox {
                font-size: 14px;
                padding: 5px;
                border: 2px solid #238636;
                border-radius: 8px;
                background-color: #0d1117;
                color: #c9d1d9;
                width: 100px;
            }
            QSpinBox:hover {
                border: 2px solid #2ea043;
                background-color: #161b22;
            }
        """)
        spinbox.setButtonSymbols(QSpinBox.NoButtons)

    def create_combo_box(self, items):
        combo = QComboBox()
        combo.addItem("Select an algorithm...")
        combo.addItems(sorted(items))
        combo.setMinimumWidth(250)
        combo.setStyleSheet("""
            QComboBox {
                font-size: 16px;
                padding: 6px;
                border: 2px solid #238636;
                border-radius: 8px;
                background-color: #0d1117;
                color: #c9d1d9;
            }
            QComboBox:hover {
                border: 2px solid #2ea043;
                background-color: #161b22;
            }
            QComboBox::drop-down {
                border: none;
            }
            QComboBox::down-arrow {
                image: none;
                border: none;
            }
            QComboBox QAbstractItemView {
                background-color: #0d1117;
                color: #c9d1d9;
                selection-background-color: #238636;
                selection-color: white;
                border: 1px solid #30363d;
            }
        """)
        combo.currentTextChanged.connect(self.update_label)
        return combo

    def adjust_color(self, hex_color, amount):
        # Convert hex to RGB
        r = int(hex_color[1:3], 16)
        g = int(hex_color[3:5], 16)
        b = int(hex_color[5:7], 16)
        
        # Adjust each component
        r = min(255, max(0, r + amount))
        g = min(255, max(0, g + amount))
        b = min(255, max(0, b + amount))
        
        # Convert back to hex
        return f"#{r:02x}{g:02x}{b:02x}"

    def set_dark_theme(self):
        app = QApplication.instance()
        if app:
            palette = QPalette()
            palette.setColor(QPalette.Window, QColor("#0d1117"))
            palette.setColor(QPalette.WindowText, QColor("#c9d1d9"))
            palette.setColor(QPalette.Base, QColor("#0d1117"))
            palette.setColor(QPalette.AlternateBase, QColor("#161b22"))
            palette.setColor(QPalette.ToolTipBase, QColor("#161b22"))
            palette.setColor(QPalette.ToolTipText, QColor("#c9d1d9"))
            palette.setColor(QPalette.Text, QColor("#c9d1d9"))
            palette.setColor(QPalette.Button, QColor("#21262d"))
            palette.setColor(QPalette.ButtonText, QColor("#c9d1d9"))
            palette.setColor(QPalette.BrightText, QColor("#ffffff"))
            palette.setColor(QPalette.Link, QColor("#58a6ff"))
            palette.setColor(QPalette.Highlight, QColor("#238636"))
            palette.setColor(QPalette.HighlightedText, QColor("#ffffff"))
            app.setPalette(palette)

    def update_label(self):
        first_dropdown = self.combo1.currentText()
        second_dropdown = self.combo2.currentText()
        self.label.setText(f"Selected: {first_dropdown} & {second_dropdown}")

    def create_sorted_list(self):
        try:
            num = int(self.items_spinbox.text())
            if num:
                self.current_list = [i for i in range(num)]
                self.display_list_summary("Created sorted list")
        except ValueError:
            self.output_text.append("Error: Invalid input. Please enter a valid number.")

    def create_random_list(self):
        try:
            num = int(self.items_spinbox.text())
            if num:
                self.current_list = [random.randint(1, num+1) for _ in range(num)]
                self.display_list_summary("Created random arrangement")
        except ValueError:
            self.output_text.append("Error: Invalid input. Please enter a valid number.")

    def display_list_summary(self, prefix):
        num_items = len(self.current_list)
        if num_items <= 20:
            self.output_text.append(f"{prefix}: {', '.join(map(str, self.current_list))}")
        else:
            first_five = self.current_list[:5]
            last_five = self.current_list[-5:]
            self.output_text.append(f"{prefix} with {num_items} items")
            self.output_text.append(f"First 5 items: {', '.join(map(str, first_five))}...")
            self.output_text.append(f"Last 5 items: ...{', '.join(map(str, last_five))}")

    def clear_screen(self):
        self.output_text.clear()
        self.output_text.setPlaceholderText("Results will appear here...")

    def start_comparison(self):
        if not self.current_list:
            self.output_text.append("Error: Please create a list first using 'Sorted List' or 'Random List' button")
            return

        algo1 = self.combo1.currentText()
        algo2 = self.combo2.currentText()

        if algo1 == "Select an algorithm..." or algo2 == "Select an algorithm...":
            self.output_text.append("Error: Please select two algorithms to compare")
            return

        if algo1 == algo2:
            self.output_text.append("Error: Cannot compare the same algorithm")
            return

        is_search1 = "search" in algo1.lower()
        is_search2 = "search" in algo2.lower()
        
        if is_search1 != is_search2:
            self.output_text.append("Error: Cannot compare search algorithm with sort algorithm. Please select algorithms of the same type.")
            return

        list1 = self.current_list.copy()
        list2 = self.current_list.copy()
        target_value = self.target_spinbox.value()

        algo_instance1 = Algorithms(lst=list1, target=target_value, debug=True)
        algo_instance2 = Algorithms(lst=list2, target=target_value, debug=True)

        method1 = getattr(algo_instance1, algo1)
        method2 = getattr(algo_instance2, algo2)

        thread1 = threading.Thread(target=self._run_algorithm, args=(method1, algo1))
        thread2 = threading.Thread(target=self._run_algorithm, args=(method2, algo2))

        thread1.start()
        thread2.start()
        thread1.join()
        thread2.join()

    def _run_algorithm(self, algorithm_method, algorithm_name):
        try:
            result = algorithm_method()
            if isinstance(result, tuple):
                if len(result) == 4:  # Sorting algorithm result
                    sorted_list, iterations, name, elapsed_time = result
                    self.output_text.append(f"\n{algorithm_name} Results:")
                    self.output_text.append(f"Time taken: {elapsed_time:.3f} ms")
                    self.output_text.append(f"Number of iterations: {iterations}")
                    if len(sorted_list) <= 20:
                        self.output_text.append(f"Sorted list: {sorted_list}")
                    else:
                        self.output_text.append(f"First 5 elements: {sorted_list[:5]}")
                        self.output_text.append(f"Last 5 elements: {sorted_list[-5:]}")
                elif len(result) == 5:  # Search algorithm result
                    value, index, elapsed_time, name, steps = result
                    self.output_text.append(f"\n{algorithm_name} Results:")
                    self.output_text.append(f"Found value {value} at index {index}")
                    self.output_text.append(f"Time taken: {elapsed_time:.3f} ms")
                    self.output_text.append(f"Number of steps: {steps}")
            else:
                self.output_text.append(f"\n{algorithm_name} Results:")
                self.output_text.append(f"Result: {result}")
        except Exception as e:
            self.output_text.append(f"\n{algorithm_name} Error: {str(e)}")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
