def move_file_up(list_widget):
    '''
    This function is used to change the arrangement of the file upwards. 
    '''
    filerow = list_widget.currentRow()
    file = list_widget.takeItem(filerow)
    list_widget.insertItem(filerow - 1, file)
    target = filerow if filerow == 0 else filerow - 1
    list_widget.setCurrentRow(target)


def move_file_down(list_widget):
    '''
    This function is used to change the arrangement of the file downwards. 
    '''
    filerow = list_widget.currentRow()
    file = list_widget.takeItem(filerow)
    list_widget.insertItem(filerow + 1, file)
    target = filerow if filerow == list_widget.count() - 1 else filerow + 1
    list_widget.setCurrentRow(target)
