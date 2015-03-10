# Find and delete.
# Version 1.0 (Feb, 2015).
# Abid Ali,
# IMaR Gateway Technology, Institute of Technology Tralee

import csv
fn = 'C:\Dev\workspace\Python/output.txt'
f =  open(fn)
output = []

for line in f:
    if not "delete" in line:
             output.append(line)
f.close()
f = open(fn, 'w')
f.writelines(output)
f.close()