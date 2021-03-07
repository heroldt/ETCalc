import sys
from PyQt5 import QtWidgets, uic, QtCore
import et_calc

class MainDialog(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = uic.loadUi("main.ui", self)
        #Slot init
        self.ui.calcButton.clicked.connect(self.onCalcButtonClicked)

    def clearResultField(self):
        self.ui.label_result.clear()
        
    def onCalcButtonClicked(self):
        self.clearResultField()
        erow = str(self.ui.comboBox_eRow.currentText())
        value = int(self.ui.lineEdit_value.text())
        dev, eval = et_calc.get_closest_erow_value(value,et_calc.e_rows[erow])
        self.ui.label_result.setText("Nearest Value: %.3f" % (eval))

app = QtWidgets.QApplication(sys.argv)
dialog = MainDialog()
dialog.show()
dialog.clearResultField()
sys.exit(app.exec_())