from PyQt5.QtWidgets import QApplication
from main_application import PyPDFMerger
from sys import argv


def main():
    app = QApplication(argv)
    window = PyPDFMerger()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
