import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

app = QApplication(sys.argv)
window = QWidget()
window.setGeometry(100, 100, 300, 200)  # set the window size and position

label1 = QLabel(window)
label1.setText("Label 1")
label1.move(20, 20)

label2 = QLabel(window)
label2.setText("Label 2")
label2.move(20, 50)

label3 = QLabel(window)
label3.setText("Label 3")
label3.move(20, 80)

window.show()
sys.exit(app.exec_())
