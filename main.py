import sys

from logic1 import *


def main():
    """
    Makes the App run and creates the main window
    :return: none
    """
    app = QApplication(sys.argv)
    window1 = Logic1()
    window1.show()
    app.exec()


if __name__ == "__main__":
    main()
