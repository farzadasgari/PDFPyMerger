from PyQt5.QtWidgets import QApplication
from main_application import PyPDFMerger
import sys


def main():
    '''
    Execute PDFPyMerger
    '''
    app = QApplication(sys.argv)
    window = PyPDFMerger()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
