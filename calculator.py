import sys

def calculator(income):
	shouldPay = income * ( 1 - 0.165 ) - 5000
	if shouldPay <= 0:
		tax = 0
	elif shouldPay <= 3000:
		tax = shouldPay * 0.03
	elif shouldPay <= 12000:
		tax = shouldPay * 0.1 - 210
	elif shouldPay <= 25000:
		tax = shouldPay * 0.2 - 1410
	elif shouldPay <= 35000:
		tax = shouldPay * 0.25 - 2660
	elif shouldPay <= 55000:
		tax = shouldPay * 0.3 - 4410
	elif shouldPay <= 80000:
		tax = shouldPay * 0.35 - 7160
	else:
		tax = shouldPay * 0.45 - 15160
	salary = income * ( 1 - 0.165 ) - tax
	return '{:.2f}'.format(salary)

def main():
	for item in sys.argv[1:]:
		idnum, income = item.split(':')
		income = int(income)
		print('{}:{}'.format(idnum,calculator(income)))
		
if __name__ == '__main__':
	main()

