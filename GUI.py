import sys,os
import random
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QComboBox, QTextEdit, QSpinBox
from PyQt5.QtGui import QFont, QPalette, QColor
from PyQt5.QtCore import Qt
from Algorithms import Algorithms

SD = os.path.join(os.path.dirname(__file__))
def clear():os.system('cls') if os.name == 'nt' else os.system('clear')
new_SD = os.path.join(os.path.dirname(SD), 'dump')


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Algorithm Comparison")
        self.setGeometry(100, 100, 1000, 800)

        # Set dark theme for the entire application
        self.set_dark_theme()

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignCenter)  # Center all content vertically
        
        # Input section
        input_layout = QHBoxLayout()
        input_layout.setAlignment(Qt.AlignCenter)  # Center input elements horizontally
        
        # Label for number of items
        self.items_label = QLabel("Number of items:")
        self.items_label.setStyleSheet("""
            QLabel {
                color: #c9d1d9;
                font-size: 14px;
            }
        """)
        
        # Spin box for number of items
        self.items_spinbox = QSpinBox()
        self.items_spinbox.setRange(1, 1000000000)  # Up to 1 billion items
        self.items_spinbox.setValue(100)
        self.items_spinbox.setStyleSheet("""
            QSpinBox {
                font-size: 14px;
                padding: 5px;
                border: 2px solid #238636;
                border-radius: 8px;
                background-color: #0d1117;
                color: #c9d1d9;
                width: 100px;
            }
            
            QSpinBox::up-button, QSpinBox::down-button {
                width: 0px;
                height: 0px;
                border: none;
            }

            QSpinBox::up-arrow, QSpinBox::down-arrow {
                width: 0px;
                height: 0px;
                image: none;
            }
            
            QSpinBox:hover {
                border: 2px solid #2ea043;
                background-color: #161b22;
            }
        """)
        
        # Disable the up/down buttons programmatically
        self.items_spinbox.setButtonSymbols(QSpinBox.NoButtons)
        
        # List operation buttons
        list_buttons_layout = QHBoxLayout()
        list_buttons_layout.setAlignment(Qt.AlignCenter)  # Center buttons horizontally
        
        self.sorted_btn = QPushButton("Sorted List")
        self.sorted_btn.setFixedSize(150, 40)
        self.sorted_btn.setStyleSheet("""
            QPushButton {
                font-size: 14px;
                font-weight: bold;
                background-color: #1f6feb;
                color: white;
                border: none;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #388bfd;
                border: 1px solid #58a6ff;
            }
        """)
        self.sorted_btn.clicked.connect(self.create_sorted_list)
        
        self.random_btn = QPushButton("Random List")
        self.random_btn.setFixedSize(150, 40)
        self.random_btn.setStyleSheet("""
            QPushButton {
                font-size: 14px;
                font-weight: bold;
                background-color: #d29922;
                color: white;
                border: none;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #e3b341;
                border: 1px solid #f9c513;
            }
        """)
        self.random_btn.clicked.connect(self.create_random_list)
        
        # Clear screen button
        self.clear_btn = QPushButton("Clear Screen")
        self.clear_btn.setFixedSize(150, 40)
        self.clear_btn.setStyleSheet("""
            QPushButton {
                font-size: 14px;
                font-weight: bold;
                background-color: #da3633;
                color: white;
                border: none;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #f85149;
                border: 1px solid #ff7b72;
            }
        """)

        self.clear_btn.clicked.connect(self.clear_screen)
        
        list_buttons_layout.addWidget(self.sorted_btn)
        list_buttons_layout.addWidget(self.random_btn)
        list_buttons_layout.addWidget(self.clear_btn)
        
        # Dropdowns section
        dropdown_layout = QHBoxLayout()
        dropdown_layout.setAlignment(Qt.AlignCenter)  # Center dropdowns horizontally
        
        # Dropdowns
        self.combo1 = QComboBox()
        self.combo1.addItem("Select an algorithm...")
        self.combo1.addItems([method for method in dir(Algorithms) if callable(getattr(Algorithms, method)) and not method.startswith("_")])
        self.combo1.setStyleSheet("""
            QComboBox {
                font-size: 16px;
                padding: 6px;
                border: 2px solid #238636;
                border-radius: 8px;
                background-color: #0d1117;
                color: #c9d1d9;
                min-width: 250px;
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
        
        self.combo2 = QComboBox()
        self.combo2.addItem("Select an algorithm...")
        self.combo2.addItems([method for method in dir(Algorithms) if callable(getattr(Algorithms, method)) and not method.startswith("_")])
        self.combo2.setStyleSheet("""
            QComboBox {
                font-size: 16px;
                padding: 6px;
                border: 2px solid #238636;
                border-radius: 8px;
                background-color: #0d1117;
                color: #c9d1d9;
                min-width: 250px;
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
        
        # Start button
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
        
        # Output text area
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        self.output_text.setStyleSheet("""
            QTextEdit {
                font-size: 14px;
                padding: 10px;
                border: 2px solid #30363d;
                border-radius: 8px;
                background-color: #0d1117;
                color: #c9d1d9;
            }
            QTextEdit:hover {
                border: 2px solid #58a6ff;
                background-color: #161b22;
            }
        """)
        self.output_text.setPlaceholderText("Results will appear here...")
        
        # Adding widgets to layouts
        input_layout.addWidget(self.items_label)
        input_layout.addWidget(self.items_spinbox)
        
        dropdown_layout.addWidget(self.combo1)
        dropdown_layout.addWidget(self.combo2)
        
        button_layout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignCenter)  # Center button horizontally
        button_layout.addWidget(self.button)
        
        # Adding all layouts to the main layout
        main_layout.addLayout(input_layout)
        main_layout.addLayout(list_buttons_layout)
        main_layout.addWidget(self.label)
        main_layout.addLayout(dropdown_layout)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.output_text)
        
        self.central_widget.setLayout(main_layout)
        
        # Connect signals
        self.combo1.currentTextChanged.connect(self.update_label)
        self.combo2.currentTextChanged.connect(self.update_label)
        
        # Styling the central widget
        self.central_widget.setStyleSheet("""
            QWidget {
                background-color: #0d1117;
            }
        """)
        
        # Initialize list
        self.current_list = []
    
    def set_dark_theme(self):
        """Set dark theme for the entire application"""
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
        """Create a sorted list from the current input"""
        try:
            num = int(self.items_spinbox.text())
            if num:
                self.current_list = [i for i in range(num)]
                
                # Only show a summary of the list in the output
                num_items = len(self.current_list)
                if num_items <= 20:
                    self.output_text.append("Created sorted list: " + ", ".join(map(str, self.current_list)))
                else:
                    # For larger lists, only show the first 5 and last 5 items
                    first_five = self.current_list[:5]
                    last_five = self.current_list[-5:]
                    self.output_text.append(f"Created sorted list with {num_items} items")
                    self.output_text.append(f"First 5 items: {', '.join(map(str, first_five))}...")
                    self.output_text.append(f"Last 5 items: ...{', '.join(map(str, last_five))}")
            else:
                self.output_text.append("Please enter numbers first")
            
        except ValueError:
            self.output_text.append("Invalid input. Please enter numbers separated by commas.")
    

    def create_random_list(self):
        """Create a random arrangement of the current list"""
        try:
            num = int(self.items_spinbox.text())
            if num:
                self.current_list = [random.randint(1, (num)+1) for _ in range(num)]

                num_items = len(self.current_list)

                if num_items <= 20:
                    self.output_text.append("Created random arrangement: " + ", ".join(map(str, self.current_list)))
                else:
                    first_five = self.current_list[:5]
                    last_five = self.current_list[-5:]
                    self.output_text.append(f"Created random arrangement with {num_items} items")
                    self.output_text.append(f"First 5 items: {', '.join(map(str, first_five))}...")
                    self.output_text.append(f"Last 5 items: ...{', '.join(map(str, last_five))}")
            else:
                self.output_text.append("Please enter numbers first")

        except ValueError:
            self.output_text.append("Invalid input. Please enter numbers separated by commas.")
    def clear_screen(self):
        """Clear the output text area"""
        self.output_text.clear()
        self.output_text.setPlaceholderText("Results will appear here...")
    
    def start_comparison(self):
        """Start the algorithm comparison"""
        algo1 = self.combo1.currentText()
        algo2 = self.combo2.currentText()
        al1=algo1
        al2=algo2
            
        if algo1 == "Select an algorithm..." or algo2 == "Select an algorithm...":
            self.output_text.append("Please select both algorithms to compare")
            return
        if "Search"  in algo1 and "Search"  in algo2 :
            print(True)
        elif "Sort" in algo1 and "Sort" in algo2:
            print(False)
        else:        
            return self.output_text.append("please select a same type algorithm to compare")
            
        try:
            input_text = int(self.items_spinbox.text())
            split=str(input_text)
            if not input_text:
                self.output_text.append("Please enter a list of numbers first")
                return
            
            numbers = [int(x.strip()) for x in split.split(",")]
            num_items = len(numbers)
            
            # Simulate algorithm execution (in a real app, you would implement the actual algorithms)
            clas=Algorithms(self.current_list,5)
            meths=getattr(clas,al1)
            meths2=getattr(clas,al2)
            l=meths
            # self.output_text.append(f"{clas.BinarySearch()}")
            
            self.output_text.append(f"\n--- Comparison Results ---")
            
            # Only show a summary of the list in the output
            if num_items <= 20:
                self.output_text.append(f"Input list: {numbers}")
            else:
                # For larger lists, only show the first 5 and last 5 items
                first_five = numbers[:5]
                last_five = numbers[-5:]
                self.output_text.append(f"Input list with {num_items} items")
                self.output_text.append(f"First 5 items: {', '.join(map(str, first_five))}...")
                self.output_text.append(f"Last 5 items: ...{', '.join(map(str, last_five))}")
            
            if "Search" in algo1 and "Search" in algo2:
                self.output_text.append(f"Algorithm 1 ({algo1}): finded the target: { meths()}, at the index: {self.current_list.index(meths()+1)} , at steps: {clas._Algorithms__steps} , Simulated execution time: {random.randint(10, 100)}ms")
                self.output_text.append(f"Algorithm 2 ({algo2}): finded the target:{meths2()} ,at the index: {self.current_list.index(meths2()+1) }, at steps: {clas._Algorithms__steps} , Simulated execution time: {random.randint(10, 100)}ms")
            elif "Sort" in algo1 and "Sort" in algo2:
                self.output_text.append(f"Algorithm 1 ({algo1}): the sorted list F5 and L5: {meths()},Number of itreations is: {clas._Algorithms__iteration} ,Simulated execution time: {random.randint(10, 100)}ms")
                self.output_text.append(f"Algorithm 2 ({algo2}): the sorted list F5 and L5: {meths2()},Number of itreations is: {clas._Algorithms__iteration} ,Simulated execution time: {random.randint(10, 100)}ms")
                        
            self.output_text.append("--- End of Comparison ---\n")
            
        except ValueError:
            self.output_text.append("Invalid input. Please enter numbers separated by commas.")
            

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
