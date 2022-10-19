def AsteriskTriangle(N):
	spaces = N-1
	for X in range(N):
		print((" "*(spaces-X)) + ("* "*(X+1)))
	return ""