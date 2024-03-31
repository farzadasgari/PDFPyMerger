from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType, loadUi
from time import sleep
from PyPDF2 import PdfMerger, PdfWriter, PdfReader
from file_handling import get_files, delete_file
from files_order import move_file_up, move_file_down

gui, _ = loadUiType("gui.ui")


def info_btn_clicked():
    info_dialog = Info()
    info_dialog.exec_()


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
        self.hidePasswordButton.clicked.connect(self.hide_or_show_password)
        self.showPasswordButton.clicked.connect(self.hide_or_show_password)
        self.upPDFButton.clicked.connect(lambda: move_file_up(self.PDFList))
        self.downPDFButton.clicked.connect(lambda: move_file_down(self.PDFList))
        self.executeButton.clicked.connect(self.execute)

    def actions_triggered(self):
        self.actionInfo.triggered.connect(info_btn_clicked)

    def hide_or_show_password(self) -> None:
        if self.passwordInput.echoMode() == QLineEdit.EchoMode.Password:
            self.passwordInput.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.passwordInput.setEchoMode(QLineEdit.EchoMode.Password)

    def execute(self):
        # Execute the Actions
        files = []
        for file in range(self.PDFList.count()):
            files.append(self.PDFList.item(file).text())
        if files:
            merge = PdfMerger()
            for i, file in enumerate(files):
                sleep(0.005)
                merge.append(file)
                self.progressBar.setValue(round((i + 1) * (100 / len(files))))
            self.progressBar.setValue(100)
            path = self.save_merged_file()
            if not path == "":
                if not path.lower().endswith('.pdf'):
                    path += path + '.pdf'
                merge.write(path)
                merge.close()
                password = self.passwordInput.text()
                if len(password) != 0:
                    reader = PdfReader(path)
                    writer = PdfWriter()
                    for page in reader.pages:
                        writer.add_page(page)
                    writer.encrypt(password)
                    writer.write(path)
                from subprocess import Popen
                Popen(path, shell=True)

    def save_merged_file(self):
        filedialog = QFileDialog()
        filedialog.setFileMode(QFileDialog.ExistingFiles)
        filepath, _ = QFileDialog.getSaveFileName(self, "Save Merged File",
                                                  "PDFPyMerger.pdf"
                                                  , "PDF Files (*.pdf)")
        return filepath


class Info(QDialog):
    def __init__(self):
        super(Info, self).__init__()
        loadUi("info.ui", self)


def main():
    app = QApplication(sys.argv)
    window = Merger()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
