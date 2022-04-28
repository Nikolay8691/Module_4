print(' Welcome to Module 4 task 2! Let us get started. ')

#import json

def find_pos(l_srt, new_key) :
	
	len_srt = len(l_srt)

	pos = -2
	if new_key <= l_srt[0] : pos = -1
	elif new_key > l_srt[len_srt - 1] : pos = len_srt
	else:
#		for i in range(len_srt - 1) :
#			if l_srt[i] < new_key <= l_srt[i + 1] : n = i  

		l = -1
		r = len(l_srt)
		while l < r - 1 :
			m = l + int((r - l) / 2)
			if new_key == l_srt[m] : 
				pos = m
				break
			elif new_key > l_srt[m] :
				l = m 
				pos = m 
			else:
				r = m 
				pos = m - 1

	return pos + 1

def insert_list(l_srt, l_uns) :

	len_srt = len(l_srt)
	len_uns = len(l_uns)

#	for i in range(len_uns) :
	for i in l_uns : 
		j = find_pos(l_srt, i)
		l_srt.insert(j, i)

	pass

#main program
l_sorted = [1, 4, 9, 13, 22]
l_unsorted = [5, 9, 0, 2]

#numbers_list = 'datafile4_1.json'

#with open(numbers_list, 'w') as f:
#	json.dump(l_srt,f)

#with open(numbers_list, 'r') as f:
#	l_srt = json.load(f)

print(' list of sorted numbers  : ', l_sorted)
print(' list of unsorted numbers : ', l_unsorted)

insert_list(l_sorted, l_unsorted)

print(' new list of sorted numbers : ', l_sorted)

