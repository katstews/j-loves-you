class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 250)
        self.setWindowTitle("Weather app")

        layout = QVBoxLayout() 
        self.setLayout(layout)

        layout.addWidget(QLabel("Hey!"))
        layout.addWidget(QLabel("How are you?"))
        layout.addWidget(QLabel("I hope youre ok.<br/>"))
        layout.addWidget(QLabel("heres J ripping it"))

        lb1 = QLabel()
        lb1.setPixmap(QPixmap("./j_masics.jpeg"))
        layout.addWidget(lb1)

        self.setLayout(layout)

app = QApplication(sys.argv)

window = Window()
window.show()
sys.exit(app.exec())