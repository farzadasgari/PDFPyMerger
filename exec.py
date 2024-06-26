from time import sleep
import PyPDF2.errors
from PyPDF2 import PdfMerger, PdfReader, PdfWriter
from PyQt5.QtWidgets import QFileDialog
import img2pdf
from PIL import Image
import os


def remove_image(photo_list):
    [os.remove(path) for path in photo_list if photo_list]


def handling_errors(parent, merge, photo_list):
    # For Debugging
    merge.close()
    remove_image(photo_list)
    parent.progressBar.setValue(0)
    parent.progressBar.hide()


def add_metadata(parent, writer):
    # Add MetaData For Our PDF
    writer.add_metadata(
        {
            "/Author": parent.authorInput.text(),
            "/Producer": parent.producerInput.text(),
            "/Creator": parent.creatorInput.text(),
            "/Title": parent.titleInput.text(),
            "/Subject": parent.subjectInput.text(),
        }
    )


def image_to_pdf(file_path):
    image = Image.open(file_path)
    pdf_bytes = img2pdf.convert(image.filename)
    image_pdf = open(f'{file_path}.pdf', "wb")
    image_pdf.write(pdf_bytes)
    image.close()
    image_pdf.close()


def encrypt_file(parent, path, password):
    reader = PdfReader(path)
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    writer.encrypt(password)
    add_metadata(parent, writer)
    writer.write(path)


def merger(parent):
    """
    Merge PDF files selected by the user in the parent GUI window.

    Parameters:
        parent (QWidget): The parent widget (main window) of the application.

    Optional:
        If a password is provided in the parent GUI window's password input field,
        the merged PDF file will be encrypted with the provided password.
    """

    # Get the list of files selected by the user
    files = []
    for file in range(parent.PDFList.count()):
        files.append(parent.PDFList.item(file).text())

    # If there are selected files
    if files:
        merge = PdfMerger()
        # Merge PDF files one by one
        photo_list = []

        try:
            for i, file in enumerate(files):
                sleep(0.005)  # Add a small delay for better user experience
                if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                    image_to_pdf(file)
                    merge.append(f'{file}.pdf')
                    photo_list.append(f'{file}.pdf') if f'{file}.pdf' not in photo_list else None
                else:
                    merge.append(file)
                # Update progress bar
                parent.progressBar.setValue(round((i + 1) * (100 / len(files))))

            parent.progressBar.setValue(100)

        except PyPDF2.errors.FileNotDecryptedError:
            # If we encounter an encrypted file during processing, it will show us an error
            handling_errors(parent, merge, photo_list)
            print('There are Decrypted Files!')
            return None
        except Exception:
            # Raise any other exceptions that occur during PDF processing
            handling_errors(parent, merge, photo_list)
            print('This is an Error!')
            return None

        # Save the merged PDF file
        path = save_merged_file(parent)
        if not path == "":
            # Ensure the file has a PDF extension
            if not path.lower().endswith('.pdf'):
                path += path + '.pdf'
            add_metadata(parent, merge)
            merge.write(path)  # Write the merged PDF to the specified path
            merge.close()  # Close the merger
            remove_image(photo_list)
            # If a password is provided, encrypt the PDF file
            password = parent.passwordInput.text()
            if len(password) != 0:
                encrypt_file(parent, path, password)
            # Open the merged PDF file with the default PDF viewer
            from subprocess import Popen
            Popen(path, shell=True)
        parent.progressBar.setValue(0)
        parent.progressBar.hide()


def save_merged_file(parent):
    """
    Open a dialog window for the user to select the destination path to save the merged PDF file.

    Parameters:
        parent (QWidget): The parent widget (main window) of the application.

    Returns:
        filepath (str): The selected file path.
    """
    filedialog = QFileDialog()
    filedialog.setFileMode(QFileDialog.ExistingFiles)
    filepath, _ = QFileDialog.getSaveFileName(parent, "Save Merged File",
                                              "PDFPyMerger.pdf",
                                              "PDF Files (*.pdf)")
    return filepath


def speech(parent):
    """
    Convert text to speech using pyttsx3 library.

    Description:
        The Function Takes the text content from the specified QTextBrowser widget
        (parent.textToSpeechBrowser) and converts it to speech using the pyttsx3 library.

    Parameters:
        parent (QWidget): The parent widget (main window) of the application,
        from which the QTextBrowser widget containing the text to be converted
        to speech is accessed.

    Raises:
        RuntimeError: If no text content is found in the QTextBrowser widget.
        Exception: Any exception raised during the text-to-speech conversion process.
    """
    from pyttsx3 import init

    # Initialize the text-to-speech engine
    engine = init()

    # Retrieve the text content from the specified QTextBrowser widget
    text = parent.textToSpeechBrowser.toPlainText()

    # Check if text content is available
    if text:
        # Convert text to speech
        engine.say(text)
        engine.runAndWait()
    else:
        # Raise an exception if no text content is found
        raise RuntimeError("No text content found in the QTextBrowser widget.")
