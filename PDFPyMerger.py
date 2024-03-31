from PyQt5.QtWidgets import QApplication
from main_application import PyPDFMerger
import sys


def main():
    """
    Entry point of the PDFPyMerger application.
    Initializes the PyQt application, creates the main window, and starts the event loop.
    """
    app = QApplication(sys.argv)
    window = PyPDFMerger()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
