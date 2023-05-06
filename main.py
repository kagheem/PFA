import sys
import re
from typing import Self
from PyQt5.uic import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sqlite3
from PyQt5.QtWidgets import (QApplication, QWidget, QFileDialog, QTextEdit, QPushButton, QLabel, QVBoxLayout, QMessageBox)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QDir
import platform
from PyQt5 import QtCore, QtGui,  QtWidgets
from PyQt5.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient,QPen)
from PyQt5.QtWidgets import *
from MainWindow import Ui_SplashScreen
from Login_page import Ui_Form
from PyQt5.QtCore import QByteArray
from PyQt5.QtChart import QChart, QChartView , QPieSeries
from PyQt5.QtChart import QPieSeries
from PyQt5.QtChart import QPieSlice
import hashlib
from MainWindow import  Ui_SplashScreen
from PyQt5.QtWidgets import QMainWindow



class charts(QDialog):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        super(charts,self).__init__()
        loadUi("Charts.ui",self)
        self.pushButton.clicked.connect(self.home)
        
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        self.setWindowIcon(QIcon("c.png"))
        self.setStyleSheet('background-color:rgb(27, 19, 57)')
        series = QPieSeries()
        slices = []
        slices.append(QPieSlice("ORDINATEURS", cursor.execute("SELECT count(*) FROM products WHERE name_cat ='ORDINATEURS'").fetchone()[0]))
        slices.append(QPieSlice("ORDINATEUR FIXE & ECRANS", cursor.execute("SELECT count(*) FROM products WHERE name_cat ='ORDINATEUR FIXE & ECRANS'").fetchone()[0]))
        slices.append(QPieSlice("ACCESSOIRES", cursor.execute("SELECT count(*) FROM products WHERE name_cat ='ACCESSOIRES'").fetchone()[0]))
        slices.append(QPieSlice("COMPOSANTS PC", cursor.execute("SELECT count(*) FROM products WHERE name_cat ='COMPOSANTS PC'").fetchone()[0]))
        slices.append(QPieSlice("STOCKAGE", cursor.execute("SELECT count(*) FROM products WHERE name_cat ='STOCKAGE'").fetchone()[0]))
        series.append(slices)

        chart=QChart()
        chart.addSeries(series)
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Catégories")
        chartview=QChartView(chart)
        vbox=QVBoxLayout()
        vbox.addWidget(chartview)
        self.setLayout(vbox)
        #slice
        my_slice=series.slices()[0]
        my_slice.setExploded(True)
        my_slice.setLabelVisible(True)
        my_slice.setPen(QPen(Qt.green,4))
        my_slice.setBrush(Qt.green)
    def home(self):
        home=Accueil()
        widget.addWidget(home)
        widget.setCurrentIndex(widget.currentIndex()+1)
class upload(QDialog):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        super(upload,self).__init__()
        loadUi("upload.ui",self)
        self.btn_add1.clicked.connect(self.modifier)
        self.btn_refresh.clicked.connect(self.getdata)
        self.pushButton_7.clicked.connect(self.home)
    def home(self):
        home=Accueil()
        widget.addWidget(home)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def getdata(self):
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        '''
        sqlquery = "SELECT * FROM products LIMIT 50"
        
        result=cur.execute(sqlquery)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str(data)))'''
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()
        self.tableWidget.setRowCount(len(products))
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Name", "Description", "Price", "Quantity", "Alert Stock", "Last Entry Date", "Last Exit Date", "Image", "Category"])

        for row, product in enumerate(products):
            for col, value in enumerate(product):
                if col == 8:  # column for the image
                    image_path = image_path = value.encode('utf-8').decode('utf-8') # Convert the bytes to a string
                    pixmap = QPixmap(image_path)
                    label = QLabel()
                    label.setPixmap(pixmap.scaled(100, 100, QtCore.Qt.KeepAspectRatio))  # you can adjust the size as needed
                    self.tableWidget.setCellWidget(row, col, label)
                else:
                    cell = QTableWidgetItem(str(value))
                    self.tableWidget.setItem(row, col, cell)

        cursor.close()   
    def modifier(self):
        def check_id_exists(id):
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()
        
            cursor.execute("SELECT id_produit FROM products WHERE id_produit = ?", (id,))
            row = cursor.fetchone()
            cursor.close()
        
            return row is not None

    # Get the values from the GUI controls
        id = self.idfield.text()
        description = self.descfield.text()
        prix = self.prixfield.text()
        seuil = self.seuilfield.text()
        quantite = self.quantitefield.text()
    
        if not check_id_exists(id):
            QMessageBox.warning(self, "Confirmation", "Produit n'existe pas ")
        elif len(id)==0 or len(description)==0 or len(prix)==0 or len(seuil)==0 or len(quantite)==0:
            self.error1.setText("Veuillez remplir le champ nom !! ")
            self.error2.setText("Veuillez remplir le champ description !! ")
            self.error3.setText("Veuillez remplir le champ prix !! ")
            self.error4.setText("Veuillez remplir le champ seuil !! ")
            self.error5.setText("Veuillez remplir le champ quantite !! ")
            self.error.setText("Veuillez remplir le champ ID !! ")
        else:
            # Open a connection to the database
            conn = sqlite3.connect("database.db")
            c = conn.cursor()
            # Execute the UPDATE query
            c.execute("UPDATE products SET description = ?, prix_unitaire = ?, seuil_allerte_stock = ?, quantite = ? WHERE id_produit = ?", (description, prix, seuil, quantite, id))
            # Commit the changes and close the connection
            conn.commit()
            conn.close()
            self.error1.setText("")
            self.error2.setText("")
            self.error3.setText("")
            self.error4.setText("")
            self.error5.setText("")
            self.error.setText("")
            QMessageBox.information(self, "Confirmation", "Informations mises à jour avec succès")

class Add(QDialog):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        super(Add,self).__init__()
        loadUi("add.ui",self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.btn_add1.clicked.connect(self.ajouter)
        self.btn_upload.clicked.connect(self.getpicture)
        self.pushButton_10.clicked.connect(self.home)
    def home(self):
        home=Accueil()
        widget.addWidget(home)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def getpicture(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open Image File', r"<Default dir>", "Image files (*.jpg *.jpeg *.gif)")
        '''print(file_name(0))'''
        self.picture.setPixmap(QPixmap(file_name).scaledToWidth(200))
        self.label_3.setText(file_name,) 
        with open(file_name, 'rb') as file:
            blob_data = file.read()
        sqlite3.Binary(blob_data)
    def ajouter(self):
        name = self.namefield.text()
        description = self.descfield.text()
        prix = self.prixfield.text()
        seuil= self.seuilfield.text()
        quantite = self.quantitefield.text()
        date1 = self.date_derniere_entree.text()  
        date2 = self.date_derniere_entree_2.text()
        cmb=self.comboBox.currentText()
        picture = self.label_3.text()
        if len(name)==0 or len(description)==0 or len(prix)==0 or len(seuil)==0 or len (quantite)==0 or len(date1)==0 or len(date2)==0 or len(picture)==0:
                self.error1.setText("please fill in the name's field !! ")
                self.error2.setText("please fill in the description's field !! ")
                self.error3.setText("please fill in the prix's field !! ")
                self.error4.setText("please fill in the seuil's field !! ")
                self.error5.setText("please fill in the quantite's field !! ")
                self.error_2.setText("please fill in picture 's field !! ")
         

        else:
            
            conn = sqlite3.connect("database.db")
            cur = conn.cursor()
            user_info = [name,description, prix, seuil,quantite,date1,date2,picture,cmb]
            query = 'INSERT INTO products Values(null,?,?,?,?,?,?,?,?,?)'
            cur.execute(query, user_info)
            self.error1.setText("")
            self.error2.setText("")
            self.error3.setText("")
            self.error4.setText("")
            self.error5.setText("")
           
            self.error_2.setText("")
            self.error.setText("successfully added")
            conn.commit()
            conn.close()
            self.error.setText("")
            window=Accueil()
            widget.addWidget(window)
            widget.setCurrentIndex(widget.currentIndex()+1)
            window.setWindowTitle('Login')
            window.setWindowIcon(QIcon('ic.png'))
            RES= QMessageBox.information(window,'Message','Product added successfully',QMessageBox.Yes)

       
class Accueil(QDialog):
    def __init__(self):
        super(Accueil,self).__init__()
        loadUi("Accueil.ui",self)
        
        self.btn_refresh.clicked.connect(self.getdata)
        self.deleteEmpButton.clicked.connect(self.delete)
        self.searchButton.clicked.connect(self.search)
        self.addEmpButton.clicked.connect(self.addproduit)
        self.updateEmpButton.clicked.connect(self.updateproduit)
        self.nbrr.clicked.connect(self.charts)
        self.pushButton.clicked.connect(self.home)
    def home(self):
        home=Login()
        widget.addWidget(home)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def charts(self):
        chart=charts()
        widget.addWidget(chart)
        widget.setCurrentIndex(widget.currentIndex()+1)   
    def getdata(self):
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        '''
        sqlquery = "SELECT * FROM products LIMIT 50"
        
        result=cur.execute(sqlquery)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str(data)))'''
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()
        self.tableWidget.setRowCount(len(products))
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Name", "Description", "Price", "Quantity", "Alert Stock", "Last Entry Date", "Last Exit Date", "Image", "Category"])

        for row, product in enumerate(products):
            for col, value in enumerate(product):
                if col == 8:  # column for the image
                    image_path = image_path = value.encode('utf-8').decode('utf-8') # Convert the bytes to a string
                    pixmap = QPixmap(image_path)
                    label = QLabel()
                    label.setPixmap(pixmap.scaled(100, 100, QtCore.Qt.KeepAspectRatio))  # you can adjust the size as needed
                    self.tableWidget.setCellWidget(row, col, label)
                else:
                    cell = QTableWidgetItem(str(value))
                    self.tableWidget.setItem(row, col, cell)

        cursor.close()

    def delete(self):
        
        id = self.deletefield.text()
        if id:
            
            connection = sqlite3.connect('database.db')
            cursor = connection.cursor()
            delete_query = 'DELETE FROM products WHERE id_produit = ?'
            cursor.execute(delete_query, (id,))
            connection.commit()
            connection.close()
            '''self.showAllProducts()'''
            self.deletefield.setText("")
            QMessageBox.information(self, "Success", "PRODUCT deleted successfully.")
        
        else:
            
            QMessageBox.warning(self, "Error", "Please select a product to delete to delete.")
    


        
    def search(self):
        # Get search term and search option from GUI
        search_term = self.searchfield.text()
        search_option = self.comboBox.currentText()
        
        # Connect to SQLite database
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        
        # Execute SELECT statement based on search option
        if search_option == 'Nom':
            c.execute('SELECT * FROM products WHERE name LIKE ?', ('%' + search_term + '%',))
        elif search_option == 'Prix unitaire':
            c.execute('SELECT * FROM products WHERE prix_unitaire LIKE ?', ('%' + search_term + '%',))
        elif search_option == 'Quantité':
            c.execute('SELECT * FROM products WHERE quantite LIKE ?', ('%' + search_term + '%',))
        elif search_option == 'Date de dernière entrée en stock':
            # Convert search term to datetime object
            
            c.execute('SELECT * FROM products WHERE date_derniere_entree LIKE ?', ('%' + search_term + '%',))
        
        # Get search results and display in table widget
        rows = c.fetchall()
        self.tableWidget.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.tableWidget.setItem(i, j, item)
        
        # Close database connection
        conn.close()
    def addproduit(self):   
        createproduit=Add()
        widget.addWidget(createproduit)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def updateproduit(self):   
        upproduit=upload()
        widget.addWidget(upproduit)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
        
## GLOBAL
counter = 0
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

#class login 
class Login(QDialog):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        super(Login,self).__init__()
        loadUi("Login_page.ui",self)
        
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.createacc_btn.clicked.connect(self.gotocreateacc)
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_btn.clicked.connect(self.loginfunction)
        self.quitter.clicked.connect(app.quit)
        
    def gotocreateacc(QDialog):
        createacc=Signup()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def loginfunction(self):
        user = self.usernamefield.text()
        password = self.passwordfield.text()
        username_hashed = hashlib.sha256(user.encode()).hexdigest()
        password_hashed = hashlib.sha256(password.encode()).hexdigest()
        if len(username_hashed)==0 or len(password_hashed)==0:
            self.error.setText("please fill in ALL the fields !! ")
        else:
            conn = sqlite3.connect("database.db")
            cur = conn.cursor()
            query = 'SELECT password FROM users WHERE login =\''+username_hashed+"\'"
            cur.execute(query)
            result_pass = cur.fetchone()
        if result_pass is not None and result_pass[0] == password_hashed : 
            print("Successfully logged in .")
            self.error.setText("")
            window=Accueil()
            widget.addWidget(window)
            widget.setCurrentIndex(widget.currentIndex()+1)
            window.setWindowTitle('Login')
            window.setWindowIcon(QIcon('ic.png'))
            RES= QMessageBox.information(window,'Message','Login successfully',QMessageBox.Yes)
        else:
            self.error.setText("Invalid username or password.")
            QMessageBox.warning(self, "Error", "Invalid username or password.")

## FORM SPLASH
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        '''self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)'''
        ## REMOVE TITLE BAR
        '''self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)'''

        ## CREATE DROP SHADOWN EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0,0,0,60))
        ## SET DROP SHADOWN EFFECT IN FRAME
        self.ui.dropShowdan.setGraphicsEffect(self.shadow)
        
        # QTIMER START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(1)


        # CHANGE DESCRIPTION / labelSubName
        QtCore.QTimer.singleShot(1000, lambda: self.ui.labelSubName.setText("<strong>LOADING</strong><font style=\"color:white\">LOGIN</font>"))
        QtCore.QTimer.singleShot(1500, lambda: self.ui.labelSubName.setText("<strong>LOADING</strong><font style=\"color:white\">SIGNUP</font>"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.labelSubName.setText("<strong>LOADING</strong><font style=\"color:white\">HOME</font>"))

        ## SHOW MAIN WINDOWS
        self.show()
    def progress(self):
        global counter

        #SET VALUE TO PROGRESS
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREEM AND OPEN THING
        if counter > 100:
            self.timer.stop()
            ## CREATE FORM CENTRAL
            self.main = Login()
            ## SET DROP SHADOWN EFFECT IN FRAME
            '''self.main.ui.frame.setGraphicsEffect(self.shadow)'''
            ## SHOW MAIN WINDOWS / FORM CENTRAL
            self.main.show()
            self.close()
        counter+=1


class Signup(QDialog):
    def __init__(self):
        super(Signup,self).__init__()
        loadUi("SignUp_page.ui",self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.C_passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.btn_signup.clicked.connect(self.signupfunction)
        self.pushButton_9.clicked.connect(self.home)
        
    def home(self):
        home=Login()
        widget.addWidget(home)
        widget.setCurrentIndex(widget.currentIndex()+1)
    

    def signupfunction(self):
        
        
        user = self.usernamefield.text()
        firstname = self.first_namefield.text()
        lastname = self.last_namefield.text()
        email = self.emailfield.text()
        password = self.passwordfield.text()
        cpassword = self.C_passwordfield.text()  
        telephone = self.telephonefield.text()
        username_hashed = hashlib.sha256(user.encode()).hexdigest()
        password_hashed = hashlib.sha256(password.encode()).hexdigest()
        cpassword_hashed = hashlib.sha256(cpassword.encode()).hexdigest()
        # Function to validate email
        def validate_email(email):
            pattern = r'^[\w-]+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$'
            if re.match(pattern, email):
                return True
            else:
                return False

# Function to validate telephone number
        def validate_phone(telephone):
            pattern = r'^\d{10}$'
            if re.match(pattern, telephone):
                return True
            else:
                return False   
        if len(username_hashed)==0 or len(firstname)==0 or len(lastname)==0 or len(email)==0 or len (password_hashed)==0 or len(cpassword_hashed)==0 or len(telephone)==0 :
                self.error1.setText("please fill in the username's field !! ")
                self.error2.setText("please fill in the firstname's field !! ")
                self.error3.setText("please fill in the lastname's field !! ")
                self.error4.setText("please fill in the email's field !! ")
                self.error5.setText("please fill in the password's field !! ")
                self.error6.setText("please fill in the confirm password's field !! ")
                self.error7.setText("please fill in the telephone's field !! ")
        elif password_hashed != cpassword_hashed:
            self.error.setText("password and confirm password did not match !!!")
            
        elif validate_email(email)==False:
            
            
            self.error4.setText(" ")

            self.error41.setText("the mail should be exemple@exemple.com")
         

        elif validate_phone(telephone)==False:
            self.error7.setText(" ")
            self.error71.setText("Please enter a valid 10-digit phone number")

        else:
            
            conn = sqlite3.connect("database.db")
            cur = conn.cursor()
            user_info = [ username_hashed, email ,password_hashed, cpassword_hashed,firstname,lastname, telephone]
            query = 'INSERT INTO users Values(null,?,?,?,?,?,?,?)'
            cur.execute(query, user_info)
            self.error1.setText("")
            self.error2.setText("")
            self.error3.setText("")
            self.error4.setText("")
            self.error5.setText("")
            self.error6.setText("")
            self.error7.setText("")
            self.error.setText("successfully signed up")
            conn.commit()
            conn.close()
            self.error.setText("")
            
            login=Login()
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex()+1)
            login.setWindowTitle('Login')
            login.setWindowIcon(QIcon('ic.png'))
            RES= QMessageBox.information(login,'Message','Successfully Signed Up',QMessageBox.Yes)
            
    

         
app =QApplication(sys.argv)
welcome=SplashScreen()
widget = QtWidgets.QStackedWidget()

widget.addWidget(welcome)
widget.setFixedHeight(600)
widget.setFixedWidth(800)
widget.show()


try:
    sys.exit(app.exec_())
except:
    print("Exiting")