import sys
from PyQt5 import QtWidgets, uic, QtCore
import et_calc

class MainDialog(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = uic.loadUi("main.ui", self)
        #Slot init
        self.ui.calcButton.clicked.connect(self.onCalcButtonClicked)  #Calc Button
        self.ui.lineEdit_value.returnPressed.connect(self.onCalcButtonClicked) #Press Enter in Input Field
        self.ui.action_about.triggered.connect(self.onAboutClicked)
        self.ui.actionReset.triggered.connect(self.clearAll)
        self.ui.actionBeenden.triggered.connect(self.quit)

    def clearResultField(self):
        self.ui.label_result.clear()

    def clearAll(self):
        self.clearResultField()
        self.ui.lineEdit_value.clear()

    def quit(self):
        QtWidgets.QApplication.quit()
        
    def onCalcButtonClicked(self):
        unit = ''
        self.clearResultField()
        unit = str(self.ui.comboBox_prefix.currentText())
        if self.ui.radioButton_res.isChecked() == True:
            unit += "\u03A9"
        elif self.ui.radioButton_ind.isChecked() == True:
            unit += "H"
        elif self.ui.radioButton_cap.isChecked() == True:
            unit += "F"
        erow = str(self.ui.comboBox_eRow.currentText())
        try:
            value = int(self.ui.lineEdit_value.text())
            if value <= 0:
                self.ui.label_result.setText("Nur positive Zahlen > 0 erlaubt")
                return
        except:
            self.ui.label_result.setText("Ungültige Eingabe")
            return
        dev, eval = et_calc.get_closest_erow_value(value,et_calc.e_rows[erow])
        self.ui.label_result.setText("Nächster Wert: %.3f %s (%+.1f%%)" % (eval, unit, (eval/value-1)*100))

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
