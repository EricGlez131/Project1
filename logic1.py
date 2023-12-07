from PyQt6.QtWidgets import *
from gui1 import *
from logic2 import *


class Logic1(QMainWindow, Ui_Gui1):
    def __init__(self):
        """
        In this function it setsUP the gui calling both super and setupUI in the actual GUI itself
        """
        super().__init__()
        self.setupUi(self)

        self.push_submit.clicked.connect(lambda: self.submit())

    def openWindow(self, studentsNUM) -> None:
        """
        this method is used for the creation of the second window which is the actual claculator
        :param studentsNUM: total number of students being sent to the next GUI
        :return: does not return anything but creates another window
        """
        self.hide()
        self.secondWindow = Logic2(self)
        self.secondWindow.show()
        self.secondWindow.studentsLabelNum.setText(str(studentsNUM))

    def submit(self) -> None:
        """
        this function is for the submit button to work and also checks that the input is an int with exception
        handling and call the openWindow Button when the button is pressed
        :return:
        """
        try:
            StudentNum = int(self.Number_Student.text())
            self.openWindow(StudentNum)
            self.Number_Student.clear()
        except:
            self.label_editLine.setText(f'Enter an Integer value')
            self.Number_Student.clear()
            self.Number_Student.setFocus()
