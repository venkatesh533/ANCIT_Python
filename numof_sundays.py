
'''
Python Program to display no of sundays between two years
Input: y1=2019, y2=2019
Output: Sundays count:52
'''

import datetime

y1 = int(input('First Year:'))
y2 = int(input('Second Year:'))
sun = 0
months_31 = '1,3,5,7,8,10,12'
months_30 = '4,6,9,11'

if y2 >= y1:
	for i in range(y1,y2+1):
		for j in range(1,13):
			if j == 2 and i%4 == 0:
				end = 30
			elif j == 2 and i%4 != 0:
				end = 29
			elif str(j) in months_31:
				end = 32
			else:
				end = 31
			for k in range(1,end):
				d1 = '%d-%d-%d' %(k,j,i)
				d1 = datetime.datetime.strptime(d1, '%d-%m-%Y')
				if d1.weekday() == 0:
					#print(d1.date(),end=',')
					sun += 1
else:
	print('Second year should be greater than first year')
print('Mondays count:',sun)