from time import sleep
from PyPDF2 import PdfMerger, PdfReader, PdfWriter


def merger(self):
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