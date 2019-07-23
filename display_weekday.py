
'''
Python program to display weekday
'''
import datetime

st = input('Enter Date(dd-mm-yyyy):')
days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
di = dict(zip(range(0,7),days))
dt = datetime.datetime.strptime(st, '%d-%m-%Y')
week_day = di.get(dt.weekday(),None)
print(f'Week day of {st} is {week_day}')
