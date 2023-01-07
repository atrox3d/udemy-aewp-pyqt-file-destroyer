from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QComboBox,
    QFileDialog,
)
from PyQt6.QtCore import Qt
from pathlib import Path


def create_files():
    root = Path('files/')
    for i in range(10):
        filepath = root / Path(f'file{i}')
        filepath.write_text('example text')


def open_files():
    global filenames
    filenames, _ = QFileDialog.getOpenFileNames(window,'Select Files')
    message.setText('\n'.join(filenames))


def destroy_files():
    for filename in filenames:
        filepath = Path(filename)
        size = filepath.stat().st_size
        print(f'overwriting {filepath.name} with {size} binary zeroes')
        with open(filepath, 'wb') as f:
            f.write(b'\x00' * size)
        print(f'deleting {filepath.name}')
        filepath.unlink()
        message.setText('Destruction complete.')


create_files()

filenames = []

app = QApplication([])
window = QWidget()
window.setWindowTitle('File Destroyer')
layout = QVBoxLayout()

description_label = """
Select the file(s) you want to destroy.\
The files will be <font color="red">permanently</font> deleted
"""
description = QLabel(description_label)
layout.addWidget(description)

open_button = QPushButton('Open Files')
open_button.setToolTip('Open Files')
open_button.setFixedWidth(100)
layout.addWidget(open_button, alignment=Qt.AlignmentFlag.AlignCenter)
open_button.clicked.connect(open_files)

destroy_button = QPushButton('Destroy Files')
destroy_button.setToolTip('Destroy Files')
destroy_button.setFixedWidth(100)
layout.addWidget(destroy_button, alignment=Qt.AlignmentFlag.AlignCenter)
destroy_button.clicked.connect(destroy_files)

message = QLabel('')
layout.addWidget(message)

window.setLayout(layout)
window.show()
app.exec()

