from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


def info_btn_clicked():
    '''
    This function is used to show the info box in the menu.
    '''
    info_dialog = Info()
    info_dialog.exec_()


class Info(QDialog):
    def __init__(self):
        super(Info, self).__init__()
        loadUi("info.ui", self)
