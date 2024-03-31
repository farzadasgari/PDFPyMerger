from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType, loadUi
from file_handling import get_files, delete_file
from files_order import move_file_up, move_file_down
from encrypt import hide_or_show_password
from exec import merger
from info_dialog import info_btn_clicked

gui, _ = loadUiType("gui.ui")


class Merger(QMainWindow, gui):
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


def main():
    app = QApplication(sys.argv)
    window = Merger()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
