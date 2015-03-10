# Read and Write file.
# Version 1.0 (Feb, 2015).
# Abid Ali,
# IMaR Gateway Technology, Institute of Technology Tralee

import csv
file = open('C:\Dev\workspace\Python/xyz30round3direction.csv')
reader = csv.reader(file)
file_output = open("output.txt", "w")

for line in reader:
	print(line[0],line[1],line[2], file = file_output)

file.close
file_output.close()