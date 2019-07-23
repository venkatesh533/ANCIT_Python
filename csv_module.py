
'''
Program to explain about csv module
'''
import csv

# field names 
fields = ['Name', 'Branch', 'Year', 'CGPA'] 
  
# data rows of csv file 
rows = [ ['Nikhil', 'COE', '2', '9.0'], 
         ['Sanchit', 'COE', '2', '9.1'], 
         ['Aditya', 'IT', '2', '9.3'], 
         ['Sagar', 'SE', '1', '9.5'], 
         ['Prateek', 'MCE', '3', '7.8'], 
         ['Sahil', 'EP', '2', '9.1']] 

with open('csv_write.csv', 'w', newline='') as fp:
	writer = csv.writer(fp)
	## writing header ##
	writer.writerow(fields)
	## writing data(rows) ##
	writer.writerows(rows)


# my data rows as dictionary objects 
mydict =[{'branch': 'COE', 'cgpa': '9.0', 'name': 'Nikhil', 'year': '2'}, 
         {'branch': 'COE', 'cgpa': '9.1', 'name': 'Sanchit', 'year': '2'}, 
         {'branch': 'IT', 'cgpa': '9.3', 'name': 'Aditya', 'year': '2'}, 
         {'branch': 'SE', 'cgpa': '9.5', 'name': 'Sagar', 'year': '1'}, 
         {'branch': 'MCE', 'cgpa': '7.8', 'name': 'Prateek', 'year': '3'}, 
         {'branch': 'EP', 'cgpa': '9.1', 'name': 'Sahil', 'year': '2'}] 

header = ['name','year','branch','cgpa']
## csv file writing ##

with open('csv_file.csv', 'w', newline='') as fp:
    writer = csv.DictWriter(fp, fieldnames=header)

    ## writing header ##
    writer.writeheader()
    ## writing rows ##
    writer.writerows(mydict)
    
    print('Successfully done')


#csv file reading
'''
li = []
with open('csv_file.csv', 'r') as fp_obj:
    reader = csv.reader(fp_obj)
    header = next(reader)
    print(header)
    for i in reader:
        if i:
            di = dict(zip(header,i))
            li.append(di)
    print(li)
'''
