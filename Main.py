import sys
import random
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont, QColor
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QGraphicsDropShadowEffect
)

class DiceRollerWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Dice Roller Pro")
        self.setFixedSize(360, 640)  # Standard mobile viewport ratio
        
        # Dark Theme Styling
        self.setStyleSheet("""
            QWidget {
                background-color: #121212;
                color: #FFFFFF;
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto;
            }
            QPushButton {
                background-color: #2979FF;
                color: white;
                border-radius: 25px;
                font-size: 20px;
                font-weight: bold;
            }
            QPushButton:pressed {
                background-color: #1565C0;
            }
            QPushButton:disabled {
                background-color: #424242;
                color: #757575;
            }
        """)

        # Main Layout
        layout = QVBoxLayout()
        layout.setContentsMargins(30, 50, 30, 50)
        layout.setSpacing(20)

        # Top Spacer
        layout.addStretch(1)

        # Result Display Label (Massive, crisp numbers)
        self.result_label = QLabel("6", self)
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setFont(QFont("Arial", 110, QFont.Bold))
        layout.addWidget(self.result_label)

        # Instructions / Status Label
        self.info_label = QLabel("Tap below to roll", self)
        self.info_label.setAlignment(Qt.AlignCenter)
        self.info_label.setFont(QFont("Arial", 16))
        self.info_label.setStyleSheet("color: #AAAAAA;")
        layout.addWidget(self.info_label)

        # Bottom Spacer
        layout.addStretch(1)

        # Rounded Pill Button
        self.roll_button = QPushButton("ROLL DICE", self)
        self.roll_button.setFixedHeight(70)
        
        # Add subtle shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(15)
        shadow.setColor(QColor(41, 121, 255, 100))
        shadow.setOffset(0, 5)
        self.roll_button.setGraphicsEffect(shadow)

        self.roll_button.clicked.connect(self.start_roll_animation)
        layout.addWidget(self.roll_button)

        self.setLayout(layout)

        # Animation Timer setup
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_animation)
        self.anim_count = 0

    def start_roll_animation(self):
        self.roll_button.setEnabled(False)
        self.info_label.setText("Rolling...")
        self.anim_count = 0
        self.timer.start(50)  # Ticks every 50ms

    def update_animation(self):
        self.anim_count += 1
        temp_roll = random.randint(1, 6)
        self.result_label.setText(str(temp_roll))

        # Stop after 10 ticks (0.5 seconds)
        if self.anim_count >= 10:
            self.timer.stop()
            final_roll = random.randint(1, 6)
            self.result_label.setText(str(final_roll))
            self.info_label.setText(f"You rolled a {final_roll}!")
            self.roll_button.setEnabled(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DiceRollerWindow()
    window.show()
    sys.exit(app.exec())
      
