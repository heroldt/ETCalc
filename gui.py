import sys
from types import prepare_class
from PyQt5 import QtWidgets, uic, QtCore
import et_calc

class MainDialog(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = uic.loadUi("main.ui", self)
        #Slot init
        ## tab next value
        self.ui.calcButton.clicked.connect(self.onCalcButtonClicked)  #Calc Button
        self.ui.lineEdit_value.returnPressed.connect(self.onCalcButtonClicked) #Press Enter in Input Field
        ## tab voltage divider
        self.ui.calcButton_2.clicked.connect(self.OnVDCalcButtonClicked)
        self.ui.lineEdit_value_2.returnPressed.connect(self.OnVDCalcButtonClicked)
        
        self.ui.action_about.triggered.connect(self.onAboutClicked)
        self.ui.actionReset.triggered.connect(self.clearAll)
        self.ui.actionBeenden.triggered.connect(self.quit)

    def clearResultField(self):
        self.ui.label_result.clear()

    def clearAll(self):
        self.clearResultField()
        self.ui.label_result_2.clear()
        self.ui.lineEdit_value.clear()
        self.ui.lineEdit_value_2.clear()

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
        eval = et_calc.get_closest_erow_values(value,3,et_calc.e_rows[erow])
        self.ui.label_result.setText("Nächste Werte: \n%.3f %s (%+.1f%%)\n%.3f %s (%+.1f%%)\n%.3f %s (%+.1f%%)" % (eval[0], unit, (eval[0]/value-1)*100,eval[1], unit, (eval[1]/value-1)*100,eval[2], unit, (eval[2]/value-1)*100))

    def OnVDCalcButtonClicked(self):
        self.ui.label_result_2.clear()
        try:
            value = float(self.ui.lineEdit_value_2.text())
            if value < 0 or value > 1:
                self.ui.label_result_2.setText("Gültiger Wertebereich: 0..1")
                return
        except:
            self.ui.label_result_2.setText("Ungültige Eingabe")
            return
        erow = str(self.ui.comboBox_eRow_2.currentText())
        e1,e2 = et_calc.get_vd_closest(value,et_calc.e_rows[erow])
        self.ui.label_result_2.setText("Nächste Werte: \n%.3f \n%.3f" % (e1, e2))

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
