import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QGridLayout, QMessageBox
from PyQt5.QtCore import QTimer

class WhackAMoleGame(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.score = 0
        self.time_left = 30
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)  # Update every second

        self.mole_buttons = []
        self.setup_grid()
        self.show_mole()

    def initUI(self):
        self.setWindowTitle('Whack-a-Mole Game')
        self.setGeometry(100, 100, 400, 400)
        
        self.layout = QVBoxLayout()
        self.score_label = QLabel('Score: 0')
        self.timer_label = QLabel('Time left: 30')
        
        self.layout.addWidget(self.score_label)
        self.layout.addWidget(self.timer_label)
        
        self.grid_layout = QGridLayout()
        self.layout.addLayout(self.grid_layout)
        
        self.setLayout(self.layout)

    def setup_grid(self):
        for i in range(3):
            row = []
            for j in range(3):
                button = QPushButton(' ')
                button.setFixedSize(100, 100)
                button.clicked.connect(self.whack_mole)
                self.grid_layout.addWidget(button, i, j)
                row.append(button)
            self.mole_buttons.append(row)

    def show_mole(self):
        # Hide all moles first
        for row in self.mole_buttons:
            for button in row:
                button.setText(' ')
        
        # Randomly select a button to be the mole
        i, j = random.randint(0, 2), random.randint(0, 2)
        self.mole_buttons[i][j].setText('Mole')
        
        # Schedule next mole appearance
        QTimer.singleShot(1000, self.show_mole)  # Mole appears every second

    def whack_mole(self):
        sender = self.sender()
        if sender.text() == 'Mole':
            self.score += 1
            self.score_label.setText(f'Score: {self.score}')
            sender.setText(' ')
    
    def update_timer(self):
        self.time_left -= 1
        self.timer_label.setText(f'Time left: {self.time_left}')
        if self.time_left <= 0:
            self.end_game()

    def end_game(self):
        self.timer.stop()
        QMessageBox.information(self, 'Game Over', f'Your final score is: {self.score}')
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = WhackAMoleGame()
    game.show()
    sys.exit(app.exec_())