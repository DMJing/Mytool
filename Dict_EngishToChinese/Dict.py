# -*- coding: utf-8 -*-
import os
import sys
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QComboBox, QWidget
from DictMain import Ui_DictMain


def ReadFile(FileName):
    with open(FileName, 'r', encoding='utf-8',errors="ignore") as f:
        lines = f.readlines()
    return lines

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_DictMain()
        self.ui.setupUi(self)

    def closewindow(self):
        self.close()

    def AnalysisFile(self):
        global lines
        global lines1
        lines = ReadFile("DictData.py")
        lines1 = [0]*len(lines)
        i = 0
        for line in lines:
            str1 = line.replace('\n','')
            str1 = str1.split(' ')
            lines1[i] = str1[0]
            i += 1


    def GetDictData(self):
        self.ui.DisPlay.setText('')
        FindA = self.ui.Input.text()
        if FindA == '':
            self.ui.DisPlay.setText('')
        self.ui.DisPlay.textCursor().setPosition(0)
        i = 0
        for line in lines1:
            if FindA in line and FindA!= '':
                self.ui.DisPlay.append(str(lines[i]))
            i+=1


        cursor = self.ui.DisPlay.textCursor()
        cursor.movePosition(QTextCursor.Start)
        self.ui.DisPlay.setTextCursor(cursor)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Main = MainWindow()
    Main.show()
    Main.AnalysisFile()

    sys.exit(app.exec_())