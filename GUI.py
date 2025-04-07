import sys
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel,QWidget,QVBoxLayout,QHBoxLayout,QGridLayout,QPushButton,QCheckBox,QLineEdit,QComboBox,QSizePolicy
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap,QPalette,QBrush

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Alogrthim comparsion")
        self.setGeometry(100, 100, 400, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.lineedit=QLineEdit()
        
        main_layout = QVBoxLayout()
        dropdown_layout = QHBoxLayout()  
        
        # self.button=QPushButton("Start",self)
        # self.button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # self.button.setGeometry(630,40,100,40)
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        self.button = QPushButton("Start",self)
        # self.button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # self.button.setMinimumHeight(20)
        self.move(500,200)
        self.button.setFixedSize(200,50)


        self.button.setStyleSheet("""
            QPushButton {
                font-family: Arial;
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

        
        self.combo1 = QComboBox()
        
        self.combo1.addItem("Select an option...")  # Placeholder
        self.combo1.setCurrentIndex(0)

        self.combo1.model().item(0).setEnabled(False)

    
        self.combo1.addItems(["Binary search", "Quick sort", "Linear search"])
        self.combo1.currentTextChanged.connect(self.update_label)
        # self.combo1.currentTextChanged.connect(self.bin)
        # self.combo1.setFont(QFont("Arial,50"))

        
        self.combo2 = QComboBox()
        
        
        self.combo2.addItem("Select an option...")  # Placeholder
        self.combo2.setCurrentIndex(0)

        self.combo2.model().item(0).setEnabled(False)
        
        self.combo2.addItems(["bubble sort", "inseration sort", "exp sort"])
        self.combo2.currentTextChanged.connect(self.update_label)
        self.combo1.setFont(QFont("Arial,30"))
        
        self.combo1.setStyleSheet("""
        QWidget {
                background-color: #FFFFFF;
                background-repeat: no-repeat;
                background-position: center;
                background-attachment: fixed;  
                padding:4px 4px;
                border:none;   
            }
        """)
        font = QFont("Arial", 9)
        font.setBold(True)
        self.combo1.setFont(font)
        self.combo2.setStyleSheet("""
        QWidget {
                background-color: #FFFFFF;
                background-repeat: no-repeat;
                background-position: center;
                background-attachment: fixed;
                padding:4px 4px;

            }
        """)
        font = QFont("Arial", 9)
        font.setBold(True)
        self.combo2.setFont(font)
        self.central_widget.setStyleSheet("""
            QWidget {
                background-color: #0d1117;
                background-repeat: no-repeat;
                background-position: center;
                background-attachment: fixed;
            }
        """)
        
       
        
        dropdown_layout.addWidget(self.combo1)
        dropdown_layout.addWidget(self.combo2)

        
        self.label = QLabel("Make a selection...",self)
        self.label.setFont(QFont("Arial,30"))
        self.label.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        # self.label.setGeometry(QtCore.QRect(100,200,220,80))
        self.label.setStyleSheet("""font-size: 20px;
                                 font-family:Arial;
                                 color:#238636;""")
        self.label2 = QLabel(self)
        self.label2.setFont(QFont("Arial,30"))
        self.label2.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        # self.label.setGeometry(QtCore.QRect(100,200,220,80))
        self.label2.setStyleSheet("""font-size: 20px;
                                 font-family:Arial;
                                 color:#238636;""")



        
        main_layout.addLayout(dropdown_layout)
        main_layout.addWidget(self.label)
        button_layout.addWidget(self.button)
        main_layout.addLayout(button_layout)
        self.central_widget.setLayout(main_layout)



    def update_label(self):
        firstdropdown = self.combo1.currentText()
        seconddropdown = self.combo2.currentText()
        self.label.setText(f"Selected: {firstdropdown} & {seconddropdown}")
    def bin(self):
        # self.label2.setText(f"{searchman.search()}")
        pass

def main():
    app=QApplication(sys.argv)        
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()