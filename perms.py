
def perms(lst,j):

	for i in range(len(lst)):
		if lst[i] == j:
			pass
		else:
			temp = lst[i]
			if lst[i] == lst[len(lst)-1]:
				lst[i] = lst[0]
				lst[0] = temp
			else:
				lst[i] = lst[i+1]
				lst[i+1] = temp
		print(lst)


def solve(lst):
	lst.sort()
	
	for i in range(len(lst)):
		lst.sort()
		for j in range(len(lst)):
			copy = lst
			sj = lst[j]
			perms(copy,sj)
			temp = lst[j]
			if lst[j] == lst[len(lst)-1]:
				lst[j] = lst[0]
				lst[0] = temp
			else:
				lst[j] = lst[j+1]
				temp = lst[j+1] 



solve([1,2,3,4,5,6,7,8,9,10,11,12])





