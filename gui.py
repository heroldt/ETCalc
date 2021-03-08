import sys
from PyQt5 import QtWidgets, uic, QtCore
import et_calc

class MainDialog(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = uic.loadUi("main.ui", self)
        #Slot init
        self.ui.calcButton.clicked.connect(self.onCalcButtonClicked)
        self.ui.action_about.triggered.connect(self.onAboutClicked)

    def clearResultField(self):
        self.ui.label_result.clear()
        
    def onCalcButtonClicked(self):
        self.clearResultField()
        erow = str(self.ui.comboBox_eRow.currentText())
        value = int(self.ui.lineEdit_value.text())
        dev, eval = et_calc.get_closest_erow_value(value,et_calc.e_rows[erow])
        self.ui.label_result.setText("Nearest Value: %.3f (%+.1f%%)" % (eval, (eval/value-1)*100))

    def onAboutClicked(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setText("Copyright Thomas Herold (c) 2021")
        msgBox.setWindowTitle("About")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

app = QtWidgets.QApplication(sys.argv)
dialog = MainDialog()
dialog.show()
dialog.clearResultField()
sys.exit(app.exec_())
