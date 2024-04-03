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
        None, "Open Files", "", "PDF Files (*.pdf);;Images (*.png *.jpg *.jpeg);; All Files(*)"
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
    text_browser.clear()
    if file[0].lower().endswith('.pdf'):
        for line in get_pdf_lines(file[0]):
            text_browser.append(line)



def get_pdf_lines(path):
    """
    Extract text lines from a PDF file.

    Description:
        reads a PDF file located at the specified path and yields each line of text
        extracted from the PDF pages using PyPDF2 library.

    Parameters:
        path (str): The file path to the PDF file to be processed.

    Yields:
        str: Each line of text extracted from the PDF file.

    Raises:
        FileNotFoundError: If the specified PDF file is not found.
        Exception: Any exception raised during the PDF processing.
    """
    from PyPDF2 import PdfReader

    try:
        # Open the PDF file in read-binary mode
        with open(path, 'rb') as f:
            # Create a PdfReader object to read the PDF file
            pdf_reader = PdfReader(f)

            # Iterate over each page in the PDF file
            for page in pdf_reader.pages:
                # Extract text from the current page and split it into lines
                for line in page.extract_text().splitlines():
                    # Yield each line of text
                    yield line
    except FileNotFoundError:
        # Raise an exception if the specified PDF file is not found
        raise FileNotFoundError("PDF file not found at the specified path: {}".format(path))
    except Exception as e:
        # Raise any other exceptions that occur during PDF processing
        raise Exception("An error occurred during PDF processing: {}".format(str(e)))
