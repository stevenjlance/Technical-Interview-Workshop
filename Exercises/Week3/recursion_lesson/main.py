# Write a function that counts to a value n
# e.g. count(100) counts to 100


def loopCount(n):
	for i in range(n + 1):
		print(i)

def recursive_count(n):
	if n == 0:
		return
	else:
		recursive_count(n - 1)
		print(n)

loopCount(5)
recursive_count(5)


# Write a function that returns the factorial of a number
# E.g. factorial(5) return 120 because 1*2*3*4*5=120

def loopFactorial(n):
	result = 1
	for i in range(1, n + 1):
		result *= i
	return result

def recursive_factorial(n):
	if n == 0:
		return 1
	else:
		return n * recursive_factorial(n - 1)

print(loopFactorial(5))
print(recursive_factorial(5))