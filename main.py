from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
import sys

class LoginPage(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500, 500)
        self.setWindowTitle('Live coding')
        self.ui()
    
    def ui(self):
        self.main_layout = QtWidgets.QFormLayout(self)
        self.label = QtWidgets.QLabel('Connexion')
        self.label.setAlignment(QtCore.Qt.AlignHCenter)
        self.label.setMargin(30)
        self.label.setFont(QtGui.QFont('Alata', 20))
        self.main_layout.addRow(self.label)
        self.name_label = QtWidgets.QLabel('nom:')
        self.name_label.setFont(QtGui.QFont('Alata', 13))
        self.name_input = QtWidgets.QLineEdit()
        self.email_label = QtWidgets.QLabel('email:')
        self.email_label.setFont(QtGui.QFont('Alata', 13))
        self.email_input = QtWidgets.QLineEdit()
        self.remember_me = QtWidgets.QCheckBox('Se souvenir de moi')
        self.remember_me.setFont(QtGui.QFont('Alata', 13))
        self.add_widgets_to_form_layout(
            self.main_layout,
            self.name_label,
            self.name_input,
            self.email_label,
            self.email_input,
            self.remember_me
            )

    def add_widgets_to_form_layout(self, parent, *args):
        """Adds widget(s) to parent in parameter"""
        for i in range(0, len(args), 2):
            parent.addRow(args[i]) if args[i] == args[-1] else parent.addRow(args[i], args[i+1])


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # dir = QtCore.QDir('font')
    QtGui.QFontDatabase.addApplicationFont("font/Alata-Regular.ttf")
    login_page = LoginPage()
    login_page.show()
    sys.exit(app.exec_())