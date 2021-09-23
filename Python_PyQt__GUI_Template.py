
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QGridLayout, QGroupBox, QPushButton, QLineEdit
#from PyQt5.QtWidgets import QLabel, QFileDialog, QRadioButton, QComboBox

class App(QDialog):
    def __init__(self):
        # Add fields here

        super().__init__()
        self.title = "Title"
        self.left = 0
        self.top = 0
        self.width = 600
        self.height = 100
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        windowLayout = QGridLayout()

        self.config_settings()
        windowLayout.addWidget(self.upper_left_section, 0, 0)
        #windowLayout.addWidget(self.upper_right_section, 0, 1)
        #windowLayout.addWidget(self.lower_left_section, 1, 0)
        #windowLayout.addWidget(self.lower_right_section, 1, 1)

        self.setLayout(windowLayout)
        self.show()

    def do_this(self):
        return
        
    def config_settings(self):
        upper_left_layout = QGridLayout()
        
        self.upper_left_section = QGroupBox("GroupBox 1")
        self.upper_left_section.setLayout(upper_left_layout)

        self.editedable_field = QLineEdit()
        upper_left_layout.addWidget(self.editedable_field, 0, 1)

        self.btn = QPushButton("Button 1")
        self.btn.clicked.connect(self.do_this)     
        upper_left_layout.addWidget(self.btn, 0, 2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()

    sys.exit(app.exec_())
