import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout, QMessageBox, QScrollArea
from hackyaosring import haosring_sign, convert_hex_to_int_pairs,hex_string_to_int_tuple
import pyperclip

class Alice_ring(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
    # create the input fields
        self.msg = QLineEdit()
        self.pukeys = QLineEdit()
        self.pair = QLineEdit()
        self.privatekey = QLineEdit()
    


        # create the button to trigger the function
        self.button = QPushButton('Sign')
        self.button.clicked.connect(self.runFunction)

        # create the label to display the result
        self.resultLabel1 = QLineEdit()
        self.resultLabel2 = QLineEdit()
        self.resultLabel3 = QLineEdit()

        # create the scroll area to hold the result label
        scrollArea = QScrollArea()
        scrollArea.setWidgetResizable(True)
        scrollWidget = QWidget()
        scrollLayout = QVBoxLayout(scrollWidget)
        scrollLayout.addWidget(self.resultLabel1)
        scrollLayout.addWidget(self.resultLabel2)
        scrollLayout.addWidget(self.resultLabel3)
        scrollArea.setWidget(scrollWidget)

        # create the button to copy the result to the clipboard
        self.copyButton1 = QPushButton('Copy')
        self.copyButton1.clicked.connect(self.copyResult1)
        self.copyButton2 = QPushButton('Copy')
        self.copyButton2.clicked.connect(self.copyResult2)
        self.copyButton3 = QPushButton('Copy')
        self.copyButton3.clicked.connect(self.copyResult3)

        # create the layout
        grid = QGridLayout()
        grid.addWidget(QLabel('Your private key:'), 0, 0)
        grid.addWidget(self.privatekey, 0, 1)
        grid.addWidget(QLabel('Address to receive the SBT'), 1, 0)
        grid.addWidget(self.msg, 1, 1)
        grid.addWidget(QLabel('Keys of the ring:'), 2, 0)
        grid.addWidget(self.pukeys, 2, 1)
        grid.addWidget(QLabel('Your keys:'), 3, 0)
        grid.addWidget(self.pair, 3, 1)
        grid.addWidget(self.button, 4, 0, 1, 2)
        grid.addWidget(QLabel('Addresses:'), 5, 0)
        grid.addWidget(self.resultLabel1, 5, 1)
        grid.addWidget(self.copyButton1, 5, 2)
        grid.addWidget(QLabel('Tees:'), 6, 0)
        grid.addWidget(self.resultLabel2, 6, 1)
        grid.addWidget(self.copyButton2, 6, 2)
        grid.addWidget(QLabel('Sig:'), 7, 0)
        grid.addWidget(self.resultLabel3, 7, 1)
        grid.addWidget(self.copyButton3, 7, 2)
        # grid.addWidget(QLabel(''), 7, 0) # dummy widget to fill up the space
        # grid.addWidget(scrollArea, 8, 1)
        # grid.addWidget(QLabel(''), 9, 0) # dummy widget to fill up the space
        # grid.addWidget(QLabel(''), 10, 0) # dummy widget to fill up the space

        # set the layout
        self.setLayout(grid)

        # set the window properties
        self.setGeometry(200, 200, 700, 700)
        self.setWindowTitle('Alice Ring')
        self.show()

    

    def runFunction(self):
        # get the input values
        privakey = self.privatekey.text()
        msg = self.msg.text()
        pkey = self.pukeys.text()
        yourkey = self.pair.text()
        yourkeyInt = hex_string_to_int_tuple(yourkey)
        yourpair = [(yourkeyInt),int(privakey,16)]
        pkeyInt = convert_hex_to_int_pairs(pkey)
        

        # call the function and get the result
        #result = haosring_sign(pkeys= (convert_hex_to_int_pairs(pkey)),mypair= yourpair,message= int(msg,16))
        result = haosring_sign(pkeys= pkeyInt,mypair= yourpair,message= int(msg,16))
        result1 = str(result[0])
        result2 = str(result[1])
        result3 = str(result[2])

        # display the result in the label
        self.resultLabel1.setText(result1)
        self.resultLabel2.setText(result2)
        self.resultLabel3.setText(result3)

    

    def copyResult1(self):
        # get the result text
        resultText = self.resultLabel1.text()

        # copy the result to the clipboard
        pyperclip.copy(resultText)

        # show a message box to confirm the copy
        QMessageBox.information(self, 'Copy', 'Result copied to clipboard.')

    def copyResult2(self):
        # get the result text
        resultText = self.resultLabel2.text()

        # copy the result to the clipboard
        pyperclip.copy(resultText)

        # show a message box to confirm the copy
        QMessageBox.information(self, 'Copy', 'Result copied to clipboard.')

    def copyResult3(self):
        # get the result text
        resultText = self.resultLabel3.text()   

        # copy the result to the clipboard
        pyperclip.copy(resultText)

        # show a message box to confirm the copy
        QMessageBox.information(self, 'Copy', 'Result copied to clipboard.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Alice_ring()
    sys.exit(app.exec_())
