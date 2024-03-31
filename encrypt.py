from PyQt5.QtWidgets import QLineEdit


def hide_or_show_password(passinput) -> None:
    """
    Toggle between hiding and showing the password input.
    
    Parameters:
        passinput (QLineEdit): The password input field.
    """
    
    if passinput.echoMode() == QLineEdit.EchoMode.Password:
        passinput.setEchoMode(QLineEdit.EchoMode.Normal)
    else:
        passinput.setEchoMode(QLineEdit.EchoMode.Password)
