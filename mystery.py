candidate = 1
divisors = []

while True:

	for i in range(1,candidate):
		
		if(candidate%i == 0):
		
			divisors.append(i)

	total  = sum(divisors)
	if(total==candidate):
		
		print(candidate)

	divisors = []
	candidate += 1

	powercheck = candidate

	if(powercheck > 9 and powercheck % 10 == 0):
		while(powercheck > 9 and powercheck % 10 == 0):
			powercheck /= 10
		if powercheck == 1:
			print("I just passed number: ")
			print(candidate)
