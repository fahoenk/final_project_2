from operator import methodcaller

from PyQt6.QtWidgets import *
from dialog_window import *
from gui import *


#Code for egcd and modinv from https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
def egcd(a: int, b: int) -> tuple[int,int,int]:
    """
    Method to find the greatest common divisor of two integers
    :param a: First integer
    :param b: Second integer
    :return: Greatest common divisor (g) and corresponding Euclidean algorithm values
    """
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a: int, m: int) -> int:
    """
    Method to find the inverse of a modulo m
    :param a: integer
    :param m: modulus
    :return: inverse of a modulo m
    """
    g, x, y = egcd(a, m)
    if g != 1:
        raise TypeError
    else:
        return x % m

class Logic(QMainWindow, Ui_MainWindow):
    """
    Class containing the application's logic.
    """

    def __init__(self):
        """
        Initializing method
        """
        super().__init__()
        self.setupUi(self)

        self.button_calculate.clicked.connect(lambda: self.calculate())
        self.button_help.clicked.connect(lambda: self.help())

    def calculate(self):
        """
        Method that finds modular inverse when button_calculate is clicked, and handles exceptions.
        """
        try:
            if self.input_modulo.text().strip() == "" or self.input_integer.text().strip() =="":
                raise ZeroDivisionError

            mod = int(self.input_modulo.text())
            integer = int(self.input_integer.text())
            input_int = integer

            if mod < 0:
                raise KeyError

            if integer < 0:
                while integer < 0:
                    integer += mod

            if integer % mod == 1:
                inverse = 1
            elif (integer % mod) - mod == -1:
                inverse = integer % mod
            else:
                inverse = modinv(integer, mod)

            self.label_answer.setText(f"The inverse of {input_int} mod {mod} is {inverse}")

        except ValueError:
            self.label_answer.setStyleSheet("background-color: red")
            self.label_answer.setText("Please input integer values")

        except TypeError:
            self.label_answer.setStyleSheet("background-color: red")
            self.label_answer.setText(f"{int(self.input_integer.text().strip())} does not have an inverse modulo {int(self.input_modulo.text().strip())}")

        except KeyError:
            self.label_answer.setStyleSheet("background-color: red")
            self.label_answer.setText("Please provide a positive modulus")

        except ZeroDivisionError:
            self.label_answer.setStyleSheet("background-color: red")
            self.label_answer.setText("Please fill out both fields with non-zero integer values")

        else:
            self.input_integer.clear()
            self.input_modulo.clear()
            self.label_answer.setStyleSheet("background-color: default_palette.window().color()")

    def help(self) -> None:
        """
        Method to open dialog window when button_help is clicked.
        """
        dialog = QDialog(self)  # Create an instance of the dialog
        ui2 = Ui_Dialog()  # Create an instance of the UI class
        ui2.setupUi(dialog) # Set up the UI on the dialog
        dialog.show()