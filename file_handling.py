from PyQt5.QtWidgets import QFileDialog, QListWidgetItem


def get_files(list_widget):
    """
    Open a dialog to allow users to select files and add them to the list.

    Parameters:
        list_widget (QListWidget): The QListWidget to which files will be added.
    """
    filedialog = QFileDialog()
    filedialog.setFileMode(QFileDialog.ExistingFiles)
    files = filedialog.getOpenFileNames(
        None, "Open PDF Files", "", "PDF Files (*.pdf);;Images (*.png *.jpg *.jpeg);; All Files(*)"
    )
    if files[0]:
        if not files[0][0].lower().endswith(('.pdf', '.png', '.jpg', '.jpeg')):
            print('This format not available!')
        else:
            append_files(files[0], list_widget)


def append_files(files, list_widget):
    """
    Add files to the list widget.

    Parameters:
        files (list): List of file paths to be added.
        list_widget (QListWidget): The QListWidget to which files will be added.
    """
    for file in files:
        QListWidgetItem(file, list_widget)


def delete_file(list_widget):
    """
    Delete the selected file from the list.

    Parameters:
        list_widget (QListWidget): The QListWidget from which the file will be deleted.
    """
    file = list_widget.currentRow()
    list_widget.takeItem(file)


def get_file(text_browser):
    """
    Open a dialog to allow users to select files and add it for Text to Speech Process.

    Parameters:
        text_browser (QTextBrowser): The QTextBrowser which shows the extracted lines of selected PDF file.
    """
    filedialog = QFileDialog()
    filedialog.setFileMode(QFileDialog.ExistingFiles)
    file = filedialog.getOpenFileName(
        None, "Open PDF File", "", "PDF Files (*.pdf);; All Files(*)"
    )
    
    for line in get_pdf_lines(file[0]):
        text_browser.append(line)


def get_pdf_lines(path):
    from PyPDF2 import PdfReader
    with open(path, 'rb') as f:
        pdf_reader = PdfReader(f)
        for page in pdf_reader.pages:
            for line in page.extract_text().splitlines():
                yield line        