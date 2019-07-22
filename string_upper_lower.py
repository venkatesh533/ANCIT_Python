
'''
Input: I am ANCIT
Output: i AM ancit
'''

st = input('Enter String:')
pv = ''
for i in st:
	if i.isupper():
		p = i.lower()
	elif i.islower():
		p = i.upper()
	else:
		p = i
	pv += p
print(pv)