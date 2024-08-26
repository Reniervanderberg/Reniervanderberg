import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget, QMessageBox
from PyQt5.QtCore import QTimer

class WhackAMoleGame(QMainWindow):
    def __init__(self):
        super().__init__()

        # Game settings
        self.grid_size = 4
        self.mole_timer_interval = 1000  # milliseconds
        self.mole_position = None

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Whack-a-Mole')
        self.setGeometry(100, 100, 400, 400)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        
        self.grid_layout = QGridLayout(self.central_widget)
        self.buttons = []

        for i in range(self.grid_size):
            row_buttons = []
            for j in range(self.grid_size):
                button = QPushButton(self)
                button.setFixedSize(80, 80)
                button.setStyleSheet("background-color: lightgray")
                button.clicked.connect(self.buttonClicked)
                self.grid_layout.addWidget(button, i, j)
                row_buttons.append(button)
            self.buttons.append(row_buttons)
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showMole)
        self.timer.start(self.mole_timer_interval)

    def showMole(self):
        if self.mole_position:
            # Hide the previous mole
            row, col = self.mole_position
            self.buttons[row][col].setStyleSheet("background-color: lightgray")
        
        # Choose a new random position for the mole
        self.mole_position = (random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1))
        row, col = self.mole_position
        self.buttons[row][col].setStyleSheet("background-color: red")

    def buttonClicked(self):
        sender = self.sender()
        row, col = None, None
        for r in range(self.grid_size):
            if sender in self.buttons[r]:
                row = r
                col = self.buttons[r].index(sender)
                break

        if self.mole_position == (row, col):
            self.buttons[row][col].setStyleSheet("background-color: lightgray")
            self.mole_position = None
            QMessageBox.information(self, "Whack-a-Mole", "Hit!")
        else:
            QMessageBox.warning(self, "Whack-a-Mole", "Miss!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = WhackAMoleGame()
    game.show()
    sys.exit(app.exec_())