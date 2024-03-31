from PyQt5.QtWidgets import QFileDialog, QListWidgetItem


def get_files(list_widget):
    filedialog = QFileDialog()
    filedialog.setFileMode(QFileDialog.ExistingFiles)
    files = filedialog.getOpenFileNames(
        None, "Open PDF Files", "", "PDF Files (*.pdf);;Images (*.png *.jpg *.jpeg);; All Files(*)"
    )
    append_files(files[0], list_widget)


def append_files(files, list_widget):
    for file in files:
        QListWidgetItem(file, list_widget)


def delete_file(list_widget):
    file = list_widget.currentRow()
    list_widget.takeItem(file)
