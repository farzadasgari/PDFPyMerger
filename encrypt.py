from PyQt5.QtWidgets import QLineEdit


def hide_or_show_password(passinput) -> None:
    if passinput.echoMode() == QLineEdit.EchoMode.Password:
        passinput.setEchoMode(QLineEdit.EchoMode.Normal)
    else:
        passinput.setEchoMode(QLineEdit.EchoMode.Password)
