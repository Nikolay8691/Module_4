print(' Welcome to binary search! Let us get started. ')

import json

#matrix = [1, 4, 9, 13, 22]
numbers_list = 'datafile4_1.json'

#with open(numbers_list, 'w') as f:
#	json.dump(matrix,f)

with open(numbers_list, 'r') as f:
	matrix = json.load(f)

print(matrix)

key = int(input( ' Input the figure you are searching for : '))

l = -1
r = len(matrix)
result = False
n = -1

while l < r - 1 :
	m = l + int((r - l) / 2)
	if key == matrix[m] : 
		n = m
		result = True
		break
	elif key > matrix[m] :
		l = m 
	else:
		r = m 

if n == -1 : s = ' None '
else: s = str(n)
print(' result = ', result, ' position in matrix = ', s)