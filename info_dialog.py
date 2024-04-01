from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


def info_btn_clicked():
    """
    Show the info box when the info action is clicked.
    """
    info_dialog = Info()
    info_dialog.exec_()


class Info(QDialog):
    """
    Class for displaying the information dialog.

    Attributes:
        Inherits from QDialog.
    """
    def __init__(self):
        super(Info, self).__init__()
        loadUi("info.ui", self)
