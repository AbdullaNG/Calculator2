import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon


# window's class
class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
# window's settings
		self.setGeometry(200, 200, 500, 700)
		self.setFixedSize(500, 700)
		self.setStyleSheet('background-color: #d4d3cb;')
		self.setWindowTitle('Calculator')
		self.setWindowIcon(QIcon('calculator.png'))

# label's settings
		self.label = QLabel(self)
		self.label.setGeometry(5, 10, 490, 100)
		self.label.setStyleSheet('background-color: white;'
									'border-radius: 5px;'
									'border: 2px solid grey;'
									'font-size: 25px;')
		self.label.setAlignment(Qt.AlignBottom | Qt.AlignRight)
		self.data = ''

# buttons
		self.btn_one = QPushButton('1', self)
		self.one()
		self.btn_two = QPushButton('2', self)
		self.two()
		self.btn_three = QPushButton('3', self)
		self.three()
		self.btn_four = QPushButton('4', self)
		self.four()
		self.btn_five = QPushButton('5', self)
		self.five()
		self.btn_six = QPushButton('6', self)
		self.six()
		self.btn_seven = QPushButton('7', self)
		self.seven()
		self.btn_eight = QPushButton('8', self)
		self.eight()
		self.btn_nine = QPushButton('9', self)
		self.nine()
		self.btn_zero = QPushButton('0', self)
		self.zero()
		self.btn_plus = QPushButton('+', self)
		self.plus()
		self.btn_minus = QPushButton('-', self)
		self.minus()
		self.btn_multiplication = QPushButton('*', self)
		self.multiplication()
		self.btn_division = QPushButton('/', self)
		self.division()
		self.btn_equals = QPushButton('=', self)
		self.equals()
		self.btn_dot = QPushButton('.', self)
		self.dot()
		self.btn_clear = QPushButton('Clear', self)
		self.clear()
		self.btn_delete = QPushButton('<=', self)
		self.delete()

# buttons' settings
	def one(self):
		self.btn_one.setGeometry(3, 200, 120, 120)
		self.btn_one.setStyleSheet('background-color: white;'
									'font-size: 50px;'
									'font-weight: bold;')
		self.btn_one.clicked.connect(self.one_on_click)

	def two(self):
		self.btn_two.setGeometry(128, 200, 120, 120)
		self.btn_two.setStyleSheet('background-color: white;'
									'font-size: 50px;'
									'font-weight: bold;')
		self.btn_two.clicked.connect(self.two_on_click)

	def three(self):
		self.btn_three.setGeometry(253, 200, 120, 120)
		self.btn_three.setStyleSheet('background-color: white;'
									'font-size: 50px;'
									'font-weight: bold;')
		self.btn_three.clicked.connect(self.three_on_click)

	def four(self):
		self.btn_four.setGeometry(3, 325, 120, 120)
		self.btn_four.setStyleSheet('background-color: white;'
									'font-size: 50px;'
									'font-weight: bold;')
		self.btn_four.clicked.connect(self.four_on_click)

	def five(self):
		self.btn_five.setGeometry(128, 325, 120, 120)
		self.btn_five.setStyleSheet('background-color: white;'
									'font-size: 50px;'
									'font-weight: bold;')
		self.btn_five.clicked.connect(self.five_on_click)

	def six(self):
		self.btn_six.setGeometry(253, 325, 120, 120)
		self.btn_six.setStyleSheet('background-color: white;'
									'font-size: 50px;'
									'font-weight: bold;')
		self.btn_six.clicked.connect(self.six_on_click)

	def seven(self):
		self.btn_seven.setGeometry(3, 450, 120, 120)
		self.btn_seven.setStyleSheet('background-color: white;'
									'font-size: 50px;'
									'font-weight: bold;')
		self.btn_seven.clicked.connect(self.seven_on_click)

	def eight(self):
		self.btn_eight.setGeometry(128, 450, 120, 120)
		self.btn_eight.setStyleSheet('background-color: white;'
									'font-size: 50px;'
									'font-weight: bold;')
		self.btn_eight.clicked.connect(self.eight_on_click)

	def nine(self):
		self.btn_nine.setGeometry(253, 450, 120, 120)
		self.btn_nine.setStyleSheet('background-color: white;'
									'font-size: 50px;'
									'font-weight: bold;')
		self.btn_nine.clicked.connect(self.nine_on_click)

	def zero(self):
		self.btn_zero.setGeometry(3, 575, 120, 120)
		self.btn_zero.setStyleSheet('background-color: white;'
									'font-size: 50px;'
									'font-weight: bold;')
		self.btn_zero.clicked.connect(self.zero_on_click)

	def plus(self):
		self.btn_plus.setGeometry(378, 200, 120, 120)
		self.btn_plus.setStyleSheet('background-color: #9dc9f2;'
									'font-size: 50px;'
									'font-weight: bold;'
									'color: #292d30;')
		self.btn_plus.clicked.connect(self.plus_on_click)

	def minus(self):
		self.btn_minus.setGeometry(378, 325, 120, 120)
		self.btn_minus.setStyleSheet('background-color: #9dc9f2;'
									'font-size: 50px;'
									'font-weight: bold;'
									'color: #292d30;')
		self.btn_minus.clicked.connect(self.minus_on_click)

	def multiplication(self):
		self.btn_multiplication.setGeometry(378, 450, 120, 120)
		self.btn_multiplication.setStyleSheet('background-color: #9dc9f2;'
									'font-size: 50px;'
									'font-weight: bold;'
									'color: #292d30;')
		self.btn_multiplication.clicked.connect(self.multiplication_on_click)

	def division(self):
		self.btn_division.setGeometry(378, 575, 120, 120)
		self.btn_division.setStyleSheet('background-color: #9dc9f2;'
									'font-size: 50px;'
									'font-weight: bold;'
									'color: #292d30;')
		self.btn_division.clicked.connect(self.division_on_click)

	def equals(self):
		self.btn_equals.setGeometry(253, 575, 120, 120)
		self.btn_equals.setStyleSheet('background-color: #f0cf6c;'
									'font-size: 50px;'
									'font-weight: bold;'
									'color: #292d30;')
		self.btn_equals.clicked.connect(self.equals_on_click)

	def dot(self):
		self.btn_dot.setGeometry(128, 575, 120, 120)
		self.btn_dot.setStyleSheet('background-color: #9dc9f2;'
									'font-size: 50px;'
									'font-weight: bold;'
									'color: #292d30;')
		self.btn_dot.clicked.connect(self.dot_on_click)

	def clear(self):
		self.btn_clear.setGeometry(3, 113, 244, 84)
		self.btn_clear.setStyleSheet('background-color: #f0cf6c;'
										'font-size: 50px;'
										'font-weight: bold;')
		self.btn_clear.clicked.connect(self.clear_on_click)

	def delete(self):
		self.btn_delete.setGeometry(253, 113, 244, 84)
		self.btn_delete.setStyleSheet('background-color: #f0cf6c;'
										'font-size: 50px;'
										'font-weight: bold;')
		self.btn_delete.clicked.connect(self.delete_on_click)

# buttons' logic
	def one_on_click(self):
		self.data += '1'
		self.label.setText(self.data)

	def two_on_click(self):
		self.data += '2'
		self.label.setText(self.data)

	def three_on_click(self):
		self.data += '3'
		self.label.setText(self.data)

	def four_on_click(self):
		self.data += '4'
		self.label.setText(self.data)

	def five_on_click(self):
		self.data += '5'
		self.label.setText(self.data)

	def six_on_click(self):
		self.data += '6'
		self.label.setText(self.data)

	def seven_on_click(self):
		self.data += '7'
		self.label.setText(self.data)

	def eight_on_click(self):
		self.data += '8'
		self.label.setText(self.data)

	def nine_on_click(self):
		self.data += '9'
		self.label.setText(self.data)

	def zero_on_click(self):
		self.data += '0'
		self.label.setText(self.data)

	def plus_on_click(self):
		self.data += '+'
		self.label.setText(self.data)

	def minus_on_click(self):
		self.data += '-'
		self.label.setText(self.data)

	def multiplication_on_click(self):
		self.data += '*'
		self.label.setText(self.data)

	def division_on_click(self):
		self.data += '/'
		self.label.setText(self.data)

	def equals_on_click(self):
		try:
			self.data = str(eval(self.data))
		except ZeroDivisionError:
			self.data = 'Can not divide by zero!'
		except TypeError:
			self.data = 'Wrong input!'
		except SyntaxError:
			self.data = 'Wrong input!'
		except NameError:
			self.data = 'Wrong input!'
		self.label.setText(self.data)

	def dot_on_click(self):
		self.data += '.'
		self.label.setText(self.data)

	def clear_on_click(self):
		self.data = ''
		self.label.setText(self.data)

	def delete_on_click(self):
		self.data = self.data[:-1]
		self.label.setText(self.data)


# main function
def main():
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()