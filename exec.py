from time import sleep
from PyPDF2 import PdfMerger, PdfReader, PdfWriter
from PyQt5.QtWidgets import QFileDialog


def merger(parent):
    # Execute the Actions
    files = []
    for file in range(parent.PDFList.count()):
        files.append(parent.PDFList.item(file).text())
    if files:
        merge = PdfMerger()
        for i, file in enumerate(files):
            sleep(0.005)
            merge.append(file)
            parent.progressBar.setValue(round((i + 1) * (100 / len(files))))
        parent.progressBar.setValue(100)
        path = save_merged_file(parent)
        if not path == "":
            if not path.lower().endswith('.pdf'):
                path += path + '.pdf'
            merge.write(path)
            merge.close()
            password = parent.passwordInput.text()
            if len(password) != 0:
                reader = PdfReader(path)
                writer = PdfWriter()
                for page in reader.pages:
                    writer.add_page(page)
                writer.encrypt(password)
                writer.write(path)
            from subprocess import Popen
            Popen(path, shell=True)


def save_merged_file(parent):
    filedialog = QFileDialog()
    filedialog.setFileMode(QFileDialog.ExistingFiles)
    filepath, _ = QFileDialog.getSaveFileName(parent, "Save Merged File",
                                              "PDFPyMerger.pdf"
                                              , "PDF Files (*.pdf)")
    return filepath
