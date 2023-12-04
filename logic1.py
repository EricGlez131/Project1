from PyQt6.QtWidgets import *
from gui1 import *
from logic2 import *


class Logic1(QMainWindow, Ui_Gui1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.push_submit.clicked.connect(lambda: self.submit())

    def openWindow(self, studentsNUM):
        secondWindow = Logic2()
        secondWindow.show()
        secondWindow.studentsLabelNum.setText(str(studentsNUM))

    def submit(self):
        try:
            StudentNum = int(self.Number_Student.text())
            self.openWindow(StudentNum)
            self.Number_Student.clear()
        except:
            self.label_editLine.setText(f'Enter an Integer value')
