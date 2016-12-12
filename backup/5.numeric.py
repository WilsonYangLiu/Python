import string
import math

def mulitplied(a, b):
	''' caculate a*b'''
	return a*b

def score(num):
	''' return rating score A~F '''
	if (num >= 90) & (num <= 100):
		return 'A'
	elif num >= 80:
		return 'B'
	elif num >= 70:
		return 'C'
	elif num >= 60:
		return 'D'
	else:
		return 'F'

def leapYear(year):
	''' Determine a given year is a leap year or not. '''
	if (year % 400 == 0) | ((year % 4 == 0) & (year % 100 != 0)):
		print year, "is a leap year."
		return True
	else:
		print year, "is not a leap year."
		return False

def trans2coin(dollar):
	''' for a given money < 100, transform to coins. 
		Make sure the number of coins as less as you can.
	'''
	money = dollar * 100
	if money >= 100:
		print "money ", money, " large than 100."
		return False
	else:
		a = money //25
		b = (money - a * 25) // 10
		c = (money - a * 25 - b * 10) // 5
		d = (money - a * 25 - b * 10) % 5
		print "%d = %d*(25 Cents) + %d*(10 Cents) + %d*(5 Cents) + %d*(1 Cents)." % (money, a, b, c, d)
		#print money, "=", a, "*25 Cents +", b, "*10 Cents +", c, "*5 Cents +", d, "*1 Cents." 
		return True

def myEval(expr):
	''' split the expr into 3 field: Operand, Operator, Operand.
		return its Calculation results.
	'''
	if '+' in expr:
		a, b = expr.split('+')
		return float(a)+float(b)
	elif '-' in expr:
		a, b = expr.split('-')
		return float(a)-float(b)
	elif '**' in expr:
		a, b = expr.split('**')
		return float(a)**float(b)
	elif '*' in expr:
		a, b = expr.split('*')
		return float(a)*float(b)
	elif '//' in expr:
		a, b = expr.split('//')
		return float(a)//float(b)
	elif '/' in expr:
		a, b = expr.split('/')
		return float(a)/float(b)
	elif '%' in expr:
		a, b = expr.split('%')
		return float(a)%float(b)
	else:
		return False

def Square(lenth=1, issquare=1):
	'''
	calculate the area of the square.
	Or calculate the volume of the cube when arg square == 0
	'''
	if issquare != 0:
		a = lenth ** 2
		print "calculate the area of the square: ", 
		return a
	else:
		a = lenth ** 3
		print "calculate the volume of the cube: ", 
		return a

def Round(radius=1, isball=0):
	'''
	calculate the area of the Round.
	Or calculate the volume of the ball when arg ball == 0
	'''
	if isball == 0:
		a = math.pi * (radius ** 2)
		print "calculate the area of the round: ", 
		return a
	else:
		a = (4/3.0) * math.pi * (radius ** 3)
		print "calculate the volume of the ball: ", 
		return a


