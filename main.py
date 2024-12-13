from logic import *

def main() -> None:
    """
    Shows main window
    """
    application = QApplication([])
    window = Logic() #create instance of Logic class
    window.show()
    application.exec()

if __name__ == "__main__":
    main()