from PyQt5.QtWidgets import QLineEdit


def hide_or_show_password(passinput) -> None:
    '''
    This function is used to change the password mode to Hide(*******) or Show. 
    By pressing the eye button, this mode change is displayed.
    '''
    if passinput.echoMode() == QLineEdit.EchoMode.Password:
        passinput.setEchoMode(QLineEdit.EchoMode.Normal)
    else:
        passinput.setEchoMode(QLineEdit.EchoMode.Password)
