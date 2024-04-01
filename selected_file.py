def move_file_up(list_widget):
    """
    Move the selected file up in the list.

    Parameters:
        list_widget (QListWidget): The QListWidget containing the files.
    """
    selected_file = list_widget.currentRow()
    if selected_file > 0:
        item = list_widget.takeItem(selected_file)
        list_widget.insertItem(selected_file - 1, item)
        list_widget.setCurrentRow(selected_file - 1)

def move_file_down(list_widget):
    """
    Move the selected file down in the list.

    Parameters:
        list_widget (QListWidget): The QListWidget containing the files.
    """
    selected_file = list_widget.currentRow()
    if selected_file < list_widget.count() - 1:
        item = list_widget.takeItem(selected_file)
        list_widget.insertItem(selected_file + 1, item)
        list_widget.setCurrentRow(selected_file + 1)