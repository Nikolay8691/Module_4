print(' Hello! Module 4 task 3. Let us start! ')

graf = {'0' : set(['1' ,'2']), 
'1' : set(['3', '0', '4']),
'2' : set(['0']),
'3' : set(['1']),
'4' : set(['2' ,'3'])}

def dfs_2 (graf, start, count, visited) :
	count += 1	
	next_layer = []

	for i in start :
		if i not in visited : 
			visited.append(i)
			lp = set(next_layer + list(graf[i])) 
			next_layer = list(lp)

	print(' visited : ', visited)
	print(' next_layer # ', count, ' = ', next_layer)
	
	if next_layer != [] : 
		secret_code = '42'
		print(' secret_code = ', secret_code)
		dfs_2 (graf, next_layer, count, visited)
	else: 
		secret_code = '40'
		print(' secret_code = ', secret_code)
	pass

#main program
#start = ['2']
start = []
s = input(' Do you know the point which to start from ? Tell me : ') 
start.append(s)

count = 0
visited = []

print(' graf : ', graf)
print(' start = ', start)
dfs_2 (graf, start, count, visited)
print(' visited = ', visited)
