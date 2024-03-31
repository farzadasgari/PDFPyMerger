from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType, loadUi
from time import sleep
from PyPDF2 import PdfMerger, PdfWriter, PdfReader

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
        self.addPDFButton.clicked.connect(self.get_files)
        self.deletePDFButton.clicked.connect(self.delete_file)
        self.hidePasswordButton.clicked.connect(self.hide_or_show_password)
        self.showPasswordButton.clicked.connect(self.hide_or_show_password)
        self.upPDFButton.clicked.connect(self.move_file_up)
        self.downPDFButton.clicked.connect(self.move_file_down)
        self.executeButton.clicked.connect(self.execute)

    def actions_triggered(self):
        self.actionInfo.triggered.connect(info_btn_clicked)

    def get_files(self):
        filedialog = QFileDialog()
        filedialog.setFileMode(QFileDialog.ExistingFiles)
        files = filedialog.getOpenFileNames(
            self, "Open PDF Files", "", "PDF Files (*.pdf);;Images (*.png *.jpg *.jpeg)"
        )
        self.append_files(files[0])

    def append_files(self, files):
        for file in files:
            QListWidgetItem(file, self.PDFList)

    def delete_file(self):
        file = self.PDFList.currentRow()
        self.PDFList.takeItem(file)

    def hide_or_show_password(self) -> None:
        if self.passwordInput.echoMode() == QLineEdit.EchoMode.Password:
            self.passwordInput.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.passwordInput.setEchoMode(QLineEdit.EchoMode.Password)

    def move_file_up(self):
        filerow = self.PDFList.currentRow()
        file = self.PDFList.takeItem(filerow)
        self.PDFList.insertItem(filerow - 1, file)
        target = filerow if filerow == 0 else filerow - 1
        self.PDFList.setCurrentRow(target)

    def move_file_down(self):
        filerow = self.PDFList.currentRow()
        file = self.PDFList.takeItem(filerow)
        self.PDFList.insertItem(filerow + 1, file)
        target = filerow if filerow == self.PDFList.count() - 1 else filerow + 1
        self.PDFList.setCurrentRow(target)

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
            merge.write("MyPath3445.pdf")
            merge.close()
            password = self.passwordInput.text()
            if len(password) != 0:
                reader = PdfReader("MyPath3445.pdf")
                writer = PdfWriter()
                for page in reader.pages:
                    writer.add_page(page)
                writer.encrypt(password)
                writer.write("MyPath3445.pdf")
        else:
            print("I am Error")


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
