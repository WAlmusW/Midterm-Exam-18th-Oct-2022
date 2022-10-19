def primeRprime(N):
	
	#Search Primes Close to N
	import math
	Primes = []
	limitLow = N - int(N/2)
	limitUp = N + int(N/2)
	limitPrime = math.ceil(math.sqrt(limitUp))
	for X in range(limitLow, limitUp):
		for Y in range(2, limitPrime):
			if X % Y == 0:
				break
		else:
			Primes.append(X)

	#Check Reversed Primes is Prime
	Primes2 = []
	for I in Primes:
		reversedPrime = int(str(I)[::-1])
		limitPrime = math.ceil(math.sqrt(reversedPrime))
		for J in range(2, reversedPrime):
			if reversedPrime % J == 0:
				break
		else:
			Primes2.append(I)
			
	#Check Which One is Closer
	Distance = 99999
	ClosePrime = 0
	for A in Primes2:
		if abs(A - N) < Distance:
			ClosePrime = A
			Distance = abs(A - N)
			
	return ClosePrime