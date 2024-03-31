'''
PDF Merger:

This Python application designed to merge multiple PDF files into a single document with 
the ability to protect the merged PDF file with a password.

Required libraries:

PyQt5 = PyQt is a Python binding of the cross-platform GUI toolkit Qt, implemented as a Python plug-in.

Pillow = The Python Imaging Library adds image processing capabilities to your Python interpreter.

PyPDF2 = PyPDF2 is a free and open source pure-python PDF library capable of splitting, merging, cropping, 
 and transforming the pages of PDF files.

img2pdf = Convert images to PDF via direct JPEG inclusion.

'''
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUiType
from file_handling import get_files, delete_file
from files_order import move_file_up, move_file_down
from encrypt import hide_or_show_password
from exec import merger
from info_dialog import info_btn_clicked

gui, _ = loadUiType("gui.ui")


class PyPDFMerger(QMainWindow, gui):
    '''
    The application environment is designed with this class
    '''
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.hidePasswordButton.hide()
        self.progressBar.hide()
        self.actions_triggered()
        self.buttons_clicked()

    def buttons_clicked(self):
        self.addPDFButton.clicked.connect(lambda: get_files(self.PDFList))
        self.deletePDFButton.clicked.connect(lambda: delete_file(self.PDFList))
        self.hidePasswordButton.clicked.connect(lambda: hide_or_show_password(self.passwordInput))
        self.showPasswordButton.clicked.connect(lambda: hide_or_show_password(self.passwordInput))
        self.upPDFButton.clicked.connect(lambda: move_file_up(self.PDFList))
        self.downPDFButton.clicked.connect(lambda: move_file_down(self.PDFList))
        self.executeButton.clicked.connect(lambda: merger(self))

    def actions_triggered(self):
        self.actionInfo.triggered.connect(info_btn_clicked)
