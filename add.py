# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Add.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(843, 646)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setGeometry(QtCore.QRect(10, 10, 741, 601))
        self.widget_2.setStyleSheet("\n"
"border-bottom-right-radius:50px;\n"
"border-top-left-radius:50px;\n"
"background-color: rgb(27, 19, 57);\n"
"\n"
"")
        self.widget_2.setObjectName("widget_2")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(40, 20, 231, 571))
        self.label_4.setStyleSheet("\n"
"border-bottom-right-radius:50px;\n"
"border-top-left-radius:50px;\n"
"background-color: rgb(27, 19, 57);\n"
"\n"
"")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../../Images/GestionStock.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setGeometry(QtCore.QRect(200, 20, 491, 51))
        font = QtGui.QFont()
        font.setFamily("Snap ITC")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(181, 120, 255);\n"
"font: 28pt \"Snap ITC\";\n"
"")
        self.label_6.setObjectName("label_6")
        self.namefield = QtWidgets.QLineEdit(self.widget_2)
        self.namefield.setGeometry(QtCore.QRect(100, 90, 191, 41))
        self.namefield.setStyleSheet("background-color: rgb(27, 19, 57);\n"
"color: rgb(255, 230, 250);\n"
"\n"
"\n"
"border:none;\n"
"border-bottom :2px solid ;\n"
"border-bottom-color: rgb(255, 170, 255);\n"
"padding-bottom:7px;\n"
"\n"
"\n"
"")
        self.namefield.setObjectName("namefield")
        self.btn_add1 = QtWidgets.QPushButton(self.widget_2)
        self.btn_add1.setGeometry(QtCore.QRect(180, 520, 341, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setStrikeOut(False)
        self.btn_add1.setFont(font)
        self.btn_add1.setStyleSheet("QPushButton#btn_add1{\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgb(181, 120, 255), stop:1 rgb(255, 170, 255));\n"
"\n"
"    color:rgba(255, 255, 255, 210);\n"
"\n"
"    border-radius:5px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton#btn_add1:hover{\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgb(181, 120, 255), stop:1 rgb(255, 170, 255));\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton#btn_add1:pressed{\n"
"\n"
"    padding-left:5px;\n"
"\n"
"    padding-top:5px;\n"
"\n"
"    background-color:rgb(251, 130, 255);\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton#btn_add1, #btn_add1, #btn_add1, #btn_add1{\n"
"\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"\n"
"    color:rgb(251, 130, 255);\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton#btn_add1:hover, #btn_add1:hover, #btn_add1:hover, #btn_add1:hover{\n"
"\n"
"    color: rgb(251, 130, 255);\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton#btn_add1:pressed, #btn_add1:pressed, #btn_add1:pressed, #btn_add1:pressed{\n"
"\n"
"    padding-left:5px;\n"
"\n"
"    padding-top:5px;\n"
"\n"
"    color:rgb(251, 130, 255);;\n"
"\n"
"}\n"
"\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ic/icons8-ajouter-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_add1.setIcon(icon)
        self.btn_add1.setIconSize(QtCore.QSize(50, 50))
        self.btn_add1.setObjectName("btn_add1")
        self.seuilfield = QtWidgets.QLineEdit(self.widget_2)
        self.seuilfield.setGeometry(QtCore.QRect(100, 300, 191, 41))
        self.seuilfield.setStyleSheet("background-color: rgb(27, 19, 57);\n"
"color: rgb(255, 230, 250);\n"
"\n"
"\n"
"\n"
"border:none;\n"
"border-bottom :2px solid ;\n"
"border-bottom-color: rgb(255, 170, 255);\n"
"padding-bottom:7px;\n"
"\n"
"\n"
"")
        self.seuilfield.setObjectName("seuilfield")
        self.btn_upload = QtWidgets.QPushButton(self.widget_2)
        self.btn_upload.setGeometry(QtCore.QRect(590, 360, 111, 41))
        self.btn_upload.setStyleSheet("QPushButton#btn_upload{\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgb(181, 120, 255), stop:1 rgb(255, 170, 255));\n"
"\n"
"    color:rgba(255, 255, 255, 210);\n"
"\n"
"    border-radius:5px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton#btn_upload:hover{\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgb(181, 120, 255), stop:1 rgb(255, 170, 255));\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton#btn_upload:pressed{\n"
"\n"
"    padding-left:5px;\n"
"\n"
"    padding-top:5px;\n"
"\n"
"    background-color:rgb(251, 130, 255);\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton#btn_upload_2, #btn_upload_3, #btn_upload_4, #btn_upload_5{\n"
"\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"\n"
"    color:rgb(251, 130, 255);\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton#btn_upload_2:hover, #btn_upload_3:hover, #btn_upload_4:hover, #btn_upload_5:hover{\n"
"\n"
"    color: rgb(251, 130, 255);\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton#btn_upload_2:pressed, #btn_upload_3:pressed, #btn_upload_4:pressed, #btn_upload_5:pressed{\n"
"\n"
"    padding-left:5px;\n"
"\n"
"    padding-top:5px;\n"
"\n"
"    color:rgb(251, 130, 255);;\n"
"\n"
"}\n"
"\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ic/icons8-télécharger-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_upload.setIcon(icon1)
        self.btn_upload.setIconSize(QtCore.QSize(50, 50))
        self.btn_upload.setObjectName("btn_upload")
        self.picture = QtWidgets.QLabel(self.widget_2)
        self.picture.setGeometry(QtCore.QRect(330, 230, 211, 181))
        self.picture.setText("")
        self.picture.setPixmap(QtGui.QPixmap("placeholder.jpg"))
        self.picture.setIndent(-5)
        self.picture.setObjectName("picture")
        self.descfield = QtWidgets.QLineEdit(self.widget_2)
        self.descfield.setGeometry(QtCore.QRect(100, 160, 191, 41))
        self.descfield.setStyleSheet("background-color: rgb(27, 19, 57);\n"
"color: rgb(255, 230, 250);\n"
"\n"
"\n"
"\n"
"border:none;\n"
"border-bottom :2px solid ;\n"
"border-bottom-color: rgb(255, 170, 255);\n"
"padding-bottom:7px;\n"
"\n"
"\n"
"\n"
"")
        self.descfield.setText("")
        self.descfield.setCursorPosition(0)
        self.descfield.setObjectName("descfield")
        self.prixfield = QtWidgets.QLineEdit(self.widget_2)
        self.prixfield.setGeometry(QtCore.QRect(100, 230, 191, 41))
        self.prixfield.setStyleSheet("background-color: rgb(27, 19, 57);\n"
"color: rgb(255, 230, 250);\n"
"\n"
"\n"
"\n"
"border:none;\n"
"border-bottom :2px solid ;\n"
"border-bottom-color: rgb(255, 170, 255);\n"
"padding-bottom:7px;\n"
"\n"
"\n"
"")
        self.prixfield.setText("")
        self.prixfield.setCursorPosition(0)
        self.prixfield.setObjectName("prixfield")
        self.error5 = QtWidgets.QLabel(self.widget_2)
        self.error5.setGeometry(QtCore.QRect(40, 430, 301, 16))
        self.error5.setStyleSheet("color: rgb(170, 0, 0);")
        self.error5.setText("")
        self.error5.setObjectName("error5")
        self.error4 = QtWidgets.QLabel(self.widget_2)
        self.error4.setGeometry(QtCore.QRect(40, 350, 301, 16))
        self.error4.setStyleSheet("color: rgb(170, 0, 0);")
        self.error4.setText("")
        self.error4.setObjectName("error4")
        self.error3 = QtWidgets.QLabel(self.widget_2)
        self.error3.setGeometry(QtCore.QRect(40, 280, 301, 16))
        self.error3.setStyleSheet("color: rgb(170, 0, 0);")
        self.error3.setText("")
        self.error3.setObjectName("error3")
        self.error2 = QtWidgets.QLabel(self.widget_2)
        self.error2.setGeometry(QtCore.QRect(40, 210, 301, 16))
        self.error2.setStyleSheet("color: rgb(170, 0, 0);")
        self.error2.setText("")
        self.error2.setObjectName("error2")
        self.error1 = QtWidgets.QLabel(self.widget_2)
        self.error1.setGeometry(QtCore.QRect(40, 140, 301, 16))
        self.error1.setStyleSheet("color: rgb(170, 0, 0);")
        self.error1.setText("")
        self.error1.setObjectName("error1")
        self.error = QtWidgets.QLabel(self.widget_2)
        self.error.setGeometry(QtCore.QRect(240, 490, 341, 16))
        self.error.setStyleSheet("color: rgb(170, 0, 0);")
        self.error.setText("")
        self.error.setObjectName("error")
        self.quantitefield = QtWidgets.QLineEdit(self.widget_2)
        self.quantitefield.setGeometry(QtCore.QRect(100, 380, 191, 41))
        self.quantitefield.setStyleSheet("background-color: rgb(27, 19, 57);\n"
"color: rgb(255, 230, 250);\n"
"\n"
"\n"
"\n"
"border:none;\n"
"border-bottom :2px solid ;\n"
"border-bottom-color: rgb(255, 170, 255);\n"
"padding-bottom:7px;\n"
"\n"
"\n"
"")
        self.quantitefield.setText("")
        self.quantitefield.setCursorPosition(0)
        self.quantitefield.setObjectName("quantitefield")
        self.date_derniere_entree = QtWidgets.QDateEdit(self.widget_2)
        self.date_derniere_entree.setGeometry(QtCore.QRect(380, 110, 231, 22))
        self.date_derniere_entree.setStyleSheet("color: rgb(255, 255, 255);")
        self.date_derniere_entree.setObjectName("date_derniere_entree")
        self.date_derniere_entree_2 = QtWidgets.QDateEdit(self.widget_2)
        self.date_derniere_entree_2.setGeometry(QtCore.QRect(380, 180, 201, 22))
        self.date_derniere_entree_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.date_derniere_entree_2.setObjectName("date_derniere_entree_2")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(380, 80, 141, 16))
        self.label.setStyleSheet("color: rgb(243, 70, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(380, 150, 121, 16))
        self.label_2.setStyleSheet("color: rgb(243, 70, 255);")
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.widget_2)
        self.comboBox.setGeometry(QtCore.QRect(380, 440, 251, 31))
        self.comboBox.setStyleSheet("background-color: rgb(27, 19, 57);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"\n"
"border:none;\n"
"border-bottom :2px solid ;\n"
"border-top :2px solid ;\n"
"border-left :2px solid ;\n"
"border-right :2px solid ;\n"
"border-bottom-color: rgb(255, 170, 255);\n"
"border-top-color: rgb(255, 170, 255);\n"
"border-right-color: rgb(255, 170, 255);\n"
"border-left-color: rgb(255, 170, 255);\n"
"padding-bottom:7px;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 90, 75, 41))
        self.pushButton_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ic/icons8-badge-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 160, 75, 41))
        self.pushButton_3.setText("")
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 230, 75, 41))
        self.pushButton_4.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("ic/icons8-étiquette-de-prix-usd-40.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 300, 75, 41))
        self.pushButton_5.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("ic/icons8-produit-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 390, 75, 41))
        self.pushButton_6.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("ic/icons8-vendre-les-stock-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon5)
        self.pushButton_6.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_7.setGeometry(QtCore.QRect(324, 90, 51, 41))
        self.pushButton_7.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("ic/icons8-calendrier-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon6)
        self.pushButton_7.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_8.setGeometry(QtCore.QRect(324, 160, 51, 41))
        self.pushButton_8.setText("")
        self.pushButton_8.setIcon(icon6)
        self.pushButton_8.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(590, 270, 121, 51))
        self.label_3.setStyleSheet("color:rgb(255, 255, 0);")
        self.label_3.setObjectName("label_3")
        self.error_2 = QtWidgets.QLabel(self.widget_2)
        self.error_2.setGeometry(QtCore.QRect(380, 420, 341, 16))
        self.error_2.setStyleSheet("color: rgb(170, 0, 0);")
        self.error_2.setText("")
        self.error_2.setObjectName("error_2")
        self.pushButton_9 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_9.setGeometry(QtCore.QRect(730, 20, 75, 61))
        self.pushButton_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_9.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("ic/icons8-sortie-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon7)
        self.pushButton_9.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_10.setGeometry(QtCore.QRect(660, 0, 75, 61))
        self.pushButton_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_10.setText("")
        self.pushButton_10.setIcon(icon7)
        self.pushButton_10.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_10.setObjectName("pushButton_10")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_6.setText(_translate("Form", "ADD PRODUCT"))
        self.namefield.setPlaceholderText(_translate("Form", "Name"))
        self.btn_add1.setText(_translate("Form", "ADD"))
        self.seuilfield.setPlaceholderText(_translate("Form", "seuil alerte de stock"))
        self.btn_upload.setText(_translate("Form", "Upload"))
        self.descfield.setPlaceholderText(_translate("Form", "Description"))
        self.prixfield.setPlaceholderText(_translate("Form", "Prix Unitaire"))
        self.quantitefield.setPlaceholderText(_translate("Form", "quantite"))
        self.label.setText(_translate("Form", "Date derniere Entrée"))
        self.label_2.setText(_translate("Form", "Date derniere sortie"))
        self.comboBox.setItemText(0, _translate("Form", "ORDINATEURS"))
        self.comboBox.setItemText(1, _translate("Form", "ORDINATEUR FIXE & ECRANS"))
        self.comboBox.setItemText(2, _translate("Form", "ACCESSOIRES"))
        self.comboBox.setItemText(3, _translate("Form", "COMPOSANTS PC"))
        self.comboBox.setItemText(4, _translate("Form", "STOCKAGE"))
        self.label_3.setText(_translate("Form", "SALMA"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
