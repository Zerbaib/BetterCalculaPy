import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QLineEdit, QPushButton
import qdarkstyle
from functools import partial
import math

def on_button_click(text):
    current_text = input_box.text()
    if text == "=":
        try:
            result = eval_expression(current_text)
            input_box.setText(str(result))
        except Exception as e:
            input_box.setText("Erreur")
    elif text == "C":
        input_box.clear()
    else:
        input_box.setText(current_text + text)

def on_enter_pressed():
    on_button_click("=")

def eval_expression(expression):
    safe_dict = {"__builtins__": None, "math": math}
    try:
        return eval(expression, safe_dict)
    except Exception as e:
        raise e

app = QApplication(sys.argv)
app.setStyleSheet(qdarkstyle.load_stylesheet())

window = QWidget()
window.setWindowTitle("Calculator")
window.resize(300, 400)
layout = QVBoxLayout()

input_box = QLineEdit()
input_box.setPlaceholderText("Enter your mathematical expression")
input_box.setStyleSheet("font-size: 18px;")
input_box.returnPressed.connect(on_enter_pressed)
layout.addWidget(input_box)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "(", ")", "C"
]

button_grid_layout = QGridLayout()
button_row, button_column = 0, 0
for button_text in buttons:
    button = QPushButton(button_text)
    button.setStyleSheet("font-size: 20px;")
    button.clicked.connect(partial(on_button_click, button_text))
    button_grid_layout.addWidget(button, button_row, button_column)
    button_column += 1
    if button_column > 3:
        button_column = 0
        button_row += 1

layout.addLayout(button_grid_layout)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())

