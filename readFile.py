import csv
file = open('C:\Dev\workspace\Python\xyz30round3direction.csv')
reader = csv.reader(file)
for line in reader:
	print(line[0],line[1],line[2])
file.close