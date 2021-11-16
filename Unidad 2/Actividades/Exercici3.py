import argparse

from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication


class MainWindow(QMainWindow):
    def __init__(self, args):
        super().__init__()
        title, text, fixed, size_x, size_y = "La meua aplicació", "Hola", False, 600, 600
        if args.title:
            self.setWindowTitle(args.title)
        if args.button_text:
            text = args.button_text
        if args.fixed_size:
            fixed = args.fixed_size
        if args.size:
            size_x, size_y = args.size
        self.setGeometry(600, 400, size_x, size_y)
        if fixed:
            self.setFixedSize(size_x, size_y)
        self.button = QPushButton(text)
        self.setCentralWidget(self.button)


def main():
    parser = argparse.ArgumentParser(description='Activitat3.py [-h] [-t TITLE] [-b BUTTON_TEXT] [-f] [-s SIZE SIZE]')
    parser.add_argument("-t", "--title", help="Title of application")
    parser.add_argument("-b", "--button-text", help="Button text")
    parser.add_argument("-f", "--fixed-size", help="Window fixed size", action="store_true")
    parser.add_argument("-s", "--size", help="Window's size", nargs=2, type=int)
    args = parser.parse_args()
    app = QApplication()
    window = MainWindow(args)
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
