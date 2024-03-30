from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType, loadUi

gui, _ = loadUiType('gui.ui')


def info_btn_clicked():
    info_dialog = Info()
    info_dialog.exec_()


class Merger(QMainWindow, gui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.hidePasswordButton.hide()
        self.actions_triggered()
        self.buttons_clicked()

    def buttons_clicked(self):
        self.addPDFButton.clicked.connect(self.get_files)
        self.deletePDFButton.clicked.connect(self.delete_file)

    def actions_triggered(self):
        self.actionInfo.triggered.connect(info_btn_clicked)

    def get_files(self):
        filedialog = QFileDialog()
        filedialog.setFileMode(QFileDialog.ExistingFiles)
        files = filedialog.getOpenFileNames(self, "Open PDF Files", "", "PDF Files (*.pdf)")
        self.append_files(files[0])

    def append_files(self, files):
        for file in files:
            QListWidgetItem(file, self.PDFList)

    def delete_file(self):
        file = self.PDFList.currentRow()
        self.PDFList.takeItem(file)


class Info(QDialog):
    def __init__(self):
        super(Info, self).__init__()
        loadUi('info.ui', self)


def main():
    app = QApplication(sys.argv)
    window = Merger()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
