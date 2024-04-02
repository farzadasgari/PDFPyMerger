from time import sleep
from PyPDF2 import PdfMerger, PdfReader, PdfWriter
from PyQt5.QtWidgets import QFileDialog
import img2pdf
from PIL import Image
import os
import pyttsx3

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
                    image = Image.open(file)
                    pdf_bytes = img2pdf.convert(image.filename)
                    image_pdf = open(f'{file}.pdf', "wb")
                    image_pdf.write(pdf_bytes)
                    image_pdf.write(pdf_bytes)
                    image.close()
                    image_pdf.close()
                    merge.append(f'{file}.pdf')
                    photo_list.append(f'{file}.pdf') if f'{file}.pdf' not in photo_list else None
                else:
                    merge.append(file)
                # Update progress bar
                parent.progressBar.setValue(round((i + 1) * (100 / len(files))))
            parent.progressBar.setValue(100)
        except:
            merge.close()
            [os.remove(path) for path in photo_list if photo_list]
            parent.progressBar.setValue(0)
            parent.progressBar.hide()
            return None
        # Save the merged PDF file
        path = save_merged_file(parent)
        if not path == "":
            # Ensure the file has a PDF extension
            if not path.lower().endswith('.pdf'):
                path += path + '.pdf'
            merge.write(path)  # Write the merged PDF to the specified path
            merge.close()  # Close the merger
            [os.remove(path) for path in photo_list if photo_list]
            # If a password is provided, encrypt the PDF file
            password = parent.passwordInput.text()
            if len(password) != 0:
                reader = PdfReader(path)
                writer = PdfWriter()
                for page in reader.pages:
                    writer.add_page(page)
                writer.encrypt(password)
                writer.write(path)

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
                                              "PDFPyMerger.pdf"
                                              , "PDF Files (*.pdf)")
    return filepath


def speech(parent):
    """
    Convert PDF files to speech using pyttsx3 library.

    Parameters:
        parent (QWidget): The parent widget (main window) of the application.
    """
    files = []
    for file in range(parent.PDFList.count()):
        files.append(parent.PDFList.item(file).text())

    if files:
        engine = pyttsx3.init()
        for file in files:
            with open(file, 'rb') as f:
                pdf_reader = PdfReader(f)
                for page in pdf_reader.pages:
                    text = page.extract_text()
                    if text:
                        engine.say(text)
                        engine.runAndWait()