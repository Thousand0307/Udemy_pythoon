def find_max(a_list):
	find_max = 0
	for i in a_list:
		if find_max == 0:
			find_max = i
		elif i > find_max:
			find_max = i
		continue
	print(find_max)

answer1 = find_max([1,2,3])
answer2 = find_max([1,-1,-5])
answer3 = find_max([-8,-1,-5])
answer4 = find_max([])