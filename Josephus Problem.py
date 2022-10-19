def Josephus_List(people, step):
	people = [X for X in range(1, people+1)]
	skip = step - 1
	index = skip
	
	while len(people) > 1:
		people.pop(index)
		index = (index + skip) % len(people)
	return people[0]



def Josephus_Formula(people, step):
	y = 0
	p = 0
	k = step

	#JF(y, k) = (JF(y-1, k) + k) % (y)
	
	while p < people:
		p += 1
		y = (y+k) % (p)
	return y+1



def Josephus_Recursive(people, index, skip):
	if len(people) == 1:
		return "".join(str(X) for X in people)
	else:
		people.pop(index)
		index = (index + skip) % len(people)
		return Josephus_Recursive(people, index, skip)