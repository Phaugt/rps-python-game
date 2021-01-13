import sys, os
from random import randint
from PyQt5.QtWidgets import (QPushButton, QMainWindow, QApplication, QLabel, QLineEdit, qApp, QHBoxLayout,
                            QVBoxLayout)
from PyQt5 import (uic, QtCore, QtGui)
from PyQt5.QtGui import (QIcon, QImage, QPixmap, QIcon)
from PyQt5.QtCore import (Qt, QFile, QSize)

try:
    from PyQt5.QtWinExtras import QtWin
    myappid = 'pythonexplained.python.rps.game'
    QtWin.setCurrentProcessExplicitAppUserModelID(myappid)    
except ImportError:
    pass
#pyinstaller
def resource_path(relative_path):
    """for pyinstaller"""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath('.'), relative_path)


rps_gui = resource_path("./gui/main.ui")
game_bg = resource_path("./gui/bg.png")
rps_logo = resource_path("./gui/logo.png")
rps_rock = resource_path("./gui/rock.png")
rps_pape = resource_path("./gui/paper.png")
rps_scic = resource_path("./gui/scissors.png")
rps_tie = resource_path("./gui/tie.png")
rps_ques = resource_path("./gui/question.png")


class UI(QMainWindow):
    """main game window"""
    def __init__(self):
        super(UI, self).__init__()
        UIFile = QFile(rps_gui)
        UIFile.open(QFile.ReadOnly)
        uic.loadUi(UIFile, self)
        UIFile.close()
        rps_bg = QPixmap(game_bg)
        self.bg.setPixmap(rps_bg)
        rps_q = QPixmap(rps_ques)
        self.resultImg.setPixmap(rps_q)
        self.resultText.setAlignment(Qt.AlignCenter)


        self.choice1.setIcon(QIcon(rps_rock))
        self.choice1.setIconSize(QSize(128,128))
        self.choice1.setStatusTip("Select Rock!")
        self.choice1.clicked.connect(lambda: self.game("Rock"))

        self.choice2.setIcon(QIcon(rps_pape))
        self.choice2.setIconSize(QSize(128,128))
        self.choice2.setStatusTip("Select Paper!")
        self.choice2.clicked.connect(lambda: self.game("Paper"))

        self.choice3.setIcon(QIcon(rps_scic))
        self.choice3.setIconSize(QSize(128,128))
        self.choice3.setStatusTip("Select Scissors!")
        self.choice3.clicked.connect(lambda: self.game("Scissors"))

        self.resultImg.setStatusTip("Opponents pick!")

    def game(self,choice):
        """rps game """
        g = ["Rock", "Paper", "Scissors"]
        bot = g[randint(0,2)]

        Rock = QPixmap(rps_rock)
        Paper = QPixmap(rps_pape)
        Scissors = QPixmap(rps_scic)
        Tie = QPixmap(rps_tie)

        try:
            if choice == bot:
                self.resultImg.setPixmap(Tie)
                self.resultText.clear()
            elif choice == "Rock":
                if bot == "Paper":
                    self.resultImg.setPixmap(Paper)
                    self.resultText.clear()
                    self.resultText.setText("You lose! " + bot +" covers " + choice)
                else:
                    self.resultImg.setPixmap(Scissors)
                    self.resultText.clear()
                    self.resultText.setText("You win! " +  choice +  " smashes " +  bot)
            elif choice == "Paper":
                if bot == "Scissors":
                    self.resultImg.setPixmap(Scissors)
                    self.resultText.clear()
                    self.resultText.setText("You lose! " +  bot +  " cut " +  choice)
                else:
                    self.resultImg.setPixmap(Rock)
                    self.resultText.clear()
                    self.resultText.setText("You win! " +  choice +  " covers " +  bot)
            elif choice == "Scissors":
                if bot == "Rock":
                    self.resultImg.setPixmap(Rock)
                    self.resultText.clear()
                    self.resultText.setText("You lose... " +  bot +  " smashes " +  choice)
                else:
                    self.resultImg.setPixmap(Paper)
                    self.resultText.clear()
                    self.resultText.setText("You win! " +  choice +  " cut " +  bot)
            else:
                self.resultText.clear()
        except TypeError:
            pass

style = '''
QPushButton {
    background-color: rgba(255,255,255,0);
    border: 0px;
}
QPushButton:hover {
    color: #000000;
    background-color: #222831;
}  
QPushButton:pressed {
    color: #000000;
    background-color: #FED369;
}  
QLabel {
    color: #FED369;
    font-size: 35px;
}
'''


app = QApplication(sys.argv)
app.setWindowIcon(QIcon(rps_logo))
app.setStyleSheet(style)
window = UI()
window.show()
app.exec_()
