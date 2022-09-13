# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GetRecord.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QLineEdit, QSizePolicy, QWidget)

class Ui_GetRecord(object):
    def setupUi(self, GetRecord):
        if not GetRecord.objectName():
            GetRecord.setObjectName(u"GetRecord")
        GetRecord.resize(341, 206)
        self.ok_cancel = QDialogButtonBox(GetRecord)
        self.ok_cancel.setObjectName(u"ok_cancel")
        self.ok_cancel.setGeometry(QRect(140, 160, 171, 32))
        self.ok_cancel.setOrientation(Qt.Horizontal)
        self.ok_cancel.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.nome = QLineEdit(GetRecord)
        self.nome.setObjectName(u"nome")
        self.nome.setGeometry(QRect(90, 17, 221, 21))
        self.label_nome = QLabel(GetRecord)
        self.label_nome.setObjectName(u"label_nome")
        self.label_nome.setGeometry(QRect(46, 17, 36, 16))
        self.label_nome.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_cognome = QLabel(GetRecord)
        self.label_cognome.setObjectName(u"label_cognome")
        self.label_cognome.setGeometry(QRect(24, 48, 58, 16))
        self.label_cognome.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.cognome = QLineEdit(GetRecord)
        self.cognome.setObjectName(u"cognome")
        self.cognome.setGeometry(QRect(90, 48, 221, 21))
        self.label_telefono = QLabel(GetRecord)
        self.label_telefono.setObjectName(u"label_telefono")
        self.label_telefono.setGeometry(QRect(30, 79, 52, 16))
        self.label_telefono.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.telefono = QLineEdit(GetRecord)
        self.telefono.setObjectName(u"telefono")
        self.telefono.setGeometry(QRect(90, 79, 221, 21))
        self.label_email = QLabel(GetRecord)
        self.label_email.setObjectName(u"label_email")
        self.label_email.setGeometry(QRect(50, 110, 32, 16))
        self.label_email.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.email = QLineEdit(GetRecord)
        self.email.setObjectName(u"email")
        self.email.setGeometry(QRect(90, 110, 221, 21))

        self.retranslateUi(GetRecord)
        self.ok_cancel.accepted.connect(GetRecord.accept)
        self.ok_cancel.rejected.connect(GetRecord.reject)

        QMetaObject.connectSlotsByName(GetRecord)
    # setupUi

    def retranslateUi(self, GetRecord):
        GetRecord.setWindowTitle(QCoreApplication.translate("GetRecord", u"Dialog", None))
        self.label_nome.setText(QCoreApplication.translate("GetRecord", u"Nome", None))
        self.label_cognome.setText(QCoreApplication.translate("GetRecord", u"Cognome", None))
        self.label_telefono.setText(QCoreApplication.translate("GetRecord", u"Telefono", None))
        self.label_email.setText(QCoreApplication.translate("GetRecord", u"Email", None))
    # retranslateUi

